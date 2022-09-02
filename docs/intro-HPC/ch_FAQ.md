# Frequently Asked Questions {#ch:faq}

## When will my job start?

See the explanation about how jobs get prioritized in . In practice it's
impossible to predict when your job(s) will start, since most currently
running jobs will finish before their requested walltime expires, and
new jobs by may be submitted by other users that are assigned a higher
priority than your job(s). You can use the `showstart` command. For more
information, see .

## Can I share my account with someone else?

You are not allowed to share your VSC account with anyone else, it is
strictly personal. See
<https://helpdesk.ugent.be/account/en/regels.php>. For KU Leuven, see
<https://admin.kuleuven.be/personeel/english_hrdepartment/ICT-codeofconduct-staff#section-5>.
For Hasselt University, see <https://www.uhasselt.be/intra/IVC>. See
<http://www.vub.ac.be/sites/vub/files/reglement-gebruik-ict-infrastructuur.pdf>.
See <https://pintra.uantwerpen.be/bbcswebdav/xid-23610_1> If you want to
share data, there are alternatives (like a shared directories in VO
space, see ).

## Can I share my data with other users?

Yes, you can use the `chmod` or `setfacl` commands to change permissions
of files so other users can access the data. For example, the following
command will enable a user named "otheruser" to read the file named
`dataset.txt`. See

::: prompt
-rwxr-x---+ 2
:::

For more information about `chmod` or `setfacl`, see [the section on
chmod in chapter 3 of the Linux intro
manual](\LinuxManualURL#sec:chmod).

## Can I use multiple different SSH key pairs to connect to my VSC account?

Yes, and this is recommended when working from different computers.
Please see on how to do this.

## I want to use software that is not available on the clusters yet {#sec:software-installation}

Please fill out the details about the software and why you need it in
this form:
<https://www.ugent.be/hpc/en/support/software-installation-request>.
When submitting the form, a mail will be sent to containing all the
provided information. The HPC team will look into your request as soon
as possible you and contact you when the installation is done or if
further information is required. Please send an e-mail to that includes:

-   What software you want to install and the required version

-   Detailed installation instructions

-   The purpose for which you want to install the software
