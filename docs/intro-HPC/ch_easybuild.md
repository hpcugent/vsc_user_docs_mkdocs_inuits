# Easybuild { #ch:easybuild}

## What is Easybuild?

You can use EasyBuild to build and install supported software in your
own VSC account, rather than requesting a central installation by the
HPC support team.

EasyBuild (<https://easybuilders.github.io/easybuild>) is the software
build and installation framework that was created by the HPC-UGent team,
and has recently been picked up by HPC sites around the world. It allows
you to manage (scientific) software on High Performance Computing (HPC)
systems in an efficient way.

## When should I use Easybuild?

For general software installation requests, please see . However, there
might be reasons to install the software yourself:

-   applying custom patches to the software that only you or your group
    are using

-   evaluating new software versions prior to requesting a central
    software installation

-   installing (very) old software versions that are no longer eligible
    for central installation (on new clusters)

## Configuring EasyBuild

Before you use EasyBuild, you need to configure it:

### Path to sources

This is where EasyBuild can find software sources:

::: prompt
:::

-   the first directory `$VSC_DATA/easybuild/sources` is where EasyBuild
    will (try to) automatically download sources if they're not
    available yet

-   `/apps/gent/source` is the central "cache" for already downloaded
    sources, and will be considered by EasyBuild before downloading
    anything

### Build directory

This directory is where EasyBuild will build software in. To have good
performance, this needs to be on a fast filesystem.

::: prompt
:::

On cluster nodes, you can use the fast, in-memory `/dev/shm/$USER`
location as a build directory.

### Software install location

This is where EasyBuild will install the software (and accompanying
modules) to.

For example, to let it use `$VSC_DATA/easybuild`, use:

::: prompt
:::

Using the `$VSC_OS_LOCAL`, `$VSC_ARCH` and `$VSC_ARCH_SUFFIX`
environment variables ensures that your install software to a location
that is specific to the cluster you are building for.

Make sure you , since the loaded `cluster` module determines the
location of the installed software. Software built on the login nodes
may not work on the cluster you want to use the software on (see also ).

To share custom software installations with members of your VO, replace
`$VSC_DATA` with `$VSC_DATA_VO` in the example above.

## Using EasyBuild

Before using EasyBuild, you first need to load the `EasyBuild` module.
We don't specify a version here (this is an exception, for most other
modules you should, see ) because newer versions might include important
bug fixes.

::: prompt
module load EasyBuild
:::

### Installing supported software

EasyBuild provides a large collection of readily available software
versions, combined with a particular toolchain version. Use the
`--search` (or `-S`) functionality to see which different 'easyconfigs'
(build recipes, see
<http://easybuild.readthedocs.org/en/latest/Concepts_and_Terminology.html#easyconfig-files>)
are available:

For readily available easyconfigs, just specify the name of the
easyconfig file to build and install the corresponding software package:

::: prompt
:::

### Installing variants on supported software

To install small variants on supported software, e.g., a different
software version, or using a different compiler toolchain, use the
corresponding `--try-X` options:

To try to install `example v1.2.6`, based on the easyconfig file for
`example v1.2.5`:

::: prompt
:::

To try to install example v1.2.5 with a different compiler toolchain:

::: prompt
:::

### Install other software

To install other, not yet supported, software, you will need to provide
the required easyconfig files yourself. See
<https://easybuild.readthedocs.org/en/latest/Writing_easyconfig_files.html>
for more information.

## Using the installed modules

To use the modules you installed with EasyBuild, extend `$MODULEPATH` to
make them accessible for loading:

::: prompt
:::

It makes sense to put this `module use` command and all `export`
commands in your `.bashrc` login script. That way you don't have to type
these commands every time you want to use EasyBuild or you want to load
modules generated with EasyBuild. See also [the section on `.bashrc` in
the "Beyond the basics" chapter of the intro to
Linux](\LinuxManualURL#sec:bashrc-login-script).
