import os

from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin, Config
from mkdocs.structure.files import File, Files
from yaml import safe_load


class UgentPlugin(BasePlugin):
    config_scheme = (
            ('os_pick', Type(bool, default=False)),
            ('yamls', Type(list, default=[]))
            )

    def __init__(self, *args, **kwargs):
        super(UgentPlugin, self).__init__(*args, **kwargs)
        self.os_pick = None
        self.yamls = None

    def on_config(self, config: Config):
        self.os_pick = self.config['os_pick']
        self.yamls = self.config['yamls']
        # with open('constants.yml', 'r') as file:
        #     constants = safe_load(file)
        # config.get('extra', default={}).update(constants)
        return config

    def get_uri(self, obj, prefix=None):
        res = {}
        if isinstance(obj, dict):
            for key, el in obj.items():
                if prefix:
                    res[prefix + (key,)] = self.get_uri(el)
                    print(res)
                else:
                    res[(key,)] = self.get_uri(el)
        else:
            res = list(obj)
        return res

    def get_uris(self, files, config):
        uris = []
        for yml in self.yamls:
            with open(yml, 'r') as file:
                config = safe_load(file)
            uris += self.get_uri(config['nav'])
        return uris

    def on_files(self, files: Files, config: Config):
        if self.os_pick:
            print(self.get_uris(files, config))
        # exit()
        docs = {
                ('Home',):
                    {
                            'Linux': 'index.md',
                            'Windows': 'index.md',
                            'MacOS': 'index.md',
                            },
                ('HPC Tutorial', 'Getting an HPC Account'): {
                        'Linux': 'intro-HPC/Antwerpen/Linux/intro-HPC/ch_account.md',
                        'Windows': 'intro-HPC/ch_account.md',
                        'MacOS': 'intro-HPC/ch_account.md',
                        },
                }
        os_picker_dir = "os_pickers"

        os_pick_per_site_dir = os.path.pardir
        fst: File = files.documentation_pages()[0]

        # new_file = File('../index.md', 'docs')


        # os.rmdir(os_picker_dir)
        # os.mkdir(os_picker_dir)
        # for k, v in docs.items():
        #     for doc in v.values():
        #         files.append(File(path=doc, src_dir=os.path.dirname(doc),
        #                           dest_dir=os_picker_dir, use_directory_urls=False))
        # os.rmdir(os_picker_dir)
        # print(files.documentation_pages())
        # exit(0)
        return files
