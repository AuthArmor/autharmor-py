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
from pydantic import BaseModel, StrictInt, StrictStr

class StartMagiclinkEmailAuthResponse(BaseModel):
    """
    StartMagiclinkEmailAuthResponse
    """
    auth_request_id: Optional[StrictStr] = None
    user_id: Optional[StrictStr] = None
    timeout_in_seconds: Optional[StrictInt] = None
    timeout_utc_datetime: Optional[datetime] = None
    __properties = ["auth_request_id", "user_id", "timeout_in_seconds", "timeout_utc_datetime"]

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
    def from_json(cls, json_str: str) -> StartMagiclinkEmailAuthResponse:
        """Create an instance of StartMagiclinkEmailAuthResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StartMagiclinkEmailAuthResponse:
        """Create an instance of StartMagiclinkEmailAuthResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StartMagiclinkEmailAuthResponse.parse_obj(obj)

        _obj = StartMagiclinkEmailAuthResponse.parse_obj({
            "auth_request_id": obj.get("auth_request_id"),
            "user_id": obj.get("user_id"),
            "timeout_in_seconds": obj.get("timeout_in_seconds"),
            "timeout_utc_datetime": obj.get("timeout_utc_datetime")
        })
        return _obj

