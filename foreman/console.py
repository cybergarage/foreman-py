#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Satoshi Konno. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import sys
from .client import Client

class Console:
    def __init__(self):
        self.tty = True
        self.eof = False
        self.client = Client()

    def next_query(self, prompt=''):
        query = ''
        if self.tty:
            query = raw_input(prompt)
        else:
            query = sys.stdin.readline()
            if query:
                query = query.strip(' \t\n\r')
                print(query)
            else:
                self.eof = True
        return query

    def loop(self):
        while not self.eof:
            try:
                query = self.next_query()
                if query:
                    result = self.client.query(query)
                    if result:
                        print(result)
            except KeyboardInterrupt:
                break
            except EOFError:
                break
