# HPC-UGent GPU clusters {#ch:gpu_ugent}

## Submitting jobs {#sec:gpu_ugent_jobs}

To submit jobs to the `joltik` GPU cluster, where each node provides 4
NVIDIA V100 GPUs (each with 32GB of GPU memory), use:

::: prompt
:::

To submit to the `accelgor` GPU cluster, where each node provides 4
NVIDIA A100 GPUs (each with 80GB GPU memory), use:

::: prompt
:::

Then use the familiar `qsub`, `qstat`, etc. commands, taking into
account the guidelines outlined in
section [1.3](#sec:gpu_ugent_resources){reference-type="ref"
reference="sec:gpu_ugent_resources"}.

### Interactive jobs {#sec:gpu_ugent_interactive_jobs}

To interactively experiment with GPUs, you can submit an interactive job
using `qsub -I` (and request one or more GPUs, see
section [1.3](#sec:gpu_ugent_resources){reference-type="ref"
reference="sec:gpu_ugent_resources"}).

Note that due to a bug in Slurm you will currently not be able to be
able to interactively use MPI software that requires access to the GPUs.
If you need this, please contact use via .

## Hardware

See <https://www.ugent.be/hpc/en/infrastructure>.

## Requesting (GPU) resources {#sec:gpu_ugent_resources}

There are 2 main ways to ask for GPUs as part of a job:

-   Either as a node property (similar to the number of cores per node
    specified via `ppn`) using `-l nodes=X:ppn=Y:gpus=Z` (where the
    `ppn=Y` is optional), or as a separate resource request (similar to
    the amount of memory) via `-l gpus=Z`. Both notations give exactly
    the same result. The `-l gpus=Z` is convenient is you only need one
    node and you are fine with the default number of cores per GPU. The
    `-l nodes=...:gpus=Z` notation is required if you want to run with
    full control or in multinode cases like MPI jobs. If you do not
    specify the number of GPUs by just using `-l gpus`, you get by
    default 1 GPU.

-   As a resource of it's own, via `--gpus X`. In this case however, you
    are *not* guaranteed that the GPUs are on the same node, so your
    script or code must be able to deal with this.

Some background:

-   The GPUs are constrained to the jobs (like the CPU cores), but do
    not run in so-called "exclusive" mode.

-   The GPUs run with the so-called "persistence daemon", so the GPUs is
    not re-initialised between jobs.

## Attention points {#sec:gpu_ugent_attention_points}

Some important attention points:

-   For MPI jobs, we recommend the (new) wrapper `mypmirun` from the
    `vsc-mympirun` module (`pmi` is the background mechanism to start
    the MPI tasks, and is different from the usual `mpirun` that is used
    by the `mympirun` wrapper). At some later point, we *might* promote
    the `mypmirun` tool or rename it, to avoid the confusion in the
    naming).

-   Sharing GPUs requires MPS. The Slurm built-in MPS does not really do
    want you want, so we will provide integration with `mypmirun` and
    `wurker`.

-   For parallel work, we are working on a `wurker` wrapper from the
    `vsc-mympirun` module that supports GPU placement and MPS, without
    any limitations wrt the requested resources (i.e. also support the
    case where GPUs are spread heterogenous over nodes from using the
    `--gpus Z` option).

-   Both `mypmirun` and `wurker` will try to do the most optimised
    placement of cores and tasks, and will provide 1 (optimal) GPU per
    task/MPI rank, and set one so-called *visible device* (i.e.
    `CUDA_VISIBLE_DEVICES` only has 1 ID). The actual devices are not
    constrained to the ranks, so you can access all devices requested in
    the job. *We know that at this moment, this is not working properly,
    but we are working on this. We advise against trying to fix this
    yourself.*

## Software with GPU support {#sec:gpu_ugent_software}

Use `module avail` to check for centrally installed software.

The subsections below only cover a couple of installed software
packages, more are available.

### GROMACS {#sec:gpu_ugent_software_gromacs}

Please consult `module avail GROMACS` for a list of installed versions.

### Horovod {#sec:gpu_ugent_software_horovod}

Horovod can be used for (multi-node) multi-GPU TensorFlow/PyTorch
calculations.

Please consult `module avail Horovod` for a list of installed versions.

Horovod supports TensorFlow, Keras, PyTorch and MxNet (see
<https://github.com/horovod/horovod#id9>), but should be run as an MPI
application with `mypmirun`. (Horovod also provides it's own wrapper
`horovodrun`, not sure if it handles placement and others correctly).

At least for simple TensorFlow benchmarks, it looks like Horovod is a
bit faster than usual autodetect multi-GPU TensorFlow without horovod,
but it comes at the cost of the code modifications to use horovod.

### PyTorch {#sec:gpu_ugent_software_pytorch}

Please consult `module avail PyTorch` for a list of installed versions.

### TensorFlow {#sec:gpu_ugent_software_tensorflow}

Please consult `module avail TensorFlow` for a list of installed
versions.

#### Example TensorFlow job script {#sec:gpu_ugent_software_tensorflow_example_job_script}

### AlphaFold {#sec:gpu_ugent_software_alphafold}

Please consult `module avail AlphaFold` for a list of installed
versions.

For more information on using AlphaFold, we strongly recommend the
VIB-UGent course available at
<https://elearning.bits.vib.be/courses/alphafold>.

## Getting help {#sec:gpu_ugent_help}

In case of questions or problems, please contact the via , and clearly
indicate that your question relates to the `joltik` cluster by adding
`[joltik]` in the email subject.
