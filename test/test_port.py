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
from empy.models.port import Port  # noqa: E501
from empy.rest import ApiException

class TestPort(unittest.TestCase):
    """Port unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Port
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Port`
        """
        model = empy.models.port.Port()  # noqa: E501
        if include_optional :
            return Port(
                bond = {"name":"name","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}, 
                data = {"bonded":True,"mac":"mac"}, 
                disbond_operation_supported = True, 
                href = '', 
                id = '', 
                name = 'bond0', 
                type = 'NetworkPort', 
                network_type = 'layer2-bonded', 
                native_virtual_network = {"vxlan":5,"metal_gateways":[{"gateway_address":"10.1.2.1/27","updated_at":"2000-01-23 04:56:07+00:00","vlan":1001,"created_at":"2000-01-23 04:56:07+00:00","href":"href","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","state":"ready"},{"gateway_address":"10.1.2.1/27","updated_at":"2000-01-23 04:56:07+00:00","vlan":1001,"created_at":"2000-01-23 04:56:07+00:00","href":"href","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","state":"ready"}],"metro_code":"metro_code","instances":[{"href":"href"},{"href":"href"}],"metro":{"href":"href"},"description":"description","href":"href","id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","facility":{"href":"href"},"assigned_to_virtual_circuit":True,"assigned_to":{"href":"href"}}, 
                virtual_networks = [
                    {"href":"href"}
                    ]
            )
        else :
            return Port(
        )
        """

    def testPort(self):
        """Test Port"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
