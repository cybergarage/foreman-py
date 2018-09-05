#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Satoshi Konno. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

from abc import ABCMeta, abstractmethod

import sys
import requests
from datetime import datetime

from metric import Metric
from query import Query

FOREMAN_GRAPHITE_DEFAULT_TIMEOUT = 10

class Graphite():
    def __init__(self):
        self.protocol = 'http'
        self.host = None
        self.port = 8080
 
    def baseURL(self):
        if not self.host or not self.protocol or not self.port:
            return None
        return '%s://%s:%d' % (self.protocol, self.host, self.port)

    def queryMetrics(self):
        baseURL = self.baseURL()
        if not baseURL:
            return False
        url = '%s/metrics/index.json' % (baseURL)
        try:
            targets = requests.get(url, timeout=FOREMAN_GRAPHITE_DEFAULT_TIMEOUT).json()
            return targets
        except Exception as e:
            sys.stdout.write(e)
        return None

    def queryMetricsData(self, query):
        baseURL = self.baseURL()
        target = query.target
        sinceStr = query.since
        untilStr = query.until
        if not baseURL or not target:
            return None
        url = '%s/render?target=%s&from=%s&until=%s&format=json' % (baseURL, target, sinceStr, untilStr)
        try:
            queryObjs = requests.get(url, timeout=FOREMAN_GRAPHITE_DEFAULT_TIMEOUT).json()
        except Exception as e:
            sys.stdout.write(e)
            return None
        if queryObjs is None:
            return None
        metrics = []
        for queryObj in queryObjs:
            target = queryObj['target']
            for dataPoint in queryObj['datapoints']:
                m = Metric([target, dataPoint[0], dataPoint[1]])
                metrics.append(m)
        return metrics
