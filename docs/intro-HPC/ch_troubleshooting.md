# Troubleshooting { #ch:troubleshooting}

## Walltime issues

If you get from your job output an error message similar to this:

::: prompt
=>\> PBS: job killed: walltime
:::

This occurs when your job did not complete within the requested
walltime. See
section [\[sec:specifying-walltime-requirements\]](#sec:specifying-walltime-requirements){reference-type="ref"
reference="sec:specifying-walltime-requirements"} for more information
about how to request the walltime. It is recommended to use
*checkpointing* if the job requires of walltime or more to be executed.

## Out of quota issues

Sometimes a job hangs at some point or it stops writing in the disk.
These errors are usually related to the quota usage. You may have
reached your quota limit at some storage endpoint. You should move (or
remove) the data to a different storage endpoint (or request more quota)
to be able to write to the disk and then resubmit the jobs. Another
option is to request extra quota for your VO to the VO moderator/s. See
section [\[subsec:predefined-user-directories\]](#subsec:predefined-user-directories){reference-type="ref"
reference="subsec:predefined-user-directories"} and
section [\[subsec:predfined-quotas\]](#subsec:predfined-quotas){reference-type="ref"
reference="subsec:predfined-quotas"} for more information about quotas
and how to use the storage endpoints in an efficient way.

## Issues connecting to login node { #sec:connecting-issues}

If you are confused about the SSH public/private key pair concept, maybe
the key/lock analogy in can help.

If you have errors that look like:

::: prompt
:::

or you are experiencing problems with connecting, here is a list of
things to do that should help:

1.  Keep in mind that it an take up to an hour for your VSC account to
    become active after it has been *approved*; until then, logging in
    to your VSC account will not work.

2.  Make sure you are connecting from an IP address that is allowed to
    access the VSC login nodes, see
    section [\[sec:connection-restrictions\]](#sec:connection-restrictions){reference-type="ref"
    reference="sec:connection-restrictions"} for more information.

3.  Your SSH private key may not be in the default location
    (`$HOME/.ssh/id_rsa`). There are several ways to deal with this
    (using one of these is sufficient):

4.  Please double/triple check your VSC login ID. It should look
    something like : the letters `vsc`, followed by exactly 5 digits.
    Make sure it's the same one as the one on
    <https://account.vscentrum.be/>.

5.  You previously connected to the from another machine, but now have
    another machine? Please follow the procedure for adding additional
    keys in
    section [\[sec:adding-multiple-keys\]](#sec:adding-multiple-keys){reference-type="ref"
    reference="sec:adding-multiple-keys"}. You may need to wait for
    15-20 minutes until the SSH public key(s) you added become active.

6.  Make sure you are using the private key (not the public key) when
    trying to connect: If you followed the manual, the private key
    filename should end in `.ppk` (not in `.pub`). When using an SSH key
    in a non-default location, make sure you supply the path of the
    private key (and not the path of the public key) to `ssh`.
    `id_rsa.pub` is the usual filename of the public key, `id_rsa` is
    the usual filename of the private key. (See also
    section [\[sec:connect\]](#sec:connect){reference-type="ref"
    reference="sec:connect"})

7.  If you have multiple private keys on your machine, please make sure
    you are using the one that corresponds to (one of) the public key(s)
    you added on <https://account.vscentrum.be/>.

8.  Please do not use someone else's private keys. You must never share
    your private key, they're called *private* for a good reason.

If you are using PuTTY and get this error message:

::: prompt
server unexpectedly closed network connection
:::

it is possible that the PuTTY version you are using is too old and
doesn't support some required (security-related) features.

Make sure you are using the latest PuTTY version if you are encountering
problems connecting (see ). If that doesn't help, please contact .

If you've tried all applicable items above and it doesn't solve your
problem, please contact and include the following information:

