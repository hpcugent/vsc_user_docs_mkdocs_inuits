# Useful Linux Commands { #ch:useful-linux-commands}

## Basic Linux Usage

All the clusters run some variant of the "" operating system. This means
that, when you connect to one of them, you get a command line interface,
which looks something like this:

::: prompt
:::

When you see this, we also say you are inside a "shell". The shell will
accept your commands, and execute them.

  ls     Shows you a list of files in the current directory
  ------ ----------------------------------------------------
  cd     Change current working directory
  rm     Remove file or directory
  nano   Text editor
  joe    Text editor
  echo   Prints its parameters to the screen

Most commands will accept or even need parameters, which are placed
after the command, separated by spaces. A simple example with the "echo"
command:

::: prompt
This is a test
:::

Important here is the "\$" sign in front of the first line. This should
not be typed, but is a convention meaning "the rest of this line should
be typed at your shell prompt". The lines not starting with the "\$"
sign are usually the feedback or output from the command.

More commands will be used in the rest of this text, and will be
explained then if necessary. If not, you can usually get more
information about a command, say the item or command "ls", by trying
either of the following:

::: prompt
:::

(You can exit the last two "manuals" by using the "q" key.) For more
exhaustive tutorials about Linux usage, please refer to the following
sites: <http://www.linux.org/lessons/>
<http://linux.about.com/od/nwb_guide/a/gdenwb06.htm>

## How to get started with shell scripts

In a shell script, you will put the commands you would normally type at
your shell prompt in the same order. This will enable you to execute all
those commands at any time by only issuing one command: starting the
script.

Scripts are basically non-compiled pieces of code: they are just text
files. Since they don't contain machine code, they are executed by what
is called a "parser" or an "interpreter". This is another program that
understands the command in the script, and converts them to machine
code. There are many kinds of scripting languages, including Perl and
Python.

Another very common scripting language is shell scripting. In a shell
script, you will put the commands you would normally type at your shell
prompt in the same order. This will enable you to execute all those
commands at any time by only issuing one command: starting the script.

Typically in the following examples they'll have on each line the next
command to be executed although it is possible to put multiple commands
on one line. A very simple example of a script may be:

::: code
bash echo \"Hello! This is my hostname:\" hostname
:::

You can type both lines at your shell prompt, and the result will be the
following:

::: prompt
Hello! This is my hostname:
:::

Suppose we want to call this script "foo". You open a new file for
editing, and name it "foo", and edit it with your favourite editor

::: prompt
:::

::: prompt
:::

or use the following commands:

::: prompt
:::

The easiest ways to run a script is by starting the interpreter and pass
the script as parameter. In case of our script, the interpreter may
either be "sh" or "bash" (which are the same on the cluster). So start
the script:

::: prompt
Hello! This is my hostname:
:::

Congratulations, you just created and started your first shell script!

A more advanced way of executing your shell scripts is by making them
executable by their own, so without invoking the interpreter manually.
The system can not automatically detect which interpreter you want, so
you need to tell this in some way. The easiest way is by using the so
called "shebang" notation, explicitly created for this function: you put
the following line on top of your shell script
"#!/path/to/your/interpreter".

You can find this path with the "which" command. In our case, since we
use bash as an interpreter, we get the following path:

::: prompt
/bin/bash
:::

We edit our script and change it with this information:

::: code
bash #!/bin/bash echo \"Hello! This is my hostname:\" hostname
:::

Note that the "shebang" must be the first line of your script! Now the
operating system knows which program should be started to run the
script.

Finally, we tell the operating system that this script is now
executable. For this we change its file attributes:

::: prompt
:::

Now you can start your script by simply executing it:

::: prompt
Hello! This is my hostname:
:::

The same technique can be used for all other scripting languages, like
Perl and Python.

Most scripting languages understand that lines beginning with "\#" are
comments, and should be ignored. If the language you want to use does
not ignore these lines, you may get strange results ...

## Linux Quick reference Guide

### Archive Commands

  tar                     An archiving program designed to store and extract files from an archive known as a tar file.
  ----------------------- -----------------------------------------------------------------------------------------------
  tar -cvf foo.tar foo/   compress the contents of foo folder to foo.tar
  tar -xvf foo.tar        extract foo.tar
  tar -xvzf foo.tar.gz    extract gzipped foo.tar.gz

### Basic Commands

  ls      Shows you a list of files in the current directory
  ------- ----------------------------------------------------
  cd      Change the current directory
  rm      Remove file or directory
  mv      Move file or directory
  echo    Display a line or text
  pwd     Print working directory
  mkdir   Create directories
  rmdir   Remove directories

### Editor

  emacs   
  ------- ----------------------------------------------------
  nano    Nano's ANOther editor, an enhanced free Pico clone
  vi      A programmers text editor

### File Commands

  cat    Read one or more files and print them to standard output
  ------ ------------------------------------------------------------------
  cmp    Compare two files byte by byte
  cp     Copy files from a source to the same or different target(s)
  du     Estimate disk usage of each file and recursively for directories
  find   Search for files in directory hierarchy
  grep   Print lines matching a pattern
  ls     List directory contents
  mv     Move file to different targets
  rm     Remove files
  sort   Sort lines of text files
  wc     Print the number of new lines, words, and bytes in files

### Help Commands

  man   Displays the manual page of a command with its name, synopsis, description, author, copyright etc.
  ----- ----------------------------------------------------------------------------------------------------

### Network Commands

  hostname   show or set the system's host name
  ---------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ifconfig   Display the current configuration of the network interface. It is also useful to get the information about IP address, subnet mask, set remote IP address, netmask etc.
  ping       send ICMP ECHO_REQUEST to network hosts, you will get back ICMP packet if the host responds. This command is useful when you are in a doubt whether your computer is connected or not.

### Other Commands

  logname   Print user's login name
  --------- --------------------------------------------------------------------------------------
  quota     Display disk usage and limits
  which     Returns the pathnames of the files that would be executed in the current environment
  whoami    Displays the login name of the current effective user

### Process Commands

  &         In order to execute a command in the background, place an ampersand (&) on the command line at the end of the command. A user job number (placed in brackets) and a system process number are displayed. A system process number is the number by which the system identifies the job whereas a user job number is the number by which the user identifies the job
  --------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  at        executes commands at a specified time
  bg        Places a suspended job in the background
  crontab   crontab is a file which contains the schedule of entries to run at specified times
  fg        A process running in the background will be processed in the foreground
  jobs      Lists the jobs being run in the background
  kill      Cancels a job running in the background, it takes argument either the user job number or the system process number
  ps        Reports a snapshot of the current processes
  top       Display Linux tasks

### User Account Commands

  chmod   Modify properties for users
  ------- -----------------------------
  chown   Change file owner and group
