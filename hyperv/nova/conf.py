# Copyright 2017 Cloudbase Solutions Srl
# All Rights Reserved.
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

from oslo_config import cfg

import nova.conf

hyperv_opts = [
    cfg.IntOpt('evacuate_task_state_timeout',
               default=600,
               help='Number of seconds to wait for an instance to be '
                    'evacuated during host maintenance.'),
    cfg.IntOpt('cluster_event_check_interval',
               default=2),
    cfg.StrOpt('instance_automatic_shutdown',
               default=False,
               help='Automatically shutdown instances when the host is '
                    'shutdown. By default, instances will be saved, which '
                    'adds a disk overhead. Changing this option will not '
                    'affect existing instances.'),
]

CONF = nova.conf.CONF
CONF.register_opts(hyperv_opts, 'hyperv')
