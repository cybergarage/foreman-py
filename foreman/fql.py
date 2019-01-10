#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Satoshi Konno. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

from __future__ import print_function
import sys
import select
from argparse import ArgumentParser
from foreman.console import Console


def main():
    console = Console()

    parser = ArgumentParser(description="Foreman client")
    parser.add_argument(
        "-H", "--host", default="localhost", help="Foreman hostname")
    parser.add_argument(
        "-P", "--port", type=int, default=8188, help="Foreman RPC port")
    parser.add_argument(
        "-E", "--execute", help="FQL statement")
    args = parser.parse_args()

    console.set_host(args.host)
    console.set_port(args.port)
    if args.execute is not None:
        console.execute(args.execute)
        quit()

    if select.select([sys.stdin, ], [], [], 0.0)[0]:
        console.tty = False
    if console.tty:
        console.output_version()
    console.loop()


if __name__ == '__main__':
    main()
