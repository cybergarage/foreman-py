#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Yahoo Japan Corporation. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

class ConnectionError(Exception):
    def __init__(self, host, port):
        self.message = 'Could connect to %s:%d' % (host, port)