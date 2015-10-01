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

import settings
import json

__author__ = 'Alejandro F. Carrera'


def save_json_metadata(metadata):
    settings.print_message(" - Saving metadata at json format ... ")
    f = open("generated/metadata.json", "w")
    f.write(json.dumps(metadata))
    f.close()


def generate_pycode():
    settings.print_message(" - Generating Python code ... ")
    f = open("generated/template.tmp", "r")
    t_file = f.read()
    f.close()
    f = open("generated/glapi.py", "w")
    f.write(t_file)
    f.close()


def generate_pypi(version):
    settings.print_message(" - Generating Pypi: %s ... " % version)
    f = open("generated/settings.tmp", "r")
    t_settings = f.read()
    f.close()
    t_settings = t_settings.replace("API_VERSION_TEMPLATE", version)
    f = open("generated/settings.py", "w")
    f.write(t_settings)
    f.close()

