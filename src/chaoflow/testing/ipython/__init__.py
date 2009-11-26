# Copyright (c) 2008-2009 by Florian Friesdorf
# Copyright 2006-2009, BlueDynamics Alliance, Austria - http://bluedynamics.com
#
# Lesser General Public License (LGPL)
#
# This file is part of chaoflow.testing.ipython.
# 
# chaoflow.testing.ipython is free software: you can redistribute it and/or
# modify it under the terms of the Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
# 
# chaoflow.testing.ipython is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# chaoflow.testing.ipython.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Florian Friesdorf <flo@chaoflow.net>"
__docformat__ = "plaintext"

import sys

from IPython.Shell import IPShellEmbed


def ipshell(locals=None, doctest=False):
    """Use ipython interactively in your doctest

    doctest=True turns on doctest mode, i.e. >>> instead of fancy ipython prompt
    """
    argv = []
    if doctest:
        argv.append('-classic')
    shell = IPShellEmbed(
            argv=argv,
            banner='\n'+'='*78+"""
IPython DocTest Interactive Console
Note: You have the same locals available as in your test-case. 
Ctrl-D ends session and continues testing.
""",
            exit_msg="""
end of IPython DocTest Interactive Console session
"""+'='*78+'\n',
            )

    savedstdout = sys.stdout
    sys.stdout = sys.stderr
    shell(local_ns=locals)
    sys.stdout = savedstdout

def dtipshell(locals=None):
    ipshell(locals, doctest=True)
