#!/usr/bin/env python
#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Yahoo Japan Corporation. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import os
import sys
from setuptools import setup

setup(
    name='foreman-py',
    version='0.1',
    description="Time series failure analisys utility.",
    author='Yahoo Japan Corporation',
    author_email='skonno@yahoo-corp.jp',
    url='https://ghe.corp.yahoo.co.jp/skonno/foreman-py',
    license='BSD',
    packages=[
        'foreman'
    ],
    install_requires=[
        'requests',
    ],
    test_suite='tests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'License :: OSI Approved :: BSD License',
    ],    
)
