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
from empy.models.project_update_input import ProjectUpdateInput  # noqa: E501
from empy.rest import ApiException

class TestProjectUpdateInput(unittest.TestCase):
    """ProjectUpdateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectUpdateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectUpdateInput`
        """
        model = empy.models.project_update_input.ProjectUpdateInput()  # noqa: E501
        if include_optional :
            return ProjectUpdateInput(
                backend_transfer_enabled = True, 
                customdata = None, 
                name = '', 
                payment_method_id = '', 
                href = ''
            )
        else :
            return ProjectUpdateInput(
        )
        """

    def testProjectUpdateInput(self):
        """Test ProjectUpdateInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
