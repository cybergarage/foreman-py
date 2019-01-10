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
import json

from .client import Client
from .exceptions import ConnectionError

FOREMAN_CONSOLE_PROMPT = "shell> "


class Console(object):
    def __init__(self):
        self.tty = True
        self.eof = False
        self.client = Client()
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def set_host(self, host):
        self.client.host = host

    def set_port(self, port):
        self.client.port = port

    def next_query(self, prompt=''):
        query = ''
        if self.tty:
            query = raw_input(prompt)
        else:
            query = sys.stdin.readline()
            if query:
                query = query.strip(' \t\n\r')
                self.output(query)
                self.output_lf()
            else:
                self.eof = True
        return query

    def loop(self):
        while not self.eof:
            try:
                query = self.next_query(FOREMAN_CONSOLE_PROMPT)
                if query:
                    self.execute(query)
            except KeyboardInterrupt:
                self.output_lf()
                break
            except EOFError:
                self.output_lf()
                break
            except ConnectionError as err:
                self.output(err.message)
                self.output_lf()
                break

    def execute(self, query):
        self.output_lf()
        res, err = self.client.query_json(query)
        msg = None
        if json is not None:
            msg = json.dumps(res, indent=4)
        if err is not None:
            msg = json.dumps(err, indent=4)
        if msg is not None:
            self.output(msg)
            self.output_lf()
        self.output_lf()

    def output(self, line):
        self.stdout.write(line)

    def output_lf(self):
        self.stdout.write('\n')

    def output_version(self):
        ver = self.client.query_version()
        self.output(ver)
        self.output_lf()
