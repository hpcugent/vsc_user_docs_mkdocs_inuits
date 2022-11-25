# Running batch jobs { #ch:running-batch-jobs}

In order to have access to the compute nodes of a cluster, you have to
use the job system. The system software that handles your batch jobs
consists of two pieces: the queue- and resource manager and the
scheduler . Together, TORQUE and Moab provide a suite of commands for
submitting jobs, altering some of the properties of waiting jobs (such
as reordering or deleting them), monitoring their progress and killing
ones that are having problems or are no longer needed. Only the most
commonly used commands are mentioned here.

::: center
![image](ch4-pbs-overview){width="5.78in" height="3.94in"}
:::

When you connect to the , you have access to (one of) the of the
cluster. There you can prepare the work you want to get done on the
cluster by, e.g., installing or compiling programs, setting up data
sets, etc. The computations however, should not be performed on this
login node. The actual work is done on the cluster's . Each compute node
contains a number of CPU . The compute nodes are managed by the job
scheduling software (Moab) and a Resource Manager (TORQUE), which
decides when and on which compute nodes the jobs can run. It is usually
not necessary to log on to the compute nodes directly and is only
allowed on the nodes where you have a job running and is only allowed on
the nodes where you have a job running . Users can (and should) monitor
their jobs periodically as they run, but do not have to remain connected
to the the entire time.

The documentation in this "Running batch jobs" section includes a
description of the general features of job scripts, how to submit them
for execution and how to monitor their progress.

## Modules { #sec:modules}

Software installation and maintenance on a cluster such as the VSC
clusters poses a number of challenges not encountered on a workstation
or a departmental cluster. We therefore need a system on the , which is
able to easily activate or deactivate the software packages that you
require for your program execution.

### Environment Variables

The program environment on the is controlled by pre-defined settings,
which are stored in environment (or shell) variables. For more
information about environment variables, see [the chapter "Getting
started", section "Variables" in the intro to
Linux](\LinuxManualURL#sec:environment-variables).

All the software packages that are installed on the cluster require
different settings. These packages include compilers, interpreters,
mathematical software such as MATLAB and SAS, as well as other
applications and libraries.

### The module command

In order to administer the active software and their environment
variables, the module system has been developed, which:

1.  Activates or deactivates *software packages* and their dependencies.

2.  Allows setting and unsetting of *environment variables*, including
    adding and deleting entries from list-like environment variables.

3.  Does this in a *shell-independent* fashion (necessary information is
    stored in the accompanying module file).

4.  Takes care of *versioning aspects*: For many libraries, multiple
    versions are installed and maintained. The module system also takes
    care of the versioning of software packages. For instance, it does
    not allow multiple versions to be loaded at same time.

5.  Takes care of *dependencies*: Another issue arises when one
    considers library versions and the dependencies they require. Some
    software requires an older version of a particular library to run
    correctly (or at all). Hence a variety of version numbers is
    available for important libraries. Modules typically load the
    required dependencies automatically.

This is all managed with the `module` command, which is explained in the
next sections.

There is also a shorter `ml` command that does exactly the same as the
`module` command and is easier to type. Whenever you see a `module`
command, you can replace `module` with `ml`.

### Available modules

A large number of software packages are installed on the clusters. A
list of all currently available software can be obtained by typing:

::: prompt
:::

It's also possible to execute `module av` or `module avail`, these are
shorter to type and will do the same thing.

This will give some output such as:

This gives a full list of software packages that can be loaded.

: lowercase and uppercase letters matter in module names.

### Organisation of modules in toolchains

The amount of modules on the VSC systems can be overwhelming, and it is
not always immediately clear which modules can be loaded safely together
if you need to combine multiple programs in a single job to get your
work done.

Therefore the VSC has defined so-called . A toolchain contains a C/C++
and Fortran compiler, a MPI library and some basic math libraries for
(dense matrix) linear algebra and FFT. Two toolchains are defined on
most VSC systems. One, the `intel` toolchain, consists of the Intel
compilers, MPI library and math libraries. The other one, the `foss`
toolchain, consists of Open Source components: the GNU compilers,
OpenMPI, OpenBLAS and the standard LAPACK and ScaLAPACK libraries for
the linear algebra operations and the FFTW library for FFT. The
toolchains are refreshed twice a year, which is reflected in their name.

E.g., `foss/a` is the first version of the `foss` toolchain in .

The toolchains are then used to compile a lot of the software installed
on the VSC clusters. You can recognise those packages easily as they all
contain the name of the toolchain after the version number in their name
(e.g., `Python/2.7.12-intel-2016b`). Only packages compiled with the
same toolchain name and version can work together without conflicts.

### Loading and unloading modules { #subsec:activating-and-deactivating-modules}

#### module load

To "activate" a software package, you load the corresponding module file
using the `module load` command:

::: prompt
:::

This will load the most recent version of *example*.

For some packages, multiple versions are installed; the load command
will automatically choose the default version (if it was set by the
system administrators) or the most recent version otherwise (i.e., the
lexicographical last after the `/`).

:

::: prompt
:::

The `ml` command is a shorthand for `module load`: `ml example/1.2.3` is
equivalent to `module load example/1.2.3`.

Modules need not be loaded one by one; the two `module load` commands
can be combined as follows:

::: prompt
:::

This will load the two modules as well as their dependencies (unless
there are conflicts between both modules).

#### module list

Obviously, you need to be able to keep track of the modules that are
currently loaded. Assuming you have run the `module load` commands
stated above, you will get the following:

::: prompt
Currently Loaded Modulefiles: 1) example/1.2.3 6)
imkl/11.3.3.210-iimpi-2016b 2) GCCcore/5.4.0 7) intel/2016b 3)
icc/2016.3.210-GCC-5.4.0-2.26 8) examplelib/1.2-intel-2016b 4)
ifort/2016.3.210-GCC-5.4.0-2.26 9) secondexample/2.7-intel-2016b 5)
impi/5.1.3.181-iccifort-2016.3.210-GCC-5.4.0-2.26
:::

