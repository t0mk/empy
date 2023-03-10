# coding: utf-8

"""
    Metal API

    desc  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import empy
from empy.api.devices_api import DevicesApi  # noqa: E501
from empy.rest import ApiException


class TestDevicesApi(unittest.TestCase):
    """DevicesApi unit test stubs"""

    def setUp(self):
        self.api = empy.api.devices_api.DevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_device(self):
        """Test case for create_device

        Create a device  # noqa: E501
        """
        pass

    def test_delete_device(self):
        """Test case for delete_device

        Delete the device  # noqa: E501
        """
        pass

    def test_find_device_by_id(self):
        """Test case for find_device_by_id

        Retrieve a device  # noqa: E501
        """
        pass

    def test_find_project_devices(self):
        """Test case for find_project_devices

        Retrieve all devices of a project  # noqa: E501
        """
        pass

    def test_update_device(self):
        """Test case for update_device

        Update the device  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
