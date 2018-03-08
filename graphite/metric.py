#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Yahoo Japan Corporation. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

from datetime import datetime
import time

class Metric:
    def __init__(self, values=None):
        self.clear()
        self.__set(values)

    def __str__(self):
        if self.value is None and self.timestamp is None:
            if not self.target is None:
                return self.target
        return '%s,%s,%d' % (self.target, str(self.value), self.posixtime)

    def clear(self):
        self.target = None
        self.value = None
        self.timestamp = None

    @property
    def posixtime(self):
        if self.timestamp is None:
            return 0
        return int(time.mktime(self.timestamp.timetuple()))

    def __set(self, values):
        if values is None or len(values) != 3:
            return False 
        self.target = values[0]
        if values[1] is not None:
            self.value = float(values[1])
        else:
            self.value = None
        self.timestamp = datetime.fromtimestamp(int(values[2])) #self.posixtime = values[2]
        return True
