#################################################################
#
# Foreman for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

.PHONY: all build test

all: test

clean:
	rm -rf tests/__pycache__
	rm -rf tests/*/__pycache__

build:
	./boostrap

test:
	py.test test/unit
