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

from taikunpycore.api.standalone_profile_api import StandaloneProfileApi


class TestStandaloneProfileApi(unittest.TestCase):
    """StandaloneProfileApi unit test stubs"""

    def setUp(self) -> None:
        self.api = StandaloneProfileApi()

    def tearDown(self) -> None:
        pass

    def test_standaloneprofile_create(self) -> None:
        """Test case for standaloneprofile_create

        Create standalone profile.
        """
        pass

    def test_standaloneprofile_delete(self) -> None:
        """Test case for standaloneprofile_delete

        Delete standalone profile.
        """
        pass

    def test_standaloneprofile_dropdown(self) -> None:
        """Test case for standaloneprofile_dropdown

        Retrieve all standalone profiles for organization
        """
        pass

    def test_standaloneprofile_edit(self) -> None:
        """Test case for standaloneprofile_edit

        Edit standalone profile.
        """
        pass

    def test_standaloneprofile_list(self) -> None:
        """Test case for standaloneprofile_list

        Retrieve all standalone profiles
        """
        pass

    def test_standaloneprofile_lock_management(self) -> None:
        """Test case for standaloneprofile_lock_management

        Lock/unlock standalone profile.
        """
        pass


if __name__ == '__main__':
    unittest.main()