Please create a log file of your SSH session by following the steps in
[this article](https://my.kualo.com/knowledgebase/?kbcat=0&article=888)
and include it in the email.

### Change PuTTY private key for a saved configuration { #subsec:putty-change-key}

1.  Open PuTTY

2.  Single click on the saved configuration

    ::: center
    ![image](831change01){width="2.49in"}
    :::

3.  Then click button

    ::: center
    ![image](831change02){width="2.49in"}
    :::

4.  Expand SSH category (on the left panel) clicking on the \"+\" next
    to SSH

    ::: center
    ![image](831change03){width="2.49in"}
    :::

5.  [\[item:putty-auth-ssh\]]{ #item:putty-auth-ssh
    label="item:putty-auth-ssh"} Click on Auth under the SSH category

    ::: center
    ![image](831change04){width="2.49in"}
    :::

6.  On the right panel, click button

    ::: center
    ![image](831change05){width="2.49in"}
    :::

7.  Then search your private key on your computer (with the extension
    ".ppk")

8.  Go back to the top of category, and click Session

    ::: center
    ![image](831change06){width="2.49in"}
    :::

9.  On the right panel, click on button

    ::: center
    ![image](831change07){width="2.49in"}
    :::

### Check whether your private key in PuTTY matches the public key on the accountpage

Follow the instructions in util item , then:

1.  Single click on the textbox containig the path to your private key,
    then select all text (push + ), then copy the location of the
    private key (push + )

    ::: center
    ![image](832check05){width="2.49in"}
    :::

2.  Open PuTTYgen

    ::: center
    ![image](832check06){width="2.49in"}
    :::

3.  Enter menu item \"File\" and select \"Load Private key\"

    ::: center
    ![image](832check07){width="2.49in"}
    :::

4.  On the \"Load private key\" popup, click in the textbox next to
    \"File name:\", then paste the location of your private key (push +
    ), then click

    ::: center
    ![image](832check08){width="5.21in"}
    :::

5.  Make sure that your Public key from the \"Public key for pasting
    into OpenSSH authorized_keys file\" textbox is in your \"Public
    keys\" section on the accountpage <https://account.vscentrum.be>.
    (Scroll down to the bottom of \"View Account\" tab, you will find
    there the \"Public keys\" section)

    ::: center
    ![image](832check09){width="2.49in"}
    :::

Please add `-vvv` as a flag to `ssh` like:

::: prompt
:::

and include the output of that command in the message.

## Security warning about invalid host key { #sec:security-warning-invald-host-key}

If you get a warning that looks like the one below, it is possible that
someone is trying to intercept the connection between you and the system
you are connecting to. Another possibility is that the host key of the
system you are connecting to has changed.

::: prompt
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @ WARNING:
REMOTE HOST IDENTIFICATION HAS CHANGED! @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ IT IS
POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY! Someone could be
eavesdropping on you right now (man-in-the-middle attack)! It is also
possible that a host key has just been changed. The fingerprint for the
ECDSA key sent by the remote host is
SHA256:1MNKFTfl1T9sm6tTWAo4sn7zyEfiWFLKbk/mlT+7S5s. Please contact your
system administrator. Add correct host key in  /.ssh/known_hosts to get
rid of this message. Offending ECDSA key in  /.ssh/known_hosts: ECDSA
host key for Host key verification failed.
:::

You will need to remove the line it's complaining about (in the example,
line 21). To do that, open `~/.ssh/config` in an editor, and remove the
line. This results in `ssh` "forgetting" the system you are connecting
to.

After you've done that, you'll need to connect to the again. See to
verify the fingerprints.

You will need to verify that the fingerprint shown in the dialog matches
one of the following fingerprints:

.

If it the fingerprint matches, click "Yes".

If it doesn't (like in the example) or you are in doubt, take a
screenshot, press "Cancel" and contact .

![image](putty_security_alert){width="50%"}

## DOS/Windows text format

If you get errors like:

::: prompt
qsub: script is written in DOS/Windows text format
:::

