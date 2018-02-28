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

from .console import Console

def main(options):
    c = Console()
    c.loop()

if __name__ == '__main__':
    main(sys.argv[1:])