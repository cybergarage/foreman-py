#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Yahoo Japan Corporation. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

if __name__ == '__main__':
    import os
    import sys
    import select
    if __package__ is None:
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from graphite import Graphite
    else:
        from .graphite import Graphite

    if (len(sys.argv) < 3):
        sys.stdout.write('%s <host> <port>\n' % (os.path.basename(sys.argv[0])))
        exit()

    g = Graphite()
    g.host = sys.argv[1]
    g.port = int(sys.argv[2])
    targets = g.queryMetrics()
    for target in targets:
        sys.stdout.write('%s\n' % (target))

