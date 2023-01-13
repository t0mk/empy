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
from empy.models.virtual_network import VirtualNetwork  # noqa: E501
from empy.rest import ApiException

class TestVirtualNetwork(unittest.TestCase):
    """VirtualNetwork unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VirtualNetwork
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VirtualNetwork`
        """
        model = empy.models.virtual_network.VirtualNetwork()  # noqa: E501
        if include_optional :
            return VirtualNetwork(
                assigned_to = {"href":"href"}, 
                assigned_to_virtual_circuit = True, 
                description = '', 
                facility = {"href":"href"}, 
                href = '', 
                id = '', 
                instances = [
                    {"href":"href"}
                    ], 
                metal_gateways = [
                    {"gateway_address":"10.1.2.1/27","updated_at":"2000-01-23 04:56:07+00:00","vlan":1001,"created_at":"2000-01-23 04:56:07+00:00","href":"href","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","state":"ready"}
                    ], 
                metro = {"href":"href"}, 
                metro_code = '', 
                vxlan = 56
            )
        else :
            return VirtualNetwork(
        )
        """

    def testVirtualNetwork(self):
        """Test VirtualNetwork"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
