# UGent HPC - pdf2wiki
## Introduction
UGent HPC currently has user manuals in LaTex. Sources can be found here: https://github.com/hpcugent/vsc_user_docs
Pdf versions can be found here: https://www.ugent.be/hpc/en/support/documentation.htm

There are different variants for each VSC site and for each operating system.

## Requirements
**Python version 3.6 and greater is required.**

Install requirements by running:
```shell
python -m pip install -r requirements.txt
```
Install custom plugin present in this repository (at least for now):
```shell
python -m pip install -e custom_plugin
```


## Configuration
Every site has 3 configuration yamls. One for each OS. Naming convention is like this:
`mkdocs_Antwerpen_Linux.yml`.

Common constants are defined in `constants.yml`.

Configuration for OS picker utility is defined in config files with naming convention like: `mkdocs_Antwerpen_OS_pick.yml`.

Configuration for landing page is defined in `mkdocs_landing_page.yml`.

Configuration for documentation building script `build.py` is in `build_config.yml`.

When editing content, only specific site-OS yaml could be affected.
When adding or removing new site or OS except for site-OS yamls also other yamls are affected. 
## Build
Usage:
```shell
python build.py [options]
```
Options:
```shell
-l, --skip-docs           Build only landing page. Skip building documentation pages. 
-d, --skip-landing-page   Build only documentation pages. Skip building landing page. 
```
Without options it will build all documentation defined in `build_config.yml` and also landing page.
```shell
python build.py
```
In directory `./build/` there will be built landing page called HPC for prettier url and site-OS hierarchy.
According to config, there will be folder structure with documentation content.

## Run website locally
Move to root directory of your static website:
```shell
cd build/HPC
```
Run simple HTTP server:
```shell
python -m http.server --cgi 8000
```
Visit `localhost:8000` and start looking around your documentation.

    