# TORQUE options {#ch:torque-options}

## TORQUE Submission Flags: common and useful directives

Below is a list of the most common and useful directives.

  ---------- -------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  -k         All            Send "stdout" and/or "stderr" to your home directory when the job runs or or
  -l         All            Precedes a resource request, e.g., processors, wallclock
  -M         All            Send an e-mail messages to an alternative e-mail address
  -m         All            Send an e-mail address when a job egins execution and/or nds or borts or or
  mem        SharedMemory   Specifies the amount of memory you need for a job.
  mpiprocs   Clusters       Number of processes per node on a cluster. This should equal number of processors on a node in most cases.
  -N         All            Give your job a unique name
  -ncpus     SharedMemory   The number of processors to use for a shared memory job.
  -r         All            Control whether or not jobs should automatically re-run from the start if the system crashes or is rebooted. Users with check points might not wish this to happen.
  select     Clusters       Number of compute nodes to use. Usually combined with the mpiprocs directive
  -V         All            Make sure that the environment in which the job is the same as the environment in which it was
  Walltime   All            The maximum time a job can run before being stopped. If not used a default of a few minutes is used. Use this flag to prevent jobs that go bad running for hundreds of hours. Format is HH:MM:SS
  ---------- -------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Environment Variables in Batch Job Scripts

TORQUE-related environment variables in batch job scripts.

::: code
bash \# Using PBS - Environment Variables: \# When a batch job starts
execution, a number of environment variables are \# predefined, which
include: \# \# Variables defined on the execution host. \# Variables
exported from the submission host with \# -v (selected variables) and -V
(all variables). \# Variables defined by PBS. \# \# The following
reflect the environment where the user ran qsub: \# PBS_O\_HOST The host
where you ran the qsub command. \# PBS_O\_LOGNAME Your user ID where you
ran qsub. \# PBS_O\_HOME Your home directory where you ran qsub. \#
PBS_O\_WORKDIR The working directory where you ran qsub. \# \# These
reflect the environment where the job is executing: \# PBS_ENVIRONMENT
Set to PBS_BATCH to indicate the job is a batch job, \# or to
PBS_INTERACTIVE to indicate the job is a PBS interactive job. \#
PBS_O\_QUEUE The original queue you submitted to. \# PBS_QUEUE The queue
the job is executing from. \# PBS_JOBID The job's PBS identifier. \#
PBS_JOBNAME The job's name.
:::

All PBS directives MUST come before the first line of executable code in
your script, otherwise they will be ignored.

When a batch job is started, a number of environment variables are
created that can be used in the batch job script. A few of the most
commonly used variables are described here.

  ----------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  PBS_ENVIRONMENT   set to PBS_BATCH to indicate that the job is a batch job; otherwise, set to PBS_INTERACTIVE to indicate that the job is a PBS interactive job.
  PBS_JOBID         the job identifier assigned to the job by the batch system. This is the same number you see when you do *qstat*.
  PBS_JOBNAME       the job name supplied by the user
  PBS_NODEFILE      the name of the file that contains the list of the nodes assigned to the job . Useful for Parallel jobs if you want to refer the node, count the node etc.
  PBS_QUEUE         the name of the queue from which the job is executed
  PBS_O\_HOME       value of the HOME variable in the environment in which *qsub* was executed
  PBS_O\_LANG       value of the LANG variable in the environment in which *qsub* was executed
  PBS_O\_LOGNAME    value of the LOGNAME variable in the environment in which *qsub* was executed
  PBS_O\_PATH       value of the PATH variable in the environment in which *qsub* was executed
  PBS_O\_MAIL       value of the MAIL variable in the environment in which *qsub* was executed
  PBS_O\_SHELL      value of the SHELL variable in the environment in which *qsub* was executed
  PBS_O\_TZ         value of the TZ variable in the environment in which *qsub* was executed
  PBS_O\_HOST       the name of the host upon which the *qsub* command is running
  PBS_O\_QUEUE      the name of the original queue to which the job was submitted
  PBS_O\_WORKDIR    the absolute path of the current working directory of the *qsub* command. This is the most useful. Use it in every job script. The first thing you do is, cd \$PBS_O\_WORKDIR after defining the resource list. This is because, pbs throw you to your \$HOME directory.
  PBS_VERSION       Version Number of TORQUE, e.g., TORQUE-2.5.1
  PBS_MOMPORT       active port for mom daemon
  PBS_TASKNUM       number of tasks requested
  PBS_JOBCOOKIE     job cookie
  PBS_SERVER        Server Running TORQUE
  ----------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
