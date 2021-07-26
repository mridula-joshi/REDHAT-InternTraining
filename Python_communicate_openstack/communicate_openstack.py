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

import argparse
import logging

import requests

from logging.handlers import RotatingFileHandler

format = logging.Formatter('% (asctime)s - % (name)s - % (levelname)s - % (message)s')
hdlr = RotatingFileHandler(filename='opstck.log',
                           maxBytes=2000,
                           backupCount=10)
hdlr.setFormatter(format)


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(hdlr)


class Communicate_with_api:
        def communicate_api(self, args):
                try:
                        url1 = args.endpoint + args.api
                        response = requests.request(method=args.method,
                                                    url=url1,
                                                    headers={"X-Auth-Token":
                                                             args.token})
                except request.exceptions.InvalidURL:
                        logger.error("INVALID URL Error")
                except request.exceptions.ConnectTimeout:
                        logger.error("Connection Error")
                except request.exceptions.HTTPError:
                        logger.error("HTTP Error")
                except Exception as e:
                        logger.warning("Exception %s", e)
                print(resonse.status_code)
                print(response.headers)
                print(response.text)

        def endpoint_check(self, url):
            regex = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
                    "2[0-4][0-9]|25[0-5])\\.){3}"\
                    "([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
                    "2[0-4][0-9]|25[0-5])"
            pattern = re.compile(regex)

            if url:
                ip = re.search(pattern, url)
                if ip:
                    return url

            raise argparse.ArgumentTypeError("invalid endpoint")

        def main(self):
                parser = argparse.ArgumentParser()
                parser.add_argument("endpoint",
                                    type=self.endpoint_check
                                    help=" Endpoint Url")
                parser.add_argument("method",
                                    help=" HTTP request method",
                                    choices=['GET', 'DELETE'],
                                    type=str)
                parser.add_argument("api",
                                    help="api_ref")
                parser.add_argument("token",
                                    help="Authorized token")
                self.communicate_api(parser.parse_args())

if __name__ == "__main__":
        co = Communicate_with_api()
        co.main()
