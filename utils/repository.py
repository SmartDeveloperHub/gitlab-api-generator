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
from subprocess import call

__author__ = 'Alejandro F. Carrera'


def get_branches_with_filter(repository, fil):
    __branches = repository.branches.keys()
    if fil is None:
        return __branches
    else:
        return [x for x in __branches if fil in x]


def remove_info_from_branches(branches_list, fil, branches_to_remove):
    __branches = branches_list
    for i in branches_to_remove:
        __branches.remove(i)
    return map(lambda x: x.replace("-" + fil, ""), __branches)


def move_to_specific_branch(repository, branch):
    repository.switch_branch(branch)


def move_docs_folder(source, destination):
    shutil.rmtree("/tmp/destiny_tmp", True)
    shutil.move(source, "/tmp/destiny_tmp")
    shutil.rmtree(destination, True)
    shutil.move("/tmp/destiny_tmp", destination)


def remove_file(file_path):
    os.remove(file_path)


def generate_doc(branch):
    file_path = settings.GEN_DOC_DISK_PATH
    if os.path.exists(file_path):
        if not os.path.isdir(file_path):
            os.remove(file_path)
        else:
            shutil.rmtree(file_path, True)
    settings.print_message(" - Generating branch: %s." % branch)
    call(["./gitlab-docs/generate.rb"])

