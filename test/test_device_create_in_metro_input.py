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
from empy.models.device_create_in_metro_input import DeviceCreateInMetroInput  # noqa: E501
from empy.rest import ApiException

class TestDeviceCreateInMetroInput(unittest.TestCase):
    """DeviceCreateInMetroInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeviceCreateInMetroInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeviceCreateInMetroInput`
        """
        model = empy.models.device_create_in_metro_input.DeviceCreateInMetroInput()  # noqa: E501
        if include_optional :
            return DeviceCreateInMetroInput(
                metro = 'sv', 
                href = '', 
                always_pxe = True, 
                billing_cycle = 'hourly', 
                customdata = empy.models.customdata.customdata(), 
                description = '', 
                features = [
                    ''
                    ], 
                hardware_reservation_id = 'next-available', 
                hostname = '', 
                ip_addresses = [
                    empy.models.device_create_input_ip_addresses_inner.DeviceCreateInput_ip_addresses_inner(
                        address_family = 4, 
                        cidr = 28, 
                        ip_reservations = [
                            ''
                            ], 
                        public = False, 
                        href = '', )
                    ], 
                ipxe_script_url = '', 
                locked = True, 
                no_ssh_keys = True, 
                operating_system = '', 
                plan = 'c3.large.x86', 
                private_ipv4_subnet_size = 56, 
                project_ssh_keys = [
                    ''
                    ], 
                public_ipv4_subnet_size = 56, 
                spot_instance = True, 
                spot_price_max = 1.23, 
                ssh_keys = [
                    {"label":"label","key":"key"}
                    ], 
                tags = [
                    ''
                    ], 
                termination_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                user_ssh_keys = [
                    ''
                    ], 
                userdata = ''
            )
        else :
            return DeviceCreateInMetroInput(
                metro = 'sv',
                operating_system = '',
                plan = 'c3.large.x86',
        )
        """

    def testDeviceCreateInMetroInput(self):
        """Test DeviceCreateInMetroInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
