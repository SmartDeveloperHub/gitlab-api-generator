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
import gittle
import settings

__author__ = 'Alejandro F. Carrera'

GEN_DISK_PATH = settings.GEN_DISK_PATH
GEN_GL_PATH = settings.GEN_GL_PATH


def clone_repo():
    settings.print_message("Cloning %s ... Please wait" % GEN_GL_PATH)
    repo = gittle.Gittle.clone(GEN_GL_PATH, GEN_DISK_PATH, bare=True)
    settings.print_message("Cloned %s to %s." % (GEN_GL_PATH, GEN_DISK_PATH))
    return repo


def get_repo():

    if os.path.exists(GEN_DISK_PATH):
        if not os.path.isdir(GEN_DISK_PATH):
            settings.print_message("%s is not directory. It was removed." % GEN_DISK_PATH)
            os.remove(GEN_DISK_PATH)
        else:
            settings.print_message("%s is a directory. It was removed." % GEN_DISK_PATH)
            shutil.rmtree(GEN_DISK_PATH, True)
    return clone_repo()

