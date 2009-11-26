Introduction
============

An interactive ipython shell to be used in your doctest, very similar to and
based on interlude.


Usage
=====

    >>> from chaoflow.testing.ipython import ipshell, dtipshell

By default you will get the default fancy ipython prompt:

    >>> ipshell( locals())

In order to get a prompt suitable for doctest generation, pass doctest=True:

    >>> ipshell( locals(), doctest=True)

or use dtipshell, which does exactly that:

    >>> dtipshell( locals())


License
=======

chaoflow.testing.ipython is licensed under LGPLv3. Please let me know if this
presents a problem for you.
