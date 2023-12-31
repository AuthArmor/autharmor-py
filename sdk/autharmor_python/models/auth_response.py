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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from autharmor_python.models.auth_details import AuthDetails

class AuthResponse(BaseModel):
    """
    AuthResponse
    """
    auth_history_id: Optional[StrictStr] = None
    result_code: Optional[StrictInt] = None
    result_message: Optional[StrictStr] = None
    authorized: Optional[StrictBool] = None
    auth_details: Optional[AuthDetails] = None
    __properties = ["auth_history_id", "result_code", "result_message", "authorized", "auth_details"]

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
    def from_json(cls, json_str: str) -> AuthResponse:
        """Create an instance of AuthResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of auth_details
        if self.auth_details:
            _dict['auth_details'] = self.auth_details.to_dict()
        # set to None if result_message (nullable) is None
        # and __fields_set__ contains the field
        if self.result_message is None and "result_message" in self.__fields_set__:
            _dict['result_message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthResponse:
        """Create an instance of AuthResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthResponse.parse_obj(obj)

        _obj = AuthResponse.parse_obj({
            "auth_history_id": obj.get("auth_history_id"),
            "result_code": obj.get("result_code"),
            "result_message": obj.get("result_message"),
            "authorized": obj.get("authorized"),
            "auth_details": AuthDetails.from_dict(obj.get("auth_details")) if obj.get("auth_details") is not None else None
        })
        return _obj


