# coding: utf-8

"""
    Autharmor

    Auth Armor - Auth Anywhere API

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, StrictInt

class UsersCredentialsResponsePageInfo(BaseModel):
    """
    UsersCredentialsResponsePageInfo
    """
    currnet_page_number: Optional[StrictInt] = None
    currnet_page_size: Optional[StrictInt] = None
    total_page_count: Optional[StrictInt] = None
    total_record_count: Optional[StrictInt] = None
    __properties = ["currnet_page_number", "currnet_page_size", "total_page_count", "total_record_count"]

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
    def from_json(cls, json_str: str) -> UsersCredentialsResponsePageInfo:
        """Create an instance of UsersCredentialsResponsePageInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UsersCredentialsResponsePageInfo:
        """Create an instance of UsersCredentialsResponsePageInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UsersCredentialsResponsePageInfo.parse_obj(obj)

        _obj = UsersCredentialsResponsePageInfo.parse_obj({
            "currnet_page_number": obj.get("currnet_page_number"),
            "currnet_page_size": obj.get("currnet_page_size"),
            "total_page_count": obj.get("total_page_count"),
            "total_record_count": obj.get("total_record_count")
        })
        return _obj


