Introduction
============

An interactive ipython shell to be used in your doctest. Very similar to and
based on interlude.


Usage
=====

    >>> from chaoflow.testing.ipython import ipshell

By default you will get a prompt suitable to copy/paster for doctests.

    >>> ipshell( locals())

In order to get the default ipython prompt, pass doctest=False:

    >>> ipshell( locals(), doctest=False)


LICENSE
=======

chaoflow.testing.crawler is licensed under LGPLv3. Please let me know if this
presents a problem for you.
