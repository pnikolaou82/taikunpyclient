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

from taikunpycore.models.white_list_domain_dto import WhiteListDomainDto

class TestWhiteListDomainDto(unittest.TestCase):
    """WhiteListDomainDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WhiteListDomainDto:
        """Test WhiteListDomainDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WhiteListDomainDto`
        """
        model = WhiteListDomainDto()
        if include_optional:
            return WhiteListDomainDto(
                id = 56,
                name = ''
            )
        else:
            return WhiteListDomainDto(
                id = 56,
                name = '',
        )
        """

    def testWhiteListDomainDto(self):
        """Test WhiteListDomainDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
