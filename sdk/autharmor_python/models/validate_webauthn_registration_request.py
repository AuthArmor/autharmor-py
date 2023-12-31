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
from pydantic import BaseModel, StrictStr

class ValidateWebauthnRegistrationRequest(BaseModel):
    """
    ValidateWebauthnRegistrationRequest
    """
    registration_validation_token: Optional[StrictStr] = None
    __properties = ["registration_validation_token"]

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
    def from_json(cls, json_str: str) -> ValidateWebauthnRegistrationRequest:
        """Create an instance of ValidateWebauthnRegistrationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if registration_validation_token (nullable) is None
        # and __fields_set__ contains the field
        if self.registration_validation_token is None and "registration_validation_token" in self.__fields_set__:
            _dict['registration_validation_token'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ValidateWebauthnRegistrationRequest:
        """Create an instance of ValidateWebauthnRegistrationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ValidateWebauthnRegistrationRequest.parse_obj(obj)

        _obj = ValidateWebauthnRegistrationRequest.parse_obj({
            "registration_validation_token": obj.get("registration_validation_token")
        })
        return _obj


