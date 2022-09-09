# HPC Quick Reference Guide { #ch:quick-reference-guide}

Remember to substitute the usernames, login nodes, file names, ...for
your own.

  ------------------- -------------------
  Login               `ssh @`
  Where am I?         `hostname`
  Copy to             `scp foo.txt @:`
  Copy from           `scp @:foo.txt .`
  Setup ftp session   `sftp @`
  ------------------- -------------------

  ---------------------------- -------------------------
  List all available modules   `module avail`
  List loaded modules          `module list`
  Load module                  `module load example`
  Unload module                `module unload example`
  Unload all modules           `module purge`
  Help on use of module        `module help`
  ---------------------------- -------------------------

  --------------------------------------------------------------------- -------------------
  Submit job with job script `script.pbs`                               `qsub script.pbs`
  Status of job with ID 12345                                           `qstat 12345`
  Possible start time of job with ID 12345 (not available everywhere)   `showstart 12345`
  Check job with ID 12345 (not available everywhere)                    `checkjob 12345`
  Show compute node of job with ID 12345                                `qstat -n 12345`
  Delete job with ID 12345                                              `qdel 12345`
  Status of all your jobs                                               `qstat`
  Detailed status of your jobs + a list nodes they are running on       `qstat -na`
  Show all jobs on queue (not available everywhere)                     `showq`
  Submit Interactive job                                                `qsub -I`
  --------------------------------------------------------------------- -------------------

  --------------------------------------- ------------------------------------
  Check your disk quota                   See <https://account.vscentrum.be>
  Check your disk quota                   `mmlsquota`
  Check disk quota nice                   `show_quota.py`
  Disk usage in current directory (`.`)   `du -h` .
  --------------------------------------- ------------------------------------

  ----------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------
  Load worker module                        `module load worker/1.6.8-intel-2018a` Don't forget to specify a version. To list available versions, use `module avail worker/`
  Submit parameter sweep                    `wsub -batch weather.pbs -data data.csv`
  Submit job array                          `wsub -t 1-100 -batch test_set.pbs`
  Submit job array with prolog and epilog   `wsub -prolog pre.sh -batch test_set.pbs -epilog post.sh -t 1-100`
  ----------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------