You can also just use the `ml` command without arguments to list loaded
modules.

It is important to note at this point that other modules (e.g.,
`intel/2016b`) are also listed, although the user did not explicitly
load them. This is because `secondexample/2.7-intel-2016b` depends on it
(as indicated in its name), and the system administrator specified that
the `intel/2016b` module should be loaded whenever *this*
`secondexample` module is loaded. There are advantages and disadvantages
to this, so be aware of automatically loaded modules whenever things go
wrong: they may have something to do with it!

#### module unload

To unload a module, one can use the `module unload` command. It works
consistently with the `load` command, and reverses the latter's effect.
However, the dependencies of the package are NOT automatically unloaded;
you will have to unload the packages one by one. When the
`secondexample` module is unloaded, only the following modules remain:

::: prompt
Currently Loaded Modulefiles: Currently Loaded Modulefiles: 1)
example/1.2.3 5) impi/5.1.3.181-iccifort-2016.3.210-GCC-5.4.0-2.26 2)
GCCcore/5.4.0 6) imkl/11.3.3.210-iimpi-2016b 3)
icc/2016.3.210-GCC-5.4.0-2.26 7) intel/2016b 4)
ifort/2016.3.210-GCC-5.4.0-2.26 8) examplelib/1.2-intel-2016b
:::

To unload the `secondexample` module, you can also use
`ml -secondexample`.

Notice that the version was not specified: there can only be one version
of a module loaded at a time, so unloading modules by name is not
ambiguous. However, checking the list of currently loaded modules is
always a good idea, since unloading a module that is currently not
loaded will *not* result in an error.

### Purging all modules { #subsec:purging-modules}

In order to unload all modules at once, and hence be sure to start in a
clean state, you can use:

::: prompt
:::

This is always safe: the `cluster` module (the module that specifies
which cluster jobs will get submitted to) will not be unloaded (because
it's a so-called "sticky" module). However, on some VSC clusters you may
be left with a very empty list of available modules after executing
`module purge`. On those systems, `module av` will show you a list of
modules containing the name of a cluster or a particular feature of a
section of the cluster, and loading the appropriate module will restore
the module list applicable to that particular system.

### Using explicit version numbers { #subsec:explicit-version-numbers}

Once a module has been installed on the cluster, the executables or
libraries it comprises are never modified. This policy ensures that the
user's programs will run consistently, at least if the user specifies a
specific version. .

Consider the following example: the user decides to use the `example`
module and at that point in time, just a single version 1.2.3 is
installed on the cluster. The user loads the module using:

::: prompt
:::

rather than

::: prompt
:::

Everything works fine, up to the point where a new version of `example`
is installed, 4.5.6. From then on, the user's `load` command will load
the latter version, rather than the intended one, which may lead to
unexpected problems. See for example .

Consider the following `example` modules:

::: prompt
example/1.2.3 example/4.5.6
:::

Let's now generate a version conflict with the `example` module, and see
what happens.

::: prompt
example/1.2.3 example/4.5.6 Lmod has detected the following error: A
different version of the 'example' module is already loaded (see output
of 'ml').
:::

::: prompt
example/1.2.3 example/4.5.6 example/4.5.6(12):ERROR:150: Module
'example/4.5.6' conflicts with the currently loaded module(s)
'example/1.2.3' example/4.5.6(12):ERROR:102: Tcl command execution
failed: conflict example
:::

Note: A `module swap` command combines the appropriate `module unload`
and `module load` commands.

### Search for modules

With the `module spider` command, you can search for modules:

::: prompt
--------------------------------------------------------------------------------
example:
--------------------------------------------------------------------------------
Description: This is just an example

Versions: example/1.2.3 example/4.5.6
--------------------------------------------------------------------------------
For detailed information about a specific \"example\" module (including
how to load the modules) use the module's full name. For example:

