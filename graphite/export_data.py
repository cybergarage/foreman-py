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
        from query import Query
        from metric import Metric
    else:
        from .graphite import Graphite
        from .query import Query
        from .metric import Metric

    if (len(sys.argv) < 5):
        sys.stdout.write('%s <host> <port> <target> <from> <until>\n' % (os.path.basename(sys.argv[0])))
        exit()

    g = Graphite()
    g.host = sys.argv[1]
    g.port = int(sys.argv[2])

    q = Query()
    q.target = sys.argv[3]
    q.since = sys.argv[4]
    q.until = sys.argv[5]

    metrics = g.queryMetricsData(q)
    for m in metrics:
        sys.stdout.write('%s\n' % str(m))

