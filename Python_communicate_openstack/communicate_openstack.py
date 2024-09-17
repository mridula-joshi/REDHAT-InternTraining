#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.
""" This will help to establish connection and communicate with the
    Openstack services using HTTP requests. """

import requests
from oslo_config import cfg
from oslo_log import log as logging


CONF = cfg.CONF

request_opts = [
    cfg.StrOpt('endpoint', required=True),
    cfg.StrOpt('method', choices=['GET', 'DELETE'], required=True),
    cfg.StrOpt('api', required=True),
    cfg.StrOpt('api_token', required='True')
]

CONF.register_opts(request_opts, group='api_requirements')


def prepare():
    logging.register_options(CONF)

    config_files = cfg.find_config_files(project='trainee_2021',
                                         prog='communicate_openstack_oslo')
    CONF(project='trainee_2021',
         default_config_files=config_files)
    logging.setup(CONF, 'trainee_2021')


class CommunicateWithApi:
    def communicate_api(self):
        try:
            request_url = CONF.api_requirements.endpoint + CONF.api_requirements.api
            respose = requests.request(method=CONF.api_requirements.method,
                                        url=request_url,
                                        headers={"X-Auth-Token":
                                                 CONF.api_requirements.api_token})
        except requests.exceptions.InvalidURL:
            LOG.error("INVALID URL Error: %s" %(request_url))
        except requests.exceptions.ConnectTimeout:
            LOG.error("Connection Error")
        except requests.exceptions.HTTPError:
            LOG.error("HTTP Error")
        except Exception as e:
            LOG.warning("Exception %s", e)
        LOG.debug(response.status_code)
        LOG.debug(response.headers)
        LOG.debug(response.text)

    def main(self):
        self.communicate_api()


if __name__ == "__main__":
    prepare()
    LOG = logging.getLogger(__name__)
    co = Communicate_with_api()
    co.main()
