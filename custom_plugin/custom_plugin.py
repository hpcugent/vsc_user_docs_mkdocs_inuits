import shutil
from os import path, makedirs

from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin, Config
from mkdocs.structure.files import File, Files
from yaml import safe_load

os_pick_str = """---
hide:
  - navigation
  - toc
---

# Please select your operating system:
{{%- if {linux_valid} %}}
[Linux]({linux_url}){{ .md-button }}
{{%- endif %}}
{{%- if {macos_valid} %}}
[MacOS]({macos_url}){{ .md-button }}
{{%- endif %}}
{{%- if {windows_valid} %}}
[Windows]({windows_url}){{ .md-button }}
{{%- endif %}}
"""

tmp_dir = path.join("tmp_dir")


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
        return config

    def get_docs(self):
        """
        Parse 'nav' data from defined yamls.
        :return:
        """
        uris = []
        for yml in self.yamls:
            with open(yml, 'r') as file:
                config = safe_load(file)
            opsys = config.get('extra').get('OS')
            uris.append((opsys, config.get('nav')))
        return uris

    def to_flat(self, docs, opsys, parkey, parvalues):
        if type(parvalues) is dict:
            key, value = list(parvalues.items())[0]
            if type(value) is list:
                docs = self.to_flat(docs, opsys, (parkey + (key,)), value)
            else:
                docs[parkey + (key,)] = docs.get((parkey + (key,)), dict({})) | {opsys: value}
        elif type(parvalues) is list:
            for parvalue in parvalues:
                docs = self.to_flat(docs, opsys, parkey, parvalue)
        return docs

    def on_files(self, files: Files, config: Config):
        extras = config.get("extra")
        if self.os_pick:
            docs_with_os = self.get_docs()

            flatten_docs = dict()
            for el in docs_with_os:
                opsys, docs = el
                for doc in docs:
                    key, value = list(doc.items())[0]
                    if type(value) is list:
                        for val in value:
                            flatten_docs = self.to_flat(flatten_docs, opsys, (key,), val)
                    else:
                        flatten_docs[(key,)] = flatten_docs.get((key,), dict({})) | {opsys: value}

            for name_chain, links_with_os in list(flatten_docs.items()):
                for opsys, link in list(links_with_os.items()):
                    file_src_dir, file_name = path.split(link)
                    base = len(path.splitext(link)[0].split("/")) * "../"
                    if 'index.md' in file_name:
                        base = (len(path.splitext(link)[0].split("/")) - 1) * "../"

                    lin_link = base + "Linux/" + path.splitext(links_with_os["Linux"])[0] if links_with_os.get(
                        "Linux") else None
                    mac_link = base + "MacOS/" + path.splitext(links_with_os["MacOS"])[0] if links_with_os.get(
                        "MacOS") else None
                    win_link = base + "Windows/" + path.splitext(links_with_os["Windows"])[0] if links_with_os.get(
                        "Windows") else None

                    if 'index.md' in file_name:
                        lin_link = base + "Linux/" + path.dirname(links_with_os["Linux"]) if links_with_os.get(
                            "Linux") else None
                        mac_link = base + "MacOS/" + path.dirname(links_with_os["MacOS"]) if links_with_os.get(
                            "MacOS") else None
                        win_link = base + "Windows/" + path.dirname(links_with_os["Windows"]) if links_with_os.get(
                            "Windows") else None

                    os_pick_with_urls = os_pick_str.format(linux_valid=(lin_link is not None),
                                                           macos_valid=(mac_link is not None),
                                                           windows_valid=(win_link is not None),
                                                           linux_url=lin_link,
                                                           macos_url=mac_link,
                                                           windows_url=win_link)
                    os_pick_dir_path = path.normpath(path.join(tmp_dir, file_src_dir))
                    os_pick_file_path = path.join(os_pick_dir_path, file_name)

                    if not path.exists(os_pick_dir_path):
                        makedirs(os_pick_dir_path)

                    with open(os_pick_file_path, 'w') as file:
                        file.write(os_pick_with_urls)

                    new_file = File(file_name, path.abspath(os_pick_dir_path),
                                    path.join(path.abspath(extras.get('build_dir')), file_src_dir),
                                    use_directory_urls=True)
                    files.append(new_file)
        return files

    def on_post_build(self, config: Config):
        shutil.rmtree(tmp_dir, ignore_errors=True)
