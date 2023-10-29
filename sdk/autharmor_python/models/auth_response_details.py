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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from autharmor_python.models.auth_profile_details import AuthProfileDetails
from autharmor_python.models.mobile_device_details import MobileDeviceDetails
from autharmor_python.models.response_auth_method import ResponseAuthMethod
from autharmor_python.models.secure_signed_message import SecureSignedMessage

class AuthResponseDetails(BaseModel):
    """
    AuthResponseDetails
    """
    var_date: Optional[datetime] = Field(None, alias="date")
    auth_method: Optional[ResponseAuthMethod] = None
    secure_signed_message: Optional[SecureSignedMessage] = None
    mobile_device_details: Optional[MobileDeviceDetails] = None
    auth_profile_details: Optional[AuthProfileDetails] = None
    __properties = ["date", "auth_method", "secure_signed_message", "mobile_device_details", "auth_profile_details"]

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
    def from_json(cls, json_str: str) -> AuthResponseDetails:
        """Create an instance of AuthResponseDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of auth_method
        if self.auth_method:
            _dict['auth_method'] = self.auth_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of secure_signed_message
        if self.secure_signed_message:
            _dict['secure_signed_message'] = self.secure_signed_message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mobile_device_details
        if self.mobile_device_details:
            _dict['mobile_device_details'] = self.mobile_device_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auth_profile_details
        if self.auth_profile_details:
            _dict['auth_profile_details'] = self.auth_profile_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthResponseDetails:
        """Create an instance of AuthResponseDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthResponseDetails.parse_obj(obj)

        _obj = AuthResponseDetails.parse_obj({
            "var_date": obj.get("date"),
            "auth_method": ResponseAuthMethod.from_dict(obj.get("auth_method")) if obj.get("auth_method") is not None else None,
            "secure_signed_message": SecureSignedMessage.from_dict(obj.get("secure_signed_message")) if obj.get("secure_signed_message") is not None else None,
            "mobile_device_details": MobileDeviceDetails.from_dict(obj.get("mobile_device_details")) if obj.get("mobile_device_details") is not None else None,
            "auth_profile_details": AuthProfileDetails.from_dict(obj.get("auth_profile_details")) if obj.get("auth_profile_details") is not None else None
        })
        return _obj

