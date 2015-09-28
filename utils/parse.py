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

import os
import shutil
import settings
from HTMLParser import HTMLParser

__author__ = 'Alejandro F. Carrera'


def check_api_call(string):

    # Remove examples
    if "?" in str(string):
        return False

    # Only detect 4 HTTP Methods
    call = ["GET", "POST", "PUT", "DELETE"]
    for i in call:
        if str(string).startswith(i):
            return True
    return False


def generate_name_from_metadata(method, string, param):
    __name = method.lower()
    if __name == "put":
        __name = "modify"
    elif __name == "post":
        __name = "create"
    else:
        pass
    __string = string
    for i in param:
        __string = __string.replace("/:" + i, "")
    __string = __string.split("/")
    for i in __string:
        __name += ("_" + i)
    return __name


def generate_param_from_metadata(string):
    __string_arr = string.split(":")
    __string_arr.pop(0)
    __string_res = []
    for i in __string_arr:
        if "/" in i:
            __string_res.append(i.split("/")[0])
        else:
            __string_res.append(i)
    return __string_res


def generate_metadata(string):
    __string = str(string)

    # Remove Whitespaces
    __string.strip()
    __string = " ".join(__string.split())
    __string = __string.replace(" ", "")

    # Get Method and Parse
    __methods = ["GET", "POST", "PUT", "DELETE"]
    __match = [s for s in __methods if __string.startswith(s)]
    if len(__match) > 0:
        __match = __match[0]
        __string = __string.replace(__match + "/", "")
        __parameters = generate_param_from_metadata(__string)
        __name = generate_name_from_metadata(__match, __string, __parameters)
        return {
            "string": __string,
            "name": __name,
            "method": __match,
            "param": __parameters,
            "param_number": len(__parameters)
        }
    return {}


class CUSTOM_PARSE(HTMLParser):

    pre_tag = None

    def __init__(self):
        self.reset()
        self.actual_tag = None
        self.name = None
        self.api = {}

    def handle_starttag(self, tag, attrs):
        self.actual_tag = tag

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.actual_tag == "code" and check_api_call(data):
            md = generate_metadata(data)
            self.api[md.get("string")] = md


def generate_code_from_file(file_name, file_path):

    # Get function
    name_lo = str(file_name).replace(".html", "").lower()
    name = name_lo.upper()

    # Get file
    fi = open(file_path, 'r')

    # Parse file
    parser = CUSTOM_PARSE()
    parser.name = name_lo
    parser.feed(fi.read())

    for i in parser.api:
        print("%s : %s" % (i, parser.api[i]))

    return {
        "name": name_lo,
        "data": None
    }


def generate_code_for_dir(file_dir):
    md = {}
    settings.print_message(" - Generating code: %s ... " % file_dir)
    for i in os.listdir(file_dir):
        gen_code = generate_code_from_file(i, file_dir + "/" + i)
        md[gen_code.get("name")] = gen_code.get("data")
    return md
