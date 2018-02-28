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

class Console:
    def __init__(self):
        self.tty = True
        self.stop = False

    def next_query(self, prompt=''):
        query = ''
        if self.tty:
            query = raw_input(prompt)
        else:
            query = sys.stdin.readline()
        return query

    def loop(self):
        while not self.stop:
            try:
                query = self.next_query()
            except KeyboardInterrupt:
                break
            except EOFError:
                break
