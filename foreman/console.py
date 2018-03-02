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

from .client import Client
from .exceptions import ConnectionError

FOREMAN_CONSOLE_PROMPT = "shell> "

class Console:
    def __init__(self):
        self.tty = True
        self.eof = False
        self.client = Client()
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def next_query(self, prompt=''):
        query = ''
        if self.tty:
            query = raw_input(prompt)
        else:
            query = sys.stdin.readline()
            if query:
                query = query.strip(' \t\n\r')
                self.output(query)
                self.outputLF()
            else:
                self.eof = True
        return query

    def loop(self):
        while not self.eof:
            try:
                query = self.next_query(FOREMAN_CONSOLE_PROMPT)
                if query:
                    result = self.client.query_text(query)
                    if result:
                        self.outputLF()
                        self.output(result)
                        self.outputLF()
                        self.outputLF()
            except KeyboardInterrupt:
                self.outputLF()
                break
            except EOFError:
                self.outputLF()
                break
            except ConnectionError as e:
                self.output(e.message)
                self.outputLF()
                break
            except Exception as e:
                self.output(e.message)
                self.outputLF()
                break

    def output(self, s):
        self.stdout.write(s)

    def outputLF(self):
        self.stdout.write('\n')

    def output_version(self):
        ver = self.client.query_version()
        self.output(ver)
        self.outputLF()
