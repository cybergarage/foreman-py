#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Satoshi Konno. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################


class ConnectionError(Exception):
    def __init__(self, host, port):
        self.message = 'Could not connect to %s:%d' % (host, port)
        super(ConnectionError, self).__init__(self.message)
