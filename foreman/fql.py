#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Satoshi Konno. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

if __name__ == '__main__':
    import sys
    import select

    if __package__ is None:
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from foreman import Console
    else:
        from .console import Console

    try:
        c = Console()
        if select.select([sys.stdin,],[],[],0.0)[0]:
             c.tty = False
        if c.tty:
            c.output_version()
        c.loop()
    except Exception as e:
        print("ERROR: " + e.message)
