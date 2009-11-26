Introduction
============

An interactive ipython shell to be used in your doctest, very similar to and
based on interlude.


Usage
=====

    >>> from chaoflow.testing.ipython import ipshell

By default you will get a prompt suitable to copy/paste for doctests.

    >>> ipshell( locals())

In order to get the default ipython prompt, pass doctest=False:

    >>> ipshell( locals(), doctest=False)


License
=======

chaoflow.testing.ipython is licensed under LGPLv3. Please let me know if this
presents a problem for you.
