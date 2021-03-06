# Copyright (c) 2016 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

__import__('pkg_resources').declare_namespace(__name__)

import os

os.environ['EVENTLET_NO_GREENDNS'] = 'yes'

# NOTE(rpodolyaka): import oslo_service first, so that it makes eventlet hub
# use a monotonic clock to avoid issues with drifts of system time (see
# LP 1510234 for details)
import oslo_service  # noqa

import eventlet  # noqa
