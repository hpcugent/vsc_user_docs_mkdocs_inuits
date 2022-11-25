# Graphical applications with VNC { #ch:vnc}

. Please see for more information.

Virtual Network Computing is a graphical desktop sharing system that
enables you to interact with graphical software running on the HPC
infrastructure from your own computer.

## Starting a VNC server { #sec:start-vnc}

First login on the login node (see ), then start `vncserver` with:

::: prompt
You will require a password to access your desktops.

Password: Verify: Would you like to enter a view-only password (y/n)? A
view-only password is not used

New '

Creating default startup script Creating default config Starting
applications specified in Log file is
:::

Note down the details in bold: the hostname (in the example: ``) and the
(partial) port number (in the example: `6`).

It's important to remember that VNC sessions are permanent. They survive
network problems and (unintended) connection loss. This means you can
logout and go home without a problem (like the terminal equivalent
`screen` or `tmux`). This also means you don't have to start `vncserver`
each time you want to connect.

## List running VNC servers { #sec:list-vnc}

You can get a list of running VNC servers on a node with

::: prompt
TigerVNC server sessions:

X DISPLAY \# PROCESS ID :6 30713
:::

This only displays the running VNC servers on .

To see what login nodes you are running a VNC server on, you can run the
`ls .vnc/*.pid` command in your home directory: the files shown have the
hostname of the login node in the filename:

::: prompt
.vnc/ .vnc/
:::

This shows that there is a VNC server running on `` on port 5906 and
another one running `` on port 5908 (see also ).

## Connecting to a VNC server

The VNC server runs on a (in the example above, on ``).

In order to access your VNC server, you will need to set up an SSH
tunnel from your workstation to this login node (see ).

Login nodes are rebooted from time to time. You can check that the VNC
server is still running in the same node by executing `vncserver -list`
(see also ). If you get an empty list, it means that there is no VNC
server running on the login node.

The *host* is `localhost`, which means "your own computer": we set up an
SSH tunnel that connects the VNC port on the login node to the same port
on your local computer.

### Determining the source/destination port { #sec:source-port-vnc}

The *destination port* is the port on which the VNC server is running
(on the login node), which is we noted down earlier (`6`); in the
running example, that is `5906`.

The *source port* is the port you will be connecting to with your VNC
client on your workstation. Although you can use any (free) port for
this, we strongly recommend to use the .

So, in our running example, both the source and destination ports are
`5906`.

### Picking an intermediate port to connect to the right login node { #sec:intermediate-port-vnc}

In general, you have no control over which login node you will be on
when setting up the SSH tunnel from your workstation to `` (see ).

If the login node you end up on is a different one than the one where
your VNC server is running (i.e., `` rather than `` in our running
example), you need to create a on the login node you are connected to,
in order to \"patch through\" to the correct port on the login node
where your VNC server is running.

In the remainder of these instructions, we will assume that we are
indeed connected to a different login node. Following these instructions
should always work, even if you happen to be connected to the correct
login node.

To set up the second SSH tunnel, you need to , which will be used as an
*intermediate* port.

Now we have a chicken-egg situation: you need to pick a port before
setting up the SSH tunnel from your workstation to ``, but only after
starting the SSH tunnel will you be able to determine whether the port
you picked is actually free or not...

In practice, if you , you have a good chance that the port will not be
used yet.

We will proceed with $12345$ as intermediate port, but . If you need
some inspiration, run the following command on a Linux server (for
example on a login node): `echo $RANDOM` (but do not use a value lower
than $1025$).

### Setting up the SSH tunnel(s) { #sec:ssh-tunnel-vnc}

#### Setting up the first SSH tunnel from your workstation to 

First, we will set up the SSH tunnel from our workstation to .

Use the settings specified in the sections above:

-   *source port*: the port on which the VNC server is running (see );

-   *destination host*: `localhost`;

-   *destination port*: use the intermediate port you picked (see )

See for detailed information on how to configure PuTTY to set up the SSH
tunnel, by entering the settings in the and fields in .

Execute the following command to set up the SSH tunnel.\

::: prompt
:::

With this, we have forwarded port `5906` on our workstation to port
`12345` on the login node we are connected to.

#### Checking whether the intermediate port is available

Before continuing, it's good to check whether the intermediate port that
you have picked is actually still available (see ).

You can check using the following command ():

::: prompt
:::

If you see no matching lines, then the port you picked is still
available, and you can continue.

If you see one or more matching lines as shown below, .

::: prompt
:::

#### Setting up the second SSH tunnel to the correct login node

In the session on the login node you created by setting up an SSH tunnel
from your workstation to ``, you now need to set up the second SSH
tunnel to \"patch through\" to the login node where your VNC server is
running (`` in our running example, see ).

To do this, run the following command:

::: prompt
:::

With this, we are forwarding port `12345` on the login node we are
connected to (which is referred to as `localhost`) through to port
`5906` on our target login node (``).

Combined with the first SSH tunnel, port `5906` on our workstation is
now connected to port `5906` on the login node where our VNC server is
running (via the intermediate port `12345` on the login node we ended up
one with the first SSH tunnel).

As shown above, you can check again using the `hostname` command whether
you are indeed connected to the right login node. If so, you can go
ahead and connect to your VNC server (see ).

### Connecting using a VNC client { #sec:vnc-client}

You can download a free VNC client from
<https://sourceforge.net/projects/turbovnc/files/>. You can download the
latest version by clicking the top-most folder that has a version number
in it that doesn't also have `beta` in the version. Then download a file
that looks like `TurboVNC64-2.1.2.exe` (the version number can be
different, but the `64` should be in the filename) and execute it. You
can download a free VNC client from
<https://sourceforge.net/projects/turbovnc/files/>. You can download the
latest version by clicking the top-most folder that has a version number
in it that doesn't also have `beta` in the version. Then download a file
ending in `TurboVNC64-2.1.2.dmg` (the version number can be different)
and execute it. Download and setup a VNC client. A good choice is
`tigervnc`. You can start it with the `vncviewer` command.

Now start your VNC client and connect to `localhost:5906`. (see ).

When prompted for a password, use the password you used to setup the VNC
server.

When prompted for default or empty panel, choose default.

If you have an empty panel, you can reset your settings with the
following commands:

::: prompt
:::

## Stopping the VNC server { #sec:stop-vnc}

The VNC server can be killed by running

::: prompt
vncserver -kill :6
:::

where `6` is the port number we noted down earlier. If you forgot, you
can get it with `vncserver -list` (see ).

## I forgot the password, what now?

You can reset the password by first stopping the VNC server (see ), then
removing the `.vnc/passwd` file (with `rm .vnc/passwd`) and then
starting the VNC server again (see ).
