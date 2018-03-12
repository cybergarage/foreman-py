#################################################################
#
# Foreman for Python
#
# Copyright (C) 2017 Yahoo Japan Corporation. All rights reserved.
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import urllib
import requests

from .constants import FOREMAN_DEFAULT_SERVER_HOST, FOREMAN_DEFAULT_HTTP_PORT, FOREMAN_HTTP_SERVER_FQL_PATH, FOREMAN_HTTP_SERVER_FQL_QUERY
from .constants import FOREMAN_CONFIG_CATEGORY_KEY, FOREMAN_CONFIG_PRODUCT_KEY, FOREMAN_CONFIG_VERSION_KEY
from .exceptions import ConnectionError

class Client:
    def __init__(self):
        self.host = FOREMAN_DEFAULT_SERVER_HOST
        self.port = FOREMAN_DEFAULT_HTTP_PORT

    def query(self, query):
        try:
            url = self.__create_query_url(query)
            res = requests.get(url)
            return res
        except requests.exceptions.ConnectionError:
            raise ConnectionError(self.host, self.port)
        except:
            raise

    def query_text(self, query):
        res = self.query(query)
        if res.status_code != 200:
            return 'INVALID REQUEST : %s (%d)' % (query, res.status_code)
        return res.text

    def query_json(self, query):
        res = self.query(query)
        if res.status_code != 200:
            return None
        return res.json()

    def query_version(self):
        query = 'EXPORT FROM CONFIG'
        json = self.query_json(query)
        if json is None:
            return ''
        product = json[FOREMAN_CONFIG_CATEGORY_KEY][FOREMAN_CONFIG_PRODUCT_KEY]
        ver = json[FOREMAN_CONFIG_CATEGORY_KEY][FOREMAN_CONFIG_VERSION_KEY]
        return '%s v%s (%s:%d)' % (product.capitalize(), ver, self.host, self.port)

    def __create_query_url(self, query):
        url = 'http://%s:%d%s?%s' % (
            self.host, 
            self.port, 
            FOREMAN_HTTP_SERVER_FQL_PATH,
            urllib.urlencode({FOREMAN_HTTP_SERVER_FQL_QUERY : query}))
        return url
