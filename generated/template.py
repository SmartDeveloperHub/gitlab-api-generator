"""
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
  This file is part of the Smart Developer Hub Project:
    http://www.smartdeveloperhub.org
  Center for Open Middleware
        http://www.centeropenmiddleware.com/
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
  Copyright (C) 2015 Center for Open Middleware.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
            http://www.apache.org/licenses/LICENSE-2.0
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=#
"""

import requests
import json
try:
    from urllib import quote_plus
except ImportError:
    from urllib.parse import quote_plus
    basestring = str

__author__ = 'Alejandro F. Carrera'


class GlAPI(object):
    """Gitlab API class"""

    def __init__(self, host, token="", oauth_token="", ssl=True):
        """on init we setup the token used for api calls
        :param host: Gitlab's host
        :param token: token
        """

        # Save flag to verify ssl connection
        self.ssl = ssl

        # Check and Save Token
        if token != "":
            self.token = token
            self.headers = {"PRIVATE-TOKEN": token}
        elif oauth_token != "":
            self.oauth_token = oauth_token
            self.headers = {"Authorization": ('Bearer {%s}', oauth_token)}

        # Check and Save Gitlab's host
        if not host:
            raise ValueError("")
        self.host = host.rstrip('/')
        if self.host.startswith('http://') or self.host.startswith('https://'):
            pass
        else:
            self.host = 'https://' + self.host

        # Dictionary with urls
        self.api_calls = {}
