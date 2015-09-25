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


class CUSTOM_PARSE(HTMLParser):

    pre_tag = None

    def __init__(self):
        self.reset()
        self.pre_tag = None
        self.name = None

    def handle_starttag(self, tag, attrs):
        if self.pre_tag == "pre" and tag == "code":
            self.pre_tag = "pre_code"
        else:
            self.pre_tag = tag

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.pre_tag == "pre_code":
            print data
        self.pre_tag = None


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