It's probably because you transferred the files from a Windows computer.
Please go to the section about `dos2unix` in [chapter 5 of the intro to
Linux](\LinuxManualURL#sec:dos2unix) to fix this error.

## Warning message when first connecting to new host { #sec:warning-message-new-host}

::: prompt
The authenticity of host Are you sure you want to continue connecting
(yes/no)?
:::

Now you can check the authenticity by checking if the line that is at
the place of the underlined piece of text matches one of the following
lines:

::: prompt
:::

If it does, type . If it doesn't, please contact support: .

## Memory limits

To avoid jobs allocating too much memory, there are memory limits in
place by default. It is possible to specify higher memory limits if your
jobs require this.

### How will I know if memory limits are the cause of my problem?

If your program fails with a memory-related issue, there is a good
chance it failed because of the memory limits and you should increase
the memory limits for your job.

Examples of these error messages are: `malloc failed`, `Out of memory`,
`Could not allocate memory` or in Java:
`Could not reserve enough space for object heap`. Your program can also
run into a `Segmentation fault` (or `segfault`) or crash due to bus
errors.

You can check the amount of virtual memory (in Kb) that is available to
you via the `ulimit -v` command *in your job script*.

### How do I specify the amount of memory I need?

See to set memory and other requirements, see to finetune the amount of
memory you request.

## Module conflicts { #sec:module-conflicts}

Modules that are loaded together must use the same toolchain version: it
is impossible to load two versions of the same module. In the following
example, we try to load a module that uses the `intel-2018a` toolchain
together with one that uses the `intel-2017a` toolchain:

::: prompt
Lmod has detected the following error: A different version of the
'intel' module is already loaded (see output of 'ml'). You should load
another 'HMMER' module for that is compatible with the currently loaded
version of 'intel'. Use 'ml avail HMMER' to get an overview of the
available versions.

If you don't understand the warning or error, contact the helpdesk at
hpc\@ugent.be While processing the following module(s):

Module fullname Module Filename --------------- ---------------
HMMER/3.1b2-intel-2017a
/apps/gent/CO7/haswell-ib/modules/all/HMMER/3.1b2-intel-2017a.lua
:::

This resulted in an error because we tried to load two different
versions of the `intel` module.

To fix this, check if there are other versions of the modules you want
to load that have the same version of common dependencies. You can list
all versions of a module with `module avail`: for `HMMER`, this command
is `module avail HMMER`.

Another common error is:

::: prompt
Lmod has detected the following error: A different version of the
'cluster' module is already loaded (see output of 'ml').

If you don't understand the warning or error, contact the helpdesk at
hpc\@ugent.be
:::

This is because there can only be one `cluster` module active at a time.
The correct command is `module swap cluster/`. See also .

## Running software that is incompatible with host { #sec:running-software-incompatible-with-host}

When running software provided through modules (see ), you may run into
errors like:

::: prompt
The following have been reloaded with a version change: 1)
cluster/victini => cluster/kirlia

Please verify that both the operating system and the processor support
Intel(R) MOVBE, F16C, FMA, BMI, LZCNT and AVX2 instructions.
:::

or errors like:

::: prompt
The following have been reloaded with a version change: 1)
cluster/victini => cluster/doduo

Illegal instruction
:::

When we swap to a different cluster, the available modules change so
they work for that cluster. That means that if the cluster and the login
nodes have a different CPU architecture, software loaded using modules
might not work.

If you want to test software on the login nodes, make sure the
`cluster/` module is loaded (with `module swap cluster/`, see ), since
the login nodes and have the same CPU architecture.

If modules are already loaded, and then we swap to a different cluster,
all our modules will get reloaded. This means that all current modules
will be unloaded and then loaded again, so they'll work on the newly
loaded cluster. Here's an example of how that would look like:

::: prompt
Due to MODULEPATH changes, the following have been reloaded: 1)
GCCcore/6.4.0 5) Tcl/8.6.8-GCCcore-6.4.0 9)
iccifort/2018.1.163-GCC-6.4.0-2.28 13)
impi/2018.1.163-iccifort-2018.1.163-GCC-6.4.0-2.28 17)
ncurses/6.0-GCCcore-6.4.0 2) GMP/6.1.2-GCCcore-6.4.0 6)
binutils/2.28-GCCcore-6.4.0 10) ifort/2018.1.163-GCC-6.4.0-2.28 14)
intel/2018a 18) zlib/1.2.11-GCCcore-6.4.0 3) Python/2.7.14-intel-2018a
7) bzip2/1.0.6-GCCcore-6.4.0 11) iimpi/2018a 15)
libffi/3.2.1-GCCcore-6.4.0 4) SQLite/3.21.0-GCCcore-6.4.0 8)
icc/2018.1.163-GCC-6.4.0-2.28 12) imkl/2018.1.163-iimpi-2018a 16)
libreadline/7.0-GCCcore-6.4.0

The following have been reloaded with a version change: 1)
cluster/victini => cluster/swalot
:::

This might result in the same problems as mentioned above. When swapping
to a different cluster, you can run `module purge` to unload all modules
to avoid problems (see ).