module spider example/1.2.3
--------------------------------------------------------------------------------
:::

It's also possible to get detailed information about a specific module:

::: prompt
------------------------------------------------------------------------------------------
example: example/1.2.3
------------------------------------------------------------------------------------------
Description: This is just an example You will need to load all module(s)
on any one of the lines below before the \"example/1.2.3\" module is
available to load.

cluster/doduo cluster/joltik cluster/kirlia cluster/skitty
cluster/swalot cluster/victini This module can be loaded directly:
module load example/1.2.3 Help:

Description =========== This is just an example

More information ================ - Homepage: https://example.com
:::

### Get detailed info

To get a list of all possible commands, type:

::: prompt
:::

Or to get more information about one specific module package:

::: prompt
----------- Module Specific Help for 'example/1.2.3'
--------------------------- This is just an example - Homepage:
https://example.com/
:::

### Save and load collections of modules { #sec:lmod-module-collection}

If you have a set of modules that you need to load often, you can save
these in a *collection*. This will enable you to load all the modules
you need with a single command.

In each `module` command shown below, you can replace `module` with
`ml`.

First, load all modules you want to include in the collections:

::: prompt
:::

Now store it in a collection using `module save`. In this example, the
collection is named `my-collection`.

::: prompt
:::

Later, for example in a jobscript or a new session, you can load all
these modules with `module restore`:

::: prompt
:::

You can get a list of all your saved collections with the
`module savelist` command:

::: prompt
Named collection list (For LMOD_SYSTEM_NAME = \"CO7-sandybridge\"): 1)
my-collection
:::

To get a list of all modules a collection will load, you can use the
`module describe` command:

::: prompt
1\) example/1.2.3 6) imkl/11.3.3.210-iimpi-2016b 2) GCCcore/5.4.0 7)
intel/2016b 3) icc/2016.3.210-GCC-5.4.0-2.26 8)
examplelib/1.2-intel-2016b 4) ifort/2016.3.210-GCC-5.4.0-2.26 9)
secondexample/2.7-intel-2016b 5)
impi/5.1.3.181-iccifort-2016.3.210-GCC-5.4.0-2.26
:::

To remove a collection, remove the corresponding file in
`$HOME/.lmod.d`:

::: prompt
:::

### Getting module details

To see how a module would change the environment, you can use the
`module show` command:

