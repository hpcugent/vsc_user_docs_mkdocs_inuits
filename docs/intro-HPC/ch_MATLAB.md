# MATLAB { #ch:matlab}

## Why is the MATLAB compiler required?

The main reason behind this alternative way of using MATLAB is
licensing: only a limited number of MATLAB sessions can be active at the
same time. However, once the MATLAB program is compiled using the MATLAB
compiler, the resulting stand-alone executable can be run without
needing to contact the license server.

Note that a license is required for the MATLAB Compiler, see
<https://nl.mathworks.com/help/compiler/index.html>. If the `mcc`
command is provided by the MATLAB installation you are using, the MATLAB
compiler can be used as explained below.

Only a limited amount of MATLAB sessions can be active at the same time
because there are only a limited amount of MATLAB research licenses
available on the MATLAB license server. If each job would need a
license, licenses would quickly run out.

## How to compile MATLAB code

Compiling MATLAB code can only be done from the login nodes, because
only login nodes can access the MATLAB license server, workernodes on
clusters can not.

To access the MATLAB compiler, the `MATLAB` module should be loaded
first. Make sure you are using the same `MATLAB` version to compile and
to run the compiled MATLAB program.

::: prompt
---------------------- MATLAB/2016b MATLAB/2017b MATLAB/2018a (D)
:::

After loading the `MATLAB` module, the `mcc` command can be used. To get
help on `mcc`, you can run `mcc -?`.

To compile a standalone application, the `-m` flag is used (the `-v`
flag means verbose output). To show how `mcc` can be used, we use the
`magicsquare` example that comes with MATLAB.

First, we copy the `magicsquare.m` example that comes with MATLAB to
`example.m`:

::: prompt
:::

To compile a MATLAB program, use `mcc -mv`:

::: prompt
Opening log file: Compiler version: 6.6 (R2018a) Dependency analysis by
REQUIREMENTS. Parsing file \" (Referenced from: \"Compiler Command
Line\"). Deleting 0 temporary MEX authorization files. Generating file
\" Generating file \"run_example.sh\".
:::

### Libraries

To compile a MATLAB program that *needs a library*, you can use the
`-I library_path` flag. This will tell the compiler to also look for
files in `library_path`.

It's also possible to use the `-a path` flag. That will result in all
files under the `path` getting added to the final executable.

For example, the command `mcc -mv example.m -I examplelib -a datafiles`
will compile `example.m` with the MATLAB files in `examplelib`, and will
include all files in the `datafiles` directory in the binary it
produces.

### Memory issues during compilation

If you are seeing Java memory issues during the compilation of your
MATLAB program on the login nodes, consider tweaking the default maximum
heap size (128M) of Java using the `_JAVA_OPTIONS` environment variable
with:

::: prompt
:::

The MATLAB compiler spawns multiple Java processes, and because of the
default memory limits that are in effect on the login nodes, this might
lead to a crash of the compiler if it's trying to create to many Java
processes. If we lower the heap size, more Java processes will be able
to fit in memory.

Another possible issue is that the heap size is too small. This could
result in errors like:

::: prompt
Error: Out of memory
:::

A possible solution to this is by setting the maximum heap size to be
bigger:

::: prompt
:::

## Multithreading

MATLAB can only use the cores in a single workernode (unless the
Distributed Computing toolbox is used, see
<https://nl.mathworks.com/products/distriben.html>).

The amount of workers used by MATLAB for the parallel toolbox can be
controlled via the `parpool` function: `parpool(16)` will use 16
workers. It's best to specify the amount of workers, because otherwise
you might not harness the full compute power available (if you have too
few workers), or you might negatively impact performance (if you have
too much workers). By default, MATLAB uses a fixed number of workers
(12).

You should use a number of workers that is equal to the number of cores
you requested when submitting your job script (the `ppn` value, see ).
You can determine the right number of workers to use via the following
code snippet in your MATLAB program:

See also [the parpool
documentation](https://nl.mathworks.com/help/distcomp/parpool.html).

## Java output logs

Each time MATLAB is executed, it generates a Java log file in the users
home directory. The output log directory can be changed using:

::: prompt
:::

where `<OUTPUT_DIR>` is the name of the desired output directory. To
create and use a temporary directory for these logs:

::: prompt
\# create unique temporary directory in $TMPDIR (or /tmp/$USER if
$TMPDIR is not defined)
# instruct MATLAB to use this directory for log files by setting$MATLAB_LOG_DIR
:::

You should remove the directory at the end of your job script:

::: prompt
:::

## Cache location

When running, MATLAB will use a cache for performance reasons. This
location and size of this cache can be changed trough the
`MCR_CACHE_ROOT` and `MCR_CACHE_SIZE` environment variables.

The snippet below would set the maximum cache size to 1024MB and the
location to `/tmp/testdirectory`.

::: prompt
:::

So when MATLAB is running, it can fill up to 1024MB of cache in
`/tmp/testdirectory`.

## MATLAB job script

All of the tweaks needed to get MATLAB working have been implemented in
an example job script. This job script is also available on the HPC.
