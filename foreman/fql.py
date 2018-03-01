#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Yahoo Japan Corporation. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import sys
import select

def main(options):
    c = Console()
    if select.select([sys.stdin,],[],[],0.0)[0]:
        c.tty = False
    c.loop()

if __name__ == '__main__':
    if __package__ is None:
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from foreman import Console
    else:
        from .console import Console

    main(sys.argv[1:])
