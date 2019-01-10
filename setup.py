#!/usr/bin/env python
#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Satoshi Konno. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

from setuptools import setup

setup(
    name='foreman_client',
    version='0.1',
    description="Time series failure analisys utility.",
    author='Satoshi Konno',
    author_email='skonno@cybergarage.org',
    url='https://github.com/cybergarage/foreman-py',
    license='BSD',
    packages=[
        'foreman'
    ],
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'fqlsh = foreman.fql:main'
        ]
    },
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
