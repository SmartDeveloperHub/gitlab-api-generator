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

from subprocess import call
import settings
import json
import os

__author__ = 'Alejandro F. Carrera'


def save_json_metadata(metadata):
    settings.print_message(" - Saving metadata at json format ... ")
    f = open("generated/data/metadata.json", "w")
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


def generate_settings(version):
    __version = str(version).replace("-", ".")
    settings.print_message(" - Generating settings.py: %s ... " % __version)
    f = open("generated/settings.tmp", "r")
    t_settings = f.read()
    f.close()
    t_settings = t_settings.replace("API_VERSION_TEMPLATE", __version + ".4")
    f = open("generated/settings.py", "w")
    f.write(t_settings)
    f.close()


def generate_pypi_settings():
    settings.print_message(" - Generating pypi config ... ")
    f = open("generated/pypi.tmp", "r")
    p_settings = f.read()
    f.close()
    p_settings = p_settings.replace("PYPI_USERNAME", settings.PYPI_USER)
    p_settings = p_settings.replace("PYPI_PASSWORD", settings.PYPI_PASS)
    f = open(os.path.join(os.path.expanduser('~'), ".pypirc"), "w")
    f.write(p_settings)
    f.close()


def upload_package():
    settings.print_message(" - Uploading pypi package ... ")
    os.chdir("generated")
    call(["python", "setup.py", "sdist", "register", "upload", "-r", "pypi"])
    os.chdir("./../")
