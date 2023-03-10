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
import datetime

import empy
from empy.models.operating_system import OperatingSystem  # noqa: E501
from empy.rest import ApiException

class TestOperatingSystem(unittest.TestCase):
    """OperatingSystem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OperatingSystem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OperatingSystem`
        """
        model = empy.models.operating_system.OperatingSystem()  # noqa: E501
        if include_optional :
            return OperatingSystem(
                distro = '', 
                id = '', 
                licensed = True, 
                name = '', 
                preinstallable = True, 
                pricing = None, 
                provisionable_on = [
                    ''
                    ], 
                slug = '', 
                version = '', 
                href = ''
            )
        else :
            return OperatingSystem(
        )
        """

    def testOperatingSystem(self):
        """Test OperatingSystem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
