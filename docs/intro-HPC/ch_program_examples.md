# Program examples {#ch:program-examples}

Go to our examples:

::: prompt
:::

Here, we just have put together a number of examples for your
convenience. We did an effort to put comments inside the source files,
so the source code files are (should be) self-explanatory.

1.  01_Python

2.  02_C\_C++

3.  03_Matlab

4.  04_MPI_C

5.  05a_OMP_C

6.  05b_OMP_FORTRAN

7.  06_NWChem

8.  07_Wien2k

9.  08_Gaussian

10. 09_Fortran

11. 10_PQS

The above 2 OMP directories contain the following examples:

  **C Files**                                                                                                 **Fortran Files**                                                                                           **Description**
  ----------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------- ---------------------------------------
  omp_hello.c                                                                                                 omp_hello.f                                                                                                 Hello world
  omp_workshare1.c                                                                                            omp_workshare1.f                                                                                            Loop work-sharing
  omp_workshare2.c                                                                                            omp_workshare2.f                                                                                            Sections work-sharing
  omp_reduction.c                                                                                             omp_reduction.f                                                                                             Combined parallel loop reduction
  omp_orphan.c                                                                                                omp_orphan.f                                                                                                Orphaned parallel loop reduction
  omp_mm.c                                                                                                    omp_mm.f                                                                                                    Matrix multiply
  omp_getEnvInfo.c                                                                                            omp_getEnvInfo.f                                                                                            Get and print environment information
  omp_bug1.c omp_bug1fix.c omp_bug2.c omp_bug3.c omp_bug4.c omp_bug4fix omp_bug5.c omp_bug5fix.c omp_bug6.c   omp_bug1.f omp_bug1fix.f omp_bug2.f omp_bug3.f omp_bug4.f omp_bug4fix omp_bug5.f omp_bug5fix.f omp_bug6.f   Programs with bugs and their solution

Compile by any of the following commands:

  **C:**         icc -openmp omp_hello.c -o hellopgcc -mp omp_hello.c -o hellogcc -fopenmp omp_hello.c -o hello
  -------------- --------------------------------------------------------------------------------------------------------
  **Fortran:**   ifort -openmp omp_hello.f -o hellopgf90 -mp omp_hello.f -o hellogfortran -fopenmp omp_hello.f -o hello

Be invited to explore the examples.
