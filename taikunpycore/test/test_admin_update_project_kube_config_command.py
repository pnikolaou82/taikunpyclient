# coding: utf-8

"""
    Taikun - WebApi

    This Api will be responsible for overall data distribution and authorization.

    The version of the OpenAPI document: v1
    Contact: noreply@taikun.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from taikunpycore.models.admin_update_project_kube_config_command import AdminUpdateProjectKubeConfigCommand

class TestAdminUpdateProjectKubeConfigCommand(unittest.TestCase):
    """AdminUpdateProjectKubeConfigCommand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdminUpdateProjectKubeConfigCommand:
        """Test AdminUpdateProjectKubeConfigCommand
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdminUpdateProjectKubeConfigCommand`
        """
        model = AdminUpdateProjectKubeConfigCommand()
        if include_optional:
            return AdminUpdateProjectKubeConfigCommand(
                project_id = 56
            )
        else:
            return AdminUpdateProjectKubeConfigCommand(
        )
        """

    def testAdminUpdateProjectKubeConfigCommand(self):
        """Test AdminUpdateProjectKubeConfigCommand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
