#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Satoshi Konno. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

class Query:
    def __init__(self):
        self.clear()

    def clear(self):
       self.target = None
       self.since = None
       self.until = None
