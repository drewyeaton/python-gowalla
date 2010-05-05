#!/usr/bin/python2.5
#
# Copyright 2010 Sentinel Design. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''A minimalist Python interface for the Gowalla API'''

__author__ = 'Drew Yeaton <drew@sentineldesign.net>'
__version__ = '1.0'


import base64
import types
import urllib
import urllib2
from urllib2 import URLError, HTTPError

import simplejson


URL = 'http://gowalla.com'

# Names of each action and its related request method
CRUD_METHODS = {
        'create': 'POST',
        'read': 'GET',
        'update': 'PUT',
        'delete': 'DELETE'
    }


class GowallaException(Exception): pass
class GowallaConnectionException(GowallaException): pass

class GowallaResourceInvalidException(GowallaException): pass
class GowallaUnauthorizedException(GowallaException): pass
class GowallaResourceNotFoundException(GowallaException): pass
class GowallaMethodNotAllowedException(GowallaException): pass
class GowallaNotAcceptableException(GowallaException): pass
class GowallaApplicationErrorException(GowallaException): pass



class Gowalla(object):
    username = ''
    password = ''
    api_key =''
    uri = ''
    response = None
    errors = None
    
    def __init__(self, username='', password='', api_key='', uri=''):
        self.username = username
        self.password = password
        self.api_key = api_key
        self.uri = uri
    
    
    def __getattr__(self, k):
        try:
            return object.__getattr__(self, k)
        except AttributeError:
            return Gowalla(self.username, self.password, self.api_key, self.uri + '/' + k)
    
    
    def __call__(self, **kwargs):
        # Split out uri into segments and assume the last segment is an 
        # action. If it isn't place it on the end of the url again
        urili = self.uri.split('/')

        # Determine method with which to to request uri
        action = urili.pop()
        try:
            method = CRUD_METHODS[action]
        except KeyError:
            urili.append(action)
            method = 'GET'

        # If pk is set in arguments, place it in url instead
        uid = kwargs.pop('id', False)
        if uid:
            urili.insert(2, uid)

        data = None

        # Build argument list if necessary
        args = ''
        if method == 'GET' and kwargs:
            args = "?%s" % (urllib.urlencode(kwargs.items()))
        
        # Build url from the pieces
        url = "%s%s%s" % (URL, '/'.join(urili), args)
        
        # Build request with our new url, method, and data
        opener = urllib2.build_opener(urllib2.HTTPHandler)
        self._request = urllib2.Request(url=url, data=data)
        self._request.get_method = lambda: method
        self._request.add_header('Accept', 'application/json')
        self._request.add_header('Content-Type', 'application/json')
        self._request.add_header('Authorization', 'Basic %s' % base64.encodestring('%s:%s' % (self.username, self.password))[:-1])
        self._request.add_header('-Gowalla-API-Key', self.api_key)

        try:                        
            response = opener.open(self._request)
            json_response = response.read()
        except HTTPError, e:
            if e.code in range(200, 205):
                pass
            elif e.code == 400:
                raise GowallaResourceInvalidException(e.read())
            elif e.code == 401:
                raise GowallaUnauthorizedException(e)
            elif e.code == 404:
                raise GowallaResourceNotFoundException(e)
            elif e.code == 405:
                raise GowallaMethodNotAllowedException(e)
            elif e.code == 406:
                raise GowallaNotAcceptableException(e)
            elif e.code == 500:
                raise GowallaApplicationErrorException(e)
            else:
                raise GowallaException(e)
        except URLError, e:
            raise GowallaConnectionException(e)
                
        self.response = simplejson.loads(json_response)
                        
        return self.response

__all__ = [
        'Gowalla',
        'GowallaException',
        'GowallaConnectionException',
        'GowallaResourceInvalidException',
        'GowallaUnauthorizedException',
        'GowallaResourceNotFoundException',
        'GowallaMethodNotAllowedException',
        'GowallaNotAcceptableException',
        'GowallaApplicationErrorException',
    ]