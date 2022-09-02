# Compiling and testing your software on the HPC {#ch:compiling-and-testing-your-software-on-the-hpc}

All nodes in the cluster are running the "" Operating system, which is a
specific version of . This means that all the software programs
(executable) that the end-user wants to run on the first must be
compiled for . It also means that you first have to install all the
required external software packages on the .

Most commonly used compilers are already pre-installed on the and can be
used straight away. Also many popular external software packages, which
are regularly used in the scientific community, are also pre-installed.

## Check the pre-installed software on the 

In order to check all the available modules and their version numbers,
which are pre-installed on the enter:

When your required application is not available on the please contact
any member. Be aware of potential "License Costs". "Open Source"
software is often preferred.

## Porting your code

To a software-program is to translate it from the operating system in
which it was developed (e.g., Windows 7) to another operating system
(e.g., on our ) so that it can be used there. Porting implies some
degree of effort, but not nearly as much as redeveloping the program in
the new environment. It all depends on how "portable" you wrote your
code.

In the simplest case the file or files may simply be copied from one
machine to the other. However, in many cases the software is installed
on a computer in a way, which depends upon its detailed hardware,
software, and setup, with device drivers for particular devices, using
installed operating system and supporting software components, and using
different directories.

In some cases software, usually described as "portable software" is
specifically designed to run on different computers with compatible
operating systems and processors without any machine-dependent
installation; it is sufficient to transfer specified directories and
their contents. Hardware- and software-specific information is often
stored in configuration files in specified locations (e.g., the registry
on machines running MS Windows).

Software, which is not portable in this sense, will have to be
transferred with modifications to support the environment on the
destination machine.

Whilst programming, it would be wise to stick to certain standards
(e.g., ISO/ANSI/POSIX). This will ease the porting of your code to other
platforms.

Porting your code to the platform is the responsibility of the end-user.

## Compiling and building on the 

Compiling refers to the process of translating code written in some
programming language, e.g., Fortran, C, or C++, to machine code.
Building is similar, but includes gluing together the machine code
resulting from different source files into an executable (or library).
The text below guides you through some basic problems typical for small
software projects. For larger projects it is more appropriate to use
makefiles or even an advanced build system like CMake.

All the nodes run the same version of the Operating System, i.e. . So,
it is sufficient to compile your program on any compute node. Once you
have generated an executable with your compiler, this executable should
be able to run on any other compute-node.

A typical process looks like:

1.  Copy your software to the login-node of the

2.  Start an interactive session on a compute node;

3.  Compile it;

4.  Test it locally;

5.  Generate your job scripts;

6.  Test it on the

7.  Run it (in parallel);

We assume you've copied your software to the The next step is to request
your private compute node.

::: prompt
qsub: waiting for job
:::

### Compiling a sequential program in C

Go to the examples for and load the foss module:

::: prompt
:::

We now list the directory and explore the contents of the "*hello.c*"
program:

::: prompt
total 512 -rw-r--r-- 1 -rw-r--r-- 1 -rw-r--r-- 1 -rw-r--r-- 1
:::

The "hello.c" program is a simple source file, written in C. It'll print
500 times "Hello #\<num>", and waits one second between 2 printouts.

We first need to compile this C-file into an executable with the
gcc-compiler.

First, check the command line options for *"gcc" (GNU C-Compiler)*, then
we compile and list the contents of the directory again:

::: prompt
total 512 -rwxrwxr-x 1 -rw-r--r-- 1 -rwxr-xr-x 1
:::

A new file "hello" has been created. Note that this file has "execute"
rights, i.e., it is an executable. More often than not, calling gcc --
or any other compiler for that matter -- will provide you with a list of
errors and warnings referring to mistakes the programmer made, such as
typos, syntax errors. You will have to correct them first in order to
make the code compile. Warnings pinpoint less crucial issues that may
relate to performance problems, using unsafe or obsolete language
features, etc. It is good practice to remove all warnings from a
compilation process, even if they seem unimportant so that a code change
that produces a warning does not go unnoticed.

Let's test this program on the local compute node, which is at your
disposal after the "qsub --I" command:

It seems to work, now run it on the

::: prompt
:::

### Compiling a parallel program in C/MPI

::: prompt
:::

List the directory and explore the contents of the "*mpihello.c*"
program:

::: prompt
total 512 total 512 -rw-r--r-- 1 -rw-r--r-- 1 -rw-r--r-- 1 -rw-r--r-- 1
:::

The "mpi_hello.c" program is a simple source file, written in C with MPI
library calls.

Then, check the command line options for *"mpicc" (GNU C-Compiler with
MPI extensions)*, then we compile and list the contents of the directory
again:

::: prompt
:::

A new file "hello" has been created. Note that this program has
"execute" rights.

Let's test this program on the "login" node first:

::: prompt
Hello World from Node 0.
:::

It seems to work, now run it on the .

::: prompt
:::

### Compiling a parallel program in Intel Parallel Studio Cluster Edition

We will now compile the same program, but using the Intel Parallel
Studio Cluster Edition compilers. We stay in the examples directory for
this chapter:

::: prompt
:::

We will compile this C/MPI -file into an executable with the Intel
Parallel Studio Cluster Edition. First, clear the modules (purge) and
then load the latest "intel" module:

::: prompt
:::

Then, compile and list the contents of the directory again. The Intel
equivalent of mpicc is mpiicc.

::: prompt
:::

Note that the old "mpihello" file has been overwritten. Let's test this
program on the "login" node first:

::: prompt
Hello World from Node 0.
:::

It seems to work, now run it on the .

::: prompt
:::

Note: The only has a license for the Intel Parallel Studio Cluster
Edition for a fixed number of users. As such, it might happen that you
have to wait a few minutes before a floating license becomes available
for your use.

Note: The Intel Parallel Studio Cluster Edition contains equivalent
compilers for all GNU compilers. Hereafter the overview for C, C++ and
Fortran compilers.

::: tabular
\|p0.15\|p0.15\|p0.15\|p0.15\|p0.15\| & &\
& & & &\
& gcc & icc & mpicc & mpiicc\
& g++ & icpc & mpicxx & mpiicpc\
& gfortran & ifort & mpif90 & mpiifort\
:::
