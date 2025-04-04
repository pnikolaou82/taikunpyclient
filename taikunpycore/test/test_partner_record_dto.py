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

from taikunpycore.models.partner_record_dto import PartnerRecordDto

class TestPartnerRecordDto(unittest.TestCase):
    """PartnerRecordDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PartnerRecordDto:
        """Test PartnerRecordDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PartnerRecordDto`
        """
        model = PartnerRecordDto()
        if include_optional:
            return PartnerRecordDto(
                id = 56,
                logo_url = '',
                background_image_url = '',
                payment_enabled = True,
                allow_registration = True,
                partner_color_settings = taikunpycore.models.partner_color_settings_dto.PartnerColorSettingsDto(
                    bg = '', 
                    bg_collapsed_sub_item = '', 
                    item_text = '', 
                    item_bg = '', 
                    item_bg_hover = '', 
                    item_text_active = '', 
                    item_bg_active = '', 
                    item_bg_active_hover = '', ),
                partner_image_settings = taikunpycore.models.partner_image_settings_dto.PartnerImageSettingsDto(
                    expanded = '', 
                    collapsed = '', )
            )
        else:
            return PartnerRecordDto(
                id = 56,
                logo_url = '',
                background_image_url = '',
                payment_enabled = True,
                allow_registration = True,
        )
        """

    def testPartnerRecordDto(self):
        """Test PartnerRecordDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
