# coding: utf-8

"""
    Taikun - WebApi

    This Api will be responsible for overall data distribution and authorization.

    The version of the OpenAPI document: v1
    Contact: noreply@taikun.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from taikunpycore.models.partner_details_for_user_dto import PartnerDetailsForUserDto
from taikunpycore.models.project_dto import ProjectDto
from taikunpycore.models.user_role import UserRole
from typing import Optional, Set
from typing_extensions import Self

class UserForListDto(BaseModel):
    """
    UserForListDto
    """ # noqa: E501
    id: Optional[StrictStr]
    username: Optional[StrictStr]
    organization_name: Optional[StrictStr] = Field(alias="organizationName")
    has_customer_id: Optional[StrictBool] = Field(alias="hasCustomerId")
    has_payment_method: Optional[StrictBool] = Field(alias="hasPaymentMethod")
    organization_id: Optional[StrictInt] = Field(alias="organizationId")
    role: UserRole
    role_name: Optional[StrictStr] = Field(default=None, alias="roleName")
    email: Optional[StrictStr]
    display_name: Optional[StrictStr] = Field(alias="displayName")
    created_at: Optional[StrictStr] = Field(alias="createdAt")
    created: Optional[datetime] = None
    is_email_confirmed: Optional[StrictBool] = Field(alias="isEmailConfirmed")
    is_email_notification_enabled: Optional[StrictBool] = Field(alias="isEmailNotificationEnabled")
    is_forced_to_reset_password: Optional[StrictBool] = Field(alias="isForcedToResetPassword")
    is_csm: Optional[StrictBool] = Field(alias="isCsm")
    is_eligible_update_subscription: Optional[StrictBool] = Field(alias="isEligibleUpdateSubscription")
    is_locked: Optional[StrictBool] = Field(alias="isLocked")
    is_approved_by_partner: Optional[StrictBool] = Field(alias="isApprovedByPartner")
    owner: Optional[StrictBool]
    is_read_only: Optional[StrictBool] = Field(alias="isReadOnly")
    has_repo: Optional[StrictBool] = Field(alias="hasRepo")
    is_new_organization: Optional[StrictBool] = Field(alias="isNewOrganization")
    is2_fa_enabled: Optional[StrictBool] = Field(alias="is2FAEnabled")
    last_login_at: Optional[StrictStr] = Field(alias="lastLoginAt")
    bound_projects: List[ProjectDto] = Field(alias="boundProjects")
    partner: PartnerDetailsForUserDto
    __properties: ClassVar[List[str]] = ["id", "username", "organizationName", "hasCustomerId", "hasPaymentMethod", "organizationId", "role", "roleName", "email", "displayName", "createdAt", "created", "isEmailConfirmed", "isEmailNotificationEnabled", "isForcedToResetPassword", "isCsm", "isEligibleUpdateSubscription", "isLocked", "isApprovedByPartner", "owner", "isReadOnly", "hasRepo", "isNewOrganization", "is2FAEnabled", "lastLoginAt", "boundProjects", "partner"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UserForListDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in bound_projects (list)
        _items = []
        if self.bound_projects:
            for _item_bound_projects in self.bound_projects:
                if _item_bound_projects:
                    _items.append(_item_bound_projects.to_dict())
            _dict['boundProjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of partner
        if self.partner:
            _dict['partner'] = self.partner.to_dict()
        # set to None if role_name (nullable) is None
        # and model_fields_set contains the field
        if self.role_name is None and "role_name" in self.model_fields_set:
            _dict['roleName'] = None

        # set to None if created (nullable) is None
        # and model_fields_set contains the field
        if self.created is None and "created" in self.model_fields_set:
            _dict['created'] = None

        # set to None if last_login_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_login_at is None and "last_login_at" in self.model_fields_set:
            _dict['lastLoginAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserForListDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "username": obj.get("username"),
            "organizationName": obj.get("organizationName"),
            "hasCustomerId": obj.get("hasCustomerId"),
            "hasPaymentMethod": obj.get("hasPaymentMethod"),
            "organizationId": obj.get("organizationId"),
            "role": obj.get("role"),
            "roleName": obj.get("roleName"),
            "email": obj.get("email"),
            "displayName": obj.get("displayName"),
            "createdAt": obj.get("createdAt"),
            "created": obj.get("created"),
            "isEmailConfirmed": obj.get("isEmailConfirmed"),
            "isEmailNotificationEnabled": obj.get("isEmailNotificationEnabled"),
            "isForcedToResetPassword": obj.get("isForcedToResetPassword"),
            "isCsm": obj.get("isCsm"),
            "isEligibleUpdateSubscription": obj.get("isEligibleUpdateSubscription"),
            "isLocked": obj.get("isLocked"),
            "isApprovedByPartner": obj.get("isApprovedByPartner"),
            "owner": obj.get("owner"),
            "isReadOnly": obj.get("isReadOnly"),
            "hasRepo": obj.get("hasRepo"),
            "isNewOrganization": obj.get("isNewOrganization"),
            "is2FAEnabled": obj.get("is2FAEnabled"),
            "lastLoginAt": obj.get("lastLoginAt"),
            "boundProjects": [ProjectDto.from_dict(_item) for _item in obj["boundProjects"]] if obj.get("boundProjects") is not None else None,
            "partner": PartnerDetailsForUserDto.from_dict(obj["partner"]) if obj.get("partner") is not None else None
        })
        return _obj


