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
import logging

__author__ = 'Alejandro F. Carrera'

# Generator Package Configuration
NAME = "gl-api-generator"
VERSION = "0.1.0"
DEBUGGER = True
LONGNAME = "Gitlab API Generator"

# Generator Paths
GEN_GL_PATH = "https://gitlab.com/gitlab-org/gitlab-ce.git"
GEN_DISK_PATH = "gitlab-ce-repo"
GEN_BRANCH = "stable"


def print_message(msg):
    if DEBUGGER:
        logging.warn("[DEBUG] %s" % msg)
    else:
        logging.info("[INFO] %s" % msg)


def print_error(msg):
    if DEBUGGER:
        logging.warn("[ERROR] %s" % msg)
    else:
        logging.info("[ERROR] %s" % msg)