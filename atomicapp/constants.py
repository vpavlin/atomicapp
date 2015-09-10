"""
 Copyright 2015 Red Hat, Inc.

 This file is part of Atomic App.

 Atomic App is free software: you can redistribute it and/or modify
 it under the terms of the GNU Lesser General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 Atomic App is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU Lesser General Public License for more details.

 You should have received a copy of the GNU Lesser General Public License
 along with Atomic App. If not, see <http://www.gnu.org/licenses/>.
"""

"""
Update the below LABELS if ATOMICAPPVERSION & NULECULESPECVERSION are updated:
1) LABEL io.projectatomic.nulecule.atomicappversion in atomicapp Dockerfile
2) LABEL io.projectatomic.nulecule.specversion  in app Dockefile
"""

__ATOMICAPPVERSION__ = '0.1.3'
__NULECULESPECVERSION__ = '0.0.2'

EXTERNAL_APP_DIR = "external"
ARTIFACTS_DIR = "artifacts" # Used as a destination when pulling remote artifact
GLOBAL_CONF = "general"
APP_ENT_PATH = "application-entity"

PARAMS_KEY = "params"
MAIN_FILE = "Nulecule"
ANSWERS_FILE = "answers.conf"
ANSWERS_FILE_SAMPLE = "answers.conf.sample"
ANSWERS_FILE_SAMPLE_FORMAT = 'ini'
WORKDIR = ".workdir"
LOCK_FILE = "/run/lock/atomicapp.lock"
HOST_DIR = "/host"

DEFAULT_PROVIDER = "kubernetes"
DEFAULT_NAMESPACE = "default"
DEFAULT_ANSWERS = {
    "general": {
        "provider": DEFAULT_PROVIDER,
        "namespace": DEFAULT_NAMESPACE
    }
}
