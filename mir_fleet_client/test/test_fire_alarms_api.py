"""
    2.13.5.3 FLEET REST API

    The REST API for the 2.13.5.3 interface of FLEET  # noqa: E501

    The version of the OpenAPI document: 2.13.5.3
    Contact: support@mir-robots.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import mir_fleet_client
from mir_fleet_client.api.fire_alarms_api import FireAlarmsApi  # noqa: E501


class TestFireAlarmsApi(unittest.TestCase):
    """FireAlarmsApi unit test stubs"""

    def setUp(self):
        self.api = FireAlarmsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_fire_alarms_get(self):
        """Test case for fire_alarms_get

        GET /fire_alarms  # noqa: E501
        """
        pass

    def test_fire_alarms_id_get(self):
        """Test case for fire_alarms_id_get

        GET /fire_alarms/{id}  # noqa: E501
        """
        pass

    def test_fire_alarms_id_put(self):
        """Test case for fire_alarms_id_put

        PUT /fire_alarms/{id}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()