::: prompt
whatis(\"Description: Python is a programming language that lets you
work more quickly and integrate your systems more effectively. -
Homepage: http://python.org/ \") conflict(\"Python\")
load(\"intel/2016b\") load(\"bzip2/1.0.6-intel-2016b\") \...
prepend_path(\...)
setenv(\"EBEXTSLISTPYTHON\",\"setuptools-23.1.0,pip-8.1.2,nose-1.3.7,numpy-1.11.1,scipy-0.17.1,ytz-2016.4\",
\...)
:::

It's also possible to use the `ml show` command instead: they are
equivalent.

Here you can see that the `Python/2.7.12-intel-2016b` comes with a whole
bunch of extensions: `numpy`, `scipy`, ...

You can also see the modules the `Python/2.7.12-intel-2016b` module
loads: `intel/2016b`, `bzip2/1.0.6-intel-2016b`, ...

::: prompt
module-whatis Description: Python is a programming language that lets
you work more quickly and integrate your systems more effectively. -
Homepage: http://python.org/ conflict Python module load foss/2014a
module load bzip2/1.0.6-foss-2014a \... prepend-path \... \... setenv
EBVERSIONPYTHON 3.2.5 setenv EBEXTSLISTPYTHON
distribute-0.6.26,pip-1.1,nose-1.1.2,numpy-1.6.1,scipy-0.10.1
:::

Here you can see that the `Python/3.2.5-foss-2014a` comes with a whole
bunch of extensions: `numpy`, `scipy`, ...

You can also see the modules the `Python/3.2.5-foss-2014a` module loads:
`foss/2014a`, `bzip2/1.0.6-foss-2014a`, ... If you're not sure what all
of this means: don't worry, you don't have to know; just load the module
and try to use the software.

## Getting system information about the HPC infrastructure

### Checking the general status of the HPC infrastructure

To check the general system state, check
<https://www.ugent.be/hpc/en/infrastructure/status>. This has
information about scheduled downtime, status of the system, ...

Note: the `qstat -q` command now only shows *your own jobs* on the
infrastructure (since May 2019), and can't be used any longer to access
how "busy" each cluster is. For example:

::: prompt
Queue Memory CPU Time Walltime Node Run Que Lm State ----------------
------ -------- -------- ---- --- --- -- ----- victini -- -- 72:00:00 --
3 9 -- E R --- --- 3 9

Please be aware that \"qstat -q\" only gives information about your own
jobs.
:::

To check how much jobs are running in what queues, you can use the
`qstat -q` command:

::: prompt
Queue Memory CPU Time Walltime Node Run Que Lm State ----------------
------ -------- -------- ---- --- --- -- ----- default -- -- -- -- 0 0
-- E R q72h -- -- 72:00:00 -- 0 0 -- E R long -- -- 72:00:00 -- 316 77
-- E R short -- -- 11:59:59 -- 21 4 -- E R q1h -- -- 01:00:00 -- 0 1 --
E R q24h -- -- 24:00:00 -- 0 0 -- E R ----- ----- 337 82
:::

Here, there are 316 jobs running on the `long` queue, and 77 jobs
queued. We can also see that the `long` queue allows a maximum wall time
of 72 hours.

### Getting cluster state

You can check <http://hpc.ugent.be/clusterstate> to see information
about the clusters: you can see the nodes that are down, free, partially
filled with jobs, completely filled with jobs, ....

You can also get this information in text form (per cluster separately)
with the `pbsmon` command:

::: prompt
3401 3402 3403 3404 3405 3406 3407 J j j J J j J

3408 3409 3410 3411 3412 3413 3414 J J J J J J J

3415 3416 J J

\_ free : 0 \| X down : 0 \| j partial : 3 \| x down_on_error : 0 \| J
full : 13 \| m maintenance : 0 \| \| . offline : 0 \| \| o other (R, \*,
\...) : 0 \|

Node type: ppn=36, mem=751GB
:::

`pbsmon` only outputs details of the cluster corresponding to the
currently loaded `cluster` module (see ).

It also shows details about the nodes in a cluster. In the example, all
nodes have 36 cores and 751 GB of memory.

## Defining and submitting your job

::: { #sec:defining-and-submitting-job}
:::

Usually, you will want to have your program running in batch mode, as
opposed to interactively as you may be accustomed to. The point is that
the program must be able to start and run without user intervention,
i.e., without you having to enter any information or to press any
buttons during program execution. All the necessary input or required
options have to be specified on the command line, or needs to be put in
input or configuration files.

As an example, we will run a Perl script, which you will find in the
examples subdirectory on the . When you received an account to the a
subdirectory with examples was automatically generated for you.

Remember that you have copied the contents of the HPC examples directory
to your home directory, so that you have your copy (editable and
over-writable) and that you can start using the examples. If you haven't
done so already, run these commands now:

::: prompt
:::

First go to the directory with the first examples by entering the
command:

::: prompt
:::

Each time you want to execute a program on the you'll need 2 things:

The executable

:   The program to execute from the end-user, together with its
    peripheral input files, databases and/or command options.

A batch job script

:   , which will define the computer resource requirements of the
    program, the required additional software packages and which will
    start the actual executable. The needs to know:

    1.  the type of compute nodes;

    2.  the number of CPUs;

    3.  the amount of memory;

    4.  the expected duration of the execution time (wall time: Time as
        measured by a clock on the wall);

    5.  the name of the files which will contain the output (i.e.,
        stdout) and error (i.e., stderr) messages;

    6.  what executable to start, and its arguments.

Later on, the user shall have to define (or to adapt) his/her own job
scripts. For now, all required job scripts for the exercises are
provided for you in the examples subdirectories.

List and check the contents with:

::: prompt
total 512 -rw-r--r-- 1 -rw-r--r-- 1
:::

In this directory you find a Perl script (named "fibo.pl") and a job
script (named "fibo.pbs").

1.  The Perl script calculates the first 30 Fibonacci numbers.

2.  The job script is actually a standard Unix/Linux shell script that
    contains a few extra comments at the beginning that specify
    directives to PBS. These comments all begin with .

We will first execute the program locally (i.e., on your current
login-node), so that you can see what the program does.

On the command line, you would run this using:

::: prompt
\[0\] -\> 0 \[1\] -\> 1 \[2\] -\> 1 \[3\] -\> 2 \[4\] -\> 3 \[5\] -\> 5
\[6\] -\> 8 \[7\] -\> 13 \[8\] -\> 21 \[9\] -\> 34 \[10\] -\> 55 \[11\]
-\> 89 \[12\] -\> 144 \[13\] -\> 233 \[14\] -\> 377 \[15\] -\> 610
\[16\] -\> 987 \[17\] -\> 1597 \[18\] -\> 2584 \[19\] -\> 4181 \[20\]
-\> 6765 \[21\] -\> 10946 \[22\] -\> 17711 \[23\] -\> 28657 \[24\] -\>
46368 \[25\] -\> 75025 \[26\] -\> 121393 \[27\] -\> 196418 \[28\] -\>
317811 \[29\] -\> 514229
:::

: Recall that you have now executed the Perl script locally on one of
the login-nodes of the cluster. Of course, this is not our final
intention; we want to run the script on any of the compute nodes. Also,
it is not considered as good practice, if you "abuse" the login-nodes
for testing your scripts and executables. It will be explained later on
how you can reserve your own compute-node (by opening an interactive
session) to test your software. But for the sake of acquiring a good
understanding of what is happening, you are pardoned for this example
since these jobs require very little computing power.

The job script contains a description of the job by specifying the
command that need to be executed on the compute node:

So, jobs are submitted as scripts (bash, Perl, Python, etc.), which
specify the parameters related to the jobs such as expected runtime
(walltime), e-mail notification, etc. These parameters can also be
specified on the command line.

This job script that can now be submitted to the cluster's job system
for execution, using the qsub (Queue SUBmit) command:

::: prompt
:::

The qsub command returns a job identifier on the HPC cluster. The
important part is the number (e.g., ""); this is a unique identifier for
the job and can be used to monitor and manage your job.

: the modules that were loaded when you submitted the job will *not* be
loaded when the job is started. You should always specify the
`module load` statements that are required for your job in the job
script itself.

To faciliate this, you can use a pre-defined module collection which you
can restore using `module restore`, see
section [1.1.10](#sec:lmod-module-collection){reference-type="ref"
reference="sec:lmod-module-collection"} for more information.

Your job is now waiting in the queue for a free workernode to start on.

Go and drink some coffee ... but not too long. If you get impatient you
can start reading the next section for more information on how to
monitor jobs in the queue.

After your job was started, and ended, check the contents of the
directory:

::: prompt
total 768 -rw-r--r-- 1 -rw------- 1 -rw------- 1 -rwxrwxr-x 1
:::

Explore the contents of the 2 new files:

::: prompt
:::

These files are used to store the standard output and error that would
otherwise be shown in the terminal window. By default, they have the
same name as that of the PBS script, i.e., "fibo.pbs" as base name,
followed by the extension ".o" (output) and ".e" (error), respectively,
and the job number ('' for this example). The error file will be empty,
at least if all went well. If not, it may contain valuable information
to determine and remedy the problem that prevented a successful run. The
standard output file will contain the results of your calculation (here,
the output of the Perl script)

### When will my job start? { #subsec:priority}

In practice it's impossible to predict when your job(s) will start,
since most currently running jobs will finish before their requested
walltime expires, and new jobs by may be submitted by other users that
are assigned a higher priority than your job(s).

The clusters use a fair-share scheduling policy (see ). There is no
guarantee on when a job will start, since it depends on a number of
factors. One of these factors is the priority of the job, which is
determined by

-   historical use: the aim is to balance usage over users, so
    infrequent (in terms of total compute time used) users get a higher
    priority

-   requested resources (amount of cores, walltime, memory, ...)

-   time waiting in queue: queued jobs get a higher priority over time

-   user limits: this avoids having a single user use the entire
    cluster. This means that each user can only use a part of the
    cluster.

Some other factors are how busy the cluster is, how many workernodes are
active, the resources (e.g., number of cores, memory) provided by each
workernode, ...

It might be beneficial to request less resources (e.g., not requesting
all cores in a workernode), since the scheduler often finds a "gap" to
fit the job into more easily.

Sometimes it happens that couple of nodes are free and a job would not
start. Empty nodes are not necessary empty for your job(s). Just
imagine, that an *N*-node-job (with a higher priority than your waiting
job(s)) should run. It is quite unlikely that *N* nodes would be empty
at the same moment to accommodate this job, so while fewer than *N*
nodes are empty, you can see them as being empty. The moment the *N*th
node becomes empty the waiting *N*-node-job will consume these *N* free
nodes.

### Specifying the cluster on which to run { #subsec:specifying-the-cluster-on-which-to-run}

To use other clusters, you can swap the `cluster` module. This is a
special module that change what modules are available for you, and what
cluster your jobs will be queued in.

By default you are working on . To switch to, e.g., you need to redefine
the environment so you get access to all modules installed on the
cluster, and to be able to submit jobs to the scheduler so your jobs
will start on instead of the default cluster.

::: prompt
:::

Note: the modules may not work directly on the login nodes, because the
login nodes do not have the same architecture as the cluster, they have
the same architecture as the cluster however, so this is why by default
software works on the login nodes. See for why this is and how to fix
this.

To list the available cluster modules, you can use the
`module avail cluster/` command:

::: prompt
------------------------------------------------------------------------------------
/etc/modulefiles/vsc
------------------------------------------------------------------------------------
cluster/doduo (S) cluster/joltik (S) cluster/kirlia (S) cluster/skitty
(S) cluster/swalot (S) cluster/victini (S,L)

Where: S: Module is Sticky, requires --force to unload or purge L:
Module is loaded

If you need software that is not listed, request it via
https://www.ugent.be/hpc/en/support/software-installation-request
:::

As indicated in the output above, each `cluster` module is a so-called
sticky module, i.e., it will not be unloaded when `module purge` (see )
is used.

The output of the various commands interacting with jobs (`qsub`,
`stat`, ...) all depend on which `cluster` module is loaded.

## Monitoring and managing your job(s) { #sec:monitoring-and-managing-your-jobs}

Using the job ID that `qsub` returned, there are various ways to monitor
the status of your job. In the following commands, replace `12345` with
the job ID `qsub` returned.

::: prompt
:::

To show an estimated start time for your job (note that this may be very
inaccurate, the margin of error on this figure can be bigger then 100%
due to a sample in a population of 1.) This command is not available on
all systems.

::: prompt
:::

This is only a very rough estimate. Jobs may launch sooner than
estimated if other jobs end faster than estimated, but may also be
delayed if other higher-priority jobs enter the system.

To show the status, but also the resources required by the job, with
error messages that may prevent your job from starting:

::: prompt
:::

To show on which compute nodes your job is running, at least, when it is
running:

::: prompt
:::

To remove a job from the queue so that it will not run, or to stop a job
that is already running.

::: prompt
:::

When you have submitted several jobs (or you just forgot about the job
ID), you can retrieve the status of all your jobs that are submitted and
are not yet finished using:

::: prompt
Job ID Name User Time Use S Queue ----------- ------- --------- --------
- -----
:::

Here:

Job ID

:   the job's unique identifier

Name

:   the name of the job

User

:   the user that owns the job

Time Use

:   the elapsed walltime for the job

Queue

:   the queue the job is in

The state S can be any of the following:

  -- -----------------------------------------------------------------------------------------------
     The job is and is waiting to start.
     The job is currently .
     The job is currently after having run.
     The job is after having run.
     The job has a user or system on it and will not be eligible to run until the hold is removed.
  -- -----------------------------------------------------------------------------------------------

User hold means that the user can remove the hold. System hold means
that the system or an administrator has put the job on hold, very likely
because something is wrong with it. Check with your helpdesk to see why
this is the case.

## Examining the queue

There is currently (since May 2019) no way to get an overall view of the
state of the cluster queues for the infrastructure, due to changes to
the cluster resource management software (and also because a general
overview is mostly meaningless since it doesn't give any indication of
the resources requested by the queued jobs).

As we learned above, Moab is the software application that actually
decides when to run your job and what resources your job will run on.

For security reasons, it is not possible to see what other users are
doing on the clusters. As such, the PBS command only gives information
about your own jobs that are queued or running, ordered by .

However, you can get some idea of the load on the clusters by specifying
the option to the command:

::: prompt
server: master01.usr.hydra.brussel.vsc

Queue Memory CPU Time Walltime Node Run Que Lm State ----------------
------ -------- -------- ---- --- --- -- ----- ghostx10 -- -- 120:00:0 5
0 0 -- D S single_core 250gb -- 120:00:0 1 256 7 -- E R ghostx8 -- --
120:00:0 9 0 0 -- E R intel -- -- -- -- 0 0 -- D S mpi -- -- 120:00:0 --
3 5 -- E R smp 250gb -- 120:00:0 1 239 17 -- E R ghostx6 -- -- 120:00:0
2 0 0 -- E R ghostx1 -- -- 120:00:0 5 0 0 -- E R ghostx11 -- -- 120:00:0
-- 3 2 -- E R submission -- -- -- -- 0 24 -- E R login -- -- 120:00:0 --
0 0 -- D S gpu -- -- 120:00:0 -- 0 0 -- E R himem -- -- 120:00:0 1 0 0
-- E R ----- ----- 501 55
:::

In this example, 55 jobs are queued in the various queues whereas 501
jobs are effectively running.

You can look at the queue by using the PBS command or the Moab command.
By default, will display the queue ordered by , whereas will display
jobs grouped by their state ("running", "idle", or "hold") then ordered
by priority. Therefore, is often more useful. Note however that at some
VSC-sites, these commands show only your jobs or may be even disabled to
not reveal what other users are doing.

The command displays information about active ("running"), eligible
("idle"), blocked ("hold"), and/or recently completed jobs. To get a
summary:

::: prompt
active jobs: 163 eligible jobs: 133 blocked jobs: 243 Total jobs: 539
:::

And to get the full detail of all the jobs, which are in the system:

::: prompt
active jobs------------------------ JOBID USERNAME STATE PROCS REMAINING
STARTTIME 428024 vsc20167 Running 8 2:57:32 Mon Sep 2 14:55:05 153
active jobs 1307 of 3360 processors in use by local jobs (38.90 153 of
168 nodes active (91.07

eligible jobs---------------------- JOBID USERNAME STATE PROCS WCLIMIT
QUEUETIME 442604 vsc20167 Idle 48 7:00:00:00 Sun Sep 22 16:39:13 442605
vsc20167 Idle 48 7:00:00:00 Sun Sep 22 16:46:22

135 eligible jobs

blocked jobs----------------------- JOBID USERNAME STATE PROCS WCLIMIT
QUEUETIME 441237 vsc20167 Idle 8 3:00:00:00 Thu Sep 19 15:53:10 442536
vsc20167 UserHold 40 3:00:00:00 Sun Sep 22 00:14:22 252 blocked jobs
Total jobs: 540
:::

There are 3 categories, the , and jobs.

Active jobs

:   are jobs that are running or starting and that consume computer
    resources. The amount of time remaining (w.r.t. walltime, sorted to
    earliest completion time) and the start time are displayed. This
    will give you an idea about the foreseen completion time. These jobs
    could be in a number of states:

    Started

    :   attempting to start, performing pre-start tasks

    Running

    :   currently executing the user application

    Suspended

    :   has been suspended by scheduler or admin (still in place on the
        allocated resources, not executing)

    Cancelling

    :   has been cancelled, in process of cleaning up

Eligible jobs

:   are jobs that are waiting in the queues and are considered eligible
    for both scheduling and backfilling. They are all in the idle job
    state and do not violate any fairness policies or do not have any
    job holds in place. The requested walltime is displayed, and the
    list is ordered by job priority.

Blocked jobs

:   are jobs that are ineligible to be run or queued. These jobs could
    be in a number of states for the following reasons:

    Idle

    :   when the job violates a fairness policy

    Userhold

    :   or systemhold when it is user or administrative hold

    Batchhold

    :   when the requested resources are not available or the resource
        manager has repeatedly failed to start the job

    Deferred

    :   when a temporary hold when the job has been unable to start
        after a specified number of attempts

    Notqueued

    :   when scheduling daemon is unavailable

## Specifying job requirements

Without giving more information about your job upon submitting it with ,
default values will be assumed that are almost never appropriate for
real jobs.

It is important to estimate the resources you need to successfully run
your program, such as the amount of time the job will require, the
amount of memory it needs, the number of CPUs it will run on, etc. This
may take some work, but it is necessary to ensure your jobs will run
properly.

### Generic resource requirements { #subsec:generic-resource-requirements}

The command takes several options to specify the requirements, of which
we list the most commonly used ones below.\

::: prompt
:::

For the simplest cases, only the amount of maximum estimated execution
time (called "walltime") is really important. Here, the job requests 2
hours, 30 minutes. As soon as the job exceeds the requested walltime, it
will be "killed" (terminated) by the job scheduler. There is no harm if
you *slightly* overestimate the maximum execution time. If you omit this
option, the queue manager will not complain but use a default value (one
hour on most clusters).

The maximum walltime for HPC-UGent clusters is .

If you want to run some final steps (for example to copy files back)
before the walltime kills your main process, you have to kill the main
command yourself before the walltime runs out and then copy the file
back. See for how to do this.\

::: prompt
:::

The job requests 4 GB of RAM memory. As soon as the job tries to use
more memory, it will be "killed" (terminated) by the job scheduler.
There is no harm if you *slightly* overestimate the requested memory.

The default memory reserved for a job on any given HPC-UGent cluster is
the "usable memory per node" divided by the "numbers of cores in a node"
multiplied by the requested processor core(s) (ppn). Jobs will request
the default memory without defining memory for the job, either as a
command line option or as a memory directive in the job script. Please
note that using the default memory is recommended. For "usable memory
per node" and "number of cores in a node" please consult
<https://www.ugent.be/hpc/en/infrastructure>.

::: prompt
:::

The job requests 5 compute nodes with two cores on each node (ppn stands
for "processors per node", where \"processors\" here actually means
\"CPU cores\").\

::: prompt
:::

The job requests just one node, but it should have an Intel Westmere
processor. A list with site-specific properties can be found in the next
section or in the User Portal ("VSC hardware" section)[^1] of the VSC
website.

These options can either be specified on the command line, e.g.

::: prompt
:::

or in the job script itself using the #PBS-directive, so "fibo.pbs"
could be modified to:

Note that the resources requested on the command line will override
those specified in the PBS file.

### Node-specific properties

The following table contains some node-specific properties that can be
used to make sure the job will run on nodes with a specific CPU or
interconnect. Note that these properties may vary over the different VSC
sites.

  ------------ -----------------------------------------------------------------------------
  ivybridge    only use Intel processors from the Ivy Bridge family (26xx-v2, hopper-only)
  broadwell    only use Intel processors from the Broadwell family (26xx-v4, leibniz-only)
  mem128       only use nodes with 128GB of RAM (leibniz)
  mem256       only use nodes with 256GB of RAM (hopper and leibniz)
  tesla, gpu   only use nodes with the NVIDUA P100 GPU (leibniz)
  ------------ -----------------------------------------------------------------------------

Since both hopper and leibniz are homogeneous with respect to processor
architecture, the CPU architecture properties are not really needed and
only defined for compatibility with other VSC clusters.

  ------------ ---------------------------------------------------
  shanghai     only use AMD Shanghai processors (AMD 2378)
  magnycours   only use AMD Magnycours processors (AMD 6134)
  interlagos   only use AMD Interlagos processors (AMD 6272)
  barcelona    only use AMD Shanghai and Magnycours processors
  amd          only use AMD processors
  ivybridge    only use Intel Ivy Bridge processors (E5-2680-v2)
  intel        only use Intel processors
  gpgpu        only use nodes with General Purpose GPUs (GPGPUs)
  k20x         only use nodes with NVIDIA Tesla K20x GPGPUs
  xeonphi      only use nodes with Xeon Phi co-processors
  phi5110p     only use nodes with Xeon Phi 5110P co-processors
  ------------ ---------------------------------------------------

To get a list of all properties defined for all nodes, enter

::: prompt
:::

This list will also contain properties referring to, e.g., network
components, rack number, etc.

## Job output and error files

At some point your job finishes, so you may no longer see the job ID in
the list of jobs when you run *qstat* (since it will only be listed for
a few minutes after completion with state "C"). After your job finishes,
you should see the standard output and error of your job in two files,
located by default in the directory where you issued the *qsub* command.

When you navigate to that directory and list its contents, you should
see them:

::: prompt
total 1024 -rw-r--r-- 1 -rw-r--r-- 1 -rw------- 1 -rw------- 1
:::

In our case, our job has created both output ('fibo.pbs.') and error
files ('fibo.pbs.') containing info written to *stdout* and *stderr*
respectively.

Inspect the generated output and error files:

::: prompt
:::

## E-mail notifications

### Upon job failure

Whenever a job fails, an e-mail will be sent to the e-mail address
that's connected to your VSC account. This is the e-mail address that is
linked to the university account, which was used during the registration
process.

You can force a job to fail by specifying an unrealistic wall-time for
the previous example. Lets give the "*fibo.pbs*" job just one second to
complete:

::: prompt
:::

Now, lets hope that the did not manage to run the job within one second,
and you will get an e-mail informing you about this error.

::: flattext
PBS Job Id: Job Name: fibo.pbs Exec host: Aborted by PBS Server Job
exceeded some resource limit (walltime, mem, etc.). Job was aborted. See
Administrator for help
:::

### Generate your own e-mail notifications

You can instruct the to send an e-mail to your e-mail address whenever a
job egins, nds and/or borts, by adding the following lines to the job
script `fibo.pbs`:

::: code
bash #PBS -m b #PBS -m e #PBS -m a
:::

or

::: code
bash #PBS -m abe
:::

These options can also be specified on the command line. Try it and see
what happens:

::: prompt
:::

The system will use the e-mail address that is connected to your VSC
account. You can also specify an alternate e-mail address with the `-M`
option:

::: prompt
:::

will send an e-mail to john.smith\@example.com when the job begins.

## Running a job after another job

If you submit two jobs expecting that should be run one after another
(for example because the first generates a file the second needs), there
might be a problem as they might both be run at the same time.

So the following example might go wrong:

::: prompt
:::

You can make jobs that depend on other jobs. This can be useful for
breaking up large jobs into smaller jobs that can be run in a pipeline.
The following example will submit 2 jobs, but the second job (`job2.sh`)
will be held (`H` status in `qstat`) until the first job successfully
completes. If the first job fails, the second will be cancelled.

::: prompt
:::

`afterok` means "After OK", or in other words, after the first job
successfully completed.

It's also possible to use `afternotok` ("After not OK") to run the
second job only if the first job exited with errors. A third option is
to use `afterany` ("After any"), to run the second job after the first
job (regardless of success or failure).

[^1]: URL:
    <https://vscdocumentation.readthedocs.io/en/latest/hardware.html>
