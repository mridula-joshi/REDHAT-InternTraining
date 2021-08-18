mport unittest
from unittest import mock
from unittest.mock import patch

from requests.exceptions import InvalidURL
from requests.exceptions import ConnectTimeout as Timeout
from argparse import ArgumentTypeError

import communicate_openstack
from communicate_openstack import CommunicateWithApi

class TestCommunicateWthApi(unittest.TestCase):
    def _make_args(self, args):
        class Args(object):
            def __init__(self, entries):
                self.__dict__.update(entries)

        return Args(args)

    def _base_request(self, method):
        args = self._make_args({'method': method,
                                'endpoint': 'http://10.0.78.192/volume/v3/project_id',
                                'api': '/volumes/volume_id',
                                'token': 'aaabbb111223344'
                               })
        with patch.object(communicate_openstack.requests, 'request') as mock_requests:
            api = CommunicateWithApi()
            api.communicate_api(args)
            mock_requests.assert_called_with(method=args.method, url=args.endpoint+args.api, headers={'X-Auth-Token': args.token})

    def test_communicate_api_get(self):
        self._base_request('GET')

    def test_communicate_api_delete(self):
        self._base_request('DELETE')

    def test_communicate_api_invalidurl(self):
        args = self._make_args({'method': 'GET',
                                'endpoint': 'htp',
                                'api': 'volumesvolume_id',
                                'token': 'aaabbb111223344'
                               })
        with patch.object(communicate_openstack.requests, 'request') as mock_requests, patch.object(communicate_openstack.logger, 'error') as mock_logger:
            mock_requests.side_effect = InvalidURL
            api = CommunicateWithApi()
            api.communicate_api(args)
            mock_logger.assert_called_once_with("INVALID URL Error")

    def test_communicate_api_timeout(self):
        args = self._make_args({'method': 'GET'
                                'endpoint': 'http://10.0.78.192/volume/v3/project_id',
                                'api': 'volumes/volume_id',
                                'token': 'aaabbb111223344'
                               })
        with patch.object(communicate_openstack.requests, 'request') as mock_requests , patch.object(communicate_openstack.logger, 'error') as mock_logger:
            mock_requests.side_effect = Timeout
            api = CommunicateWithApi()
            api.communicate_api(args)
            mock_logger.assert_called_once_with("Connection Error")

    def test_endpoint(self):
        url = 'http://10.0.78.192/volume/v3/project_id'
        api = CommunicateWithApi()
        res = api.endpoint_check(url)
        assert res == url

    def test_endpoint_error(self):
        url = 'http://10.192/volume/v3/project_id'
        api = CommunicateWithApi()

        with self.assertRaises(ArgumentTypeError):
           api.endpoint_check(url)


if __name__ == '__main__':
    unittest.main()

