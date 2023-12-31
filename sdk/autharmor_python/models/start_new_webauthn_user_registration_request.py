# coding: utf-8

"""
    Autharmor

    Autharmor provides A Suite of Authentication and Authorization tools to enhance security and accelerate your business.

    The version of the OpenAPI document: v4
    Contact: support@autharmor.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt, StrictStr
from autharmor_python.models.authenticator_attachment_type import AuthenticatorAttachmentType
from autharmor_python.models.resident_key_requirement_type import ResidentKeyRequirementType
from autharmor_python.models.user_verification_requirement_type import UserVerificationRequirementType

class StartNewWebauthnUserRegistrationRequest(BaseModel):
    """
    StartNewWebauthnUserRegistrationRequest
    """
    username: Optional[StrictStr] = None
    email_address: Optional[StrictStr] = None
    timeout_in_seconds: Optional[StrictInt] = None
    webauthn_client_id: Optional[StrictStr] = None
    attachment_type: Optional[AuthenticatorAttachmentType] = None
    resident_key_requirement_type: Optional[ResidentKeyRequirementType] = None
    user_verification_requirement_type: Optional[UserVerificationRequirementType] = None
    __properties = ["username", "email_address", "timeout_in_seconds", "webauthn_client_id", "attachment_type", "resident_key_requirement_type", "user_verification_requirement_type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> StartNewWebauthnUserRegistrationRequest:
        """Create an instance of StartNewWebauthnUserRegistrationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if username (nullable) is None
        # and __fields_set__ contains the field
        if self.username is None and "username" in self.__fields_set__:
            _dict['username'] = None

        # set to None if email_address (nullable) is None
        # and __fields_set__ contains the field
        if self.email_address is None and "email_address" in self.__fields_set__:
            _dict['email_address'] = None

        # set to None if timeout_in_seconds (nullable) is None
        # and __fields_set__ contains the field
        if self.timeout_in_seconds is None and "timeout_in_seconds" in self.__fields_set__:
            _dict['timeout_in_seconds'] = None

        # set to None if webauthn_client_id (nullable) is None
        # and __fields_set__ contains the field
        if self.webauthn_client_id is None and "webauthn_client_id" in self.__fields_set__:
            _dict['webauthn_client_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StartNewWebauthnUserRegistrationRequest:
        """Create an instance of StartNewWebauthnUserRegistrationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StartNewWebauthnUserRegistrationRequest.parse_obj(obj)

        _obj = StartNewWebauthnUserRegistrationRequest.parse_obj({
            "username": obj.get("username"),
            "email_address": obj.get("email_address"),
            "timeout_in_seconds": obj.get("timeout_in_seconds"),
            "webauthn_client_id": obj.get("webauthn_client_id"),
            "attachment_type": obj.get("attachment_type"),
            "resident_key_requirement_type": obj.get("resident_key_requirement_type"),
            "user_verification_requirement_type": obj.get("user_verification_requirement_type")
        })
        return _obj


