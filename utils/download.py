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


def clone_repo(repository, file_path):
    settings.print_message(" - Cloning %s ... Please wait" % repository)
    repo = gittle.Gittle.clone(repository, file_path, bare=False)
    settings.print_message(" - Cloned at %s directory." % file_path)
    return repo


def get_repo(repository, file_path):

    if os.path.exists(file_path):
        if not os.path.isdir(file_path):
            settings.print_message(" - Removed file: %s." % file_path)
            os.remove(file_path)
        else:
            settings.print_message(" - Removed directory: %s." % file_path)
            shutil.rmtree(file_path, True)
    return clone_repo(repository, file_path)


def get_repo_gitlab():
    return get_repo(settings.GEN_GL_GIT, settings.GEN_GL_DISK_PATH)


def get_repo_library():
    return get_repo(settings.GEN_REP_GIT, settings.GEN_REP_DISK_PATH)


def get_repo_documentation():
    return get_repo(settings.GEN_DOC_GIT, settings.GEN_DOC_DISK_PATH)
