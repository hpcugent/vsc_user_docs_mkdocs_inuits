import argparse
import os.path
import shutil
import subprocess
from shutil import rmtree

from yaml import safe_load


class BuildException(Exception):
    """Build exception."""

    def __init__(self, message=""):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"""\nSubprocess stderr:\n{self.message}\nBuild process failed. -> Cleaning up and exiting.\nTo ignore errors and finish all partial builds, use option '--ignore-errors'.\n"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get args.')
    parser.add_argument('--skip-docs', '-l', action='store_true', dest='skip_docs',
                        help='Skip building documentation pages. Build only landing page.')
    parser.add_argument('--skip-landing-page', '-d', action='store_true', dest='skip_landing_page',
                        help='Skip building landing page. Build only documentation pages.')
    parser.add_argument('--ignore-errors', action='store_true', dest='ignore_errors',
                        help='Ignore errors in partial mkdocs builds and continue with build process.')
    parser.add_argument('--verbose', '-v', action='store_true', dest='verbose',
                        help='Enable verbose logging.')

    args = parser.parse_args()

    config_yml = 'build_config.yml'
    landing_page_yml = 'mkdocs_landing_page.yml'

    with open(landing_page_yml, 'r') as file:
        extra = safe_load(file).get('extra')

    build_dir = extra.get('build_dir')

    os.makedirs(build_dir, exist_ok=True)

    with open(config_yml, 'r') as file:
        config = safe_load(file)

    clean_build_dir = False
    try:
        # Build landing page.
        if not args.skip_landing_page:
            subp = subprocess.run(f'mkdocs build -f {landing_page_yml} -d'
                                  f'{os.path.join(build_dir)}', shell=True, capture_output=True)
            if not args.ignore_errors and subp.returncode != 0:
                clean_build_dir = True
                raise BuildException(subp.stderr.decode('utf8'))
            if args.verbose and subp.stdout:
                print(subp.stdout.decode('utf8'))
            sites = set()
            for el in config.get('os_picks', None):
                for subsite_dir, subsite_yml in el.items():
                    subp = subprocess.run(f'mkdocs build -f {subsite_yml} -d '
                                          f'{os.path.join(build_dir, subsite_dir)}', shell=True,
                                          capture_output=True)
                    if not args.ignore_errors and subp.returncode != 0:
                        clean_build_dir = True
                        raise BuildException(subp.stderr.decode('utf8'))
                    if args.verbose and subp.stdout:
                        print(subp.stdout.decode('utf8'))
        # Build documentation files.
        if not args.skip_docs:
            for el in config.get('docs', None):
                for subsite_dir, subsite_yml in el.items():
                    subp = subprocess.run(f'mkdocs build -f {subsite_yml} -d '
                                          f'{os.path.join(build_dir, subsite_dir)}', shell=True,
                                          capture_output=True)
                    if not args.ignore_errors and subp.returncode != 0:
                        clean_build_dir = True
                        raise BuildException(subp.stderr.decode('utf8'))
                    if args.verbose and subp.stdout:
                        print(subp.stdout.decode('utf8'))

        # Fix styling for OS picking pages.
        if not args.skip_landing_page:
            assets = os.path.normpath(os.path.join(build_dir, 'assets'))
            assert os.path.isdir(assets)

            # Save old assets.
            assets_old = os.path.join(os.path.dirname(assets), 'assets_old')
            shutil.copytree(assets, assets_old)

            # Remove 'javascript' sub-folder as it is not necessary for OS picking files.
            shutil.rmtree(os.path.join(assets, 'javascripts'))

            # Copy assets to all OS picking sub-dirs.
            for r, d, f in os.walk(build_dir):
                for directory in d:
                    if 'assets' not in r and 'assets' not in directory and not os.path.isdir(
                            os.path.join(r, directory, 'assets')):
                        shutil.copytree(assets, os.path.normpath(os.path.join(r, directory, 'assets')))

            # Restore original assets.
            shutil.rmtree(assets)
            shutil.move(assets_old, assets)

    except BuildException as exc:
        rmtree(build_dir, ignore_errors=True)
        raise exc
