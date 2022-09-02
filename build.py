import os.path
import subprocess

from yaml import safe_load
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get args.')
    parser.add_argument('--skip-docs', '-l', action='store_true', dest='skip_docs',
                        help='Skip building documentation pages. Build only landing page.')
    parser.add_argument('--skip-landing-page', '-d', action='store_true', dest='skip_landing_page',
                        help='Skip building landing page. Build only documentation pages.')

    args = parser.parse_args()

    config_yml = 'build_config.yml'
    landing_page_yml = 'mkdocs_landing_page.yml'
    landing_page_dir = 'HPC'

    build_dir = 'build'

    os.makedirs(build_dir, exist_ok=True)

    with open(config_yml, 'r') as file:
        config = safe_load(file)

    if not args.skip_landing_page:
        subprocess.run(f'mkdocs build -f {landing_page_yml} -d'
                       f'{os.path.join(build_dir, landing_page_dir)}', shell=True)
        sites = set()
        for el in config.get('os_picks', None):
            for subsite_dir, subsite_yml in el.items():
                subprocess.run(f'mkdocs build -f {subsite_yml} -d '
                               f'{os.path.join(build_dir, landing_page_dir, subsite_dir)}', shell=True)
    if not args.skip_docs:
        for el in config.get('docs', None):
            for subsite_dir, subsite_yml in el.items():
                subprocess.run(f'mkdocs build -f {subsite_yml} -d '
                               f'{os.path.join(build_dir, landing_page_dir, subsite_dir)}', shell=True)
