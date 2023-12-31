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


from typing import List, Optional
from pydantic import BaseModel, conlist
from autharmor_python.models.get_auth_request_response import GetAuthRequestResponse
from autharmor_python.models.user_auth_history_page_info import UserAuthHistoryPageInfo

class GetUserAuthHistoryResponse(BaseModel):
    """
    GetUserAuthHistoryResponse
    """
    auth_history_records: Optional[conlist(GetAuthRequestResponse)] = None
    page_info: Optional[UserAuthHistoryPageInfo] = None
    __properties = ["auth_history_records", "page_info"]

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
    def from_json(cls, json_str: str) -> GetUserAuthHistoryResponse:
        """Create an instance of GetUserAuthHistoryResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in auth_history_records (list)
        _items = []
        if self.auth_history_records:
            for _item in self.auth_history_records:
                if _item:
                    _items.append(_item.to_dict())
            _dict['auth_history_records'] = _items
        # override the default output from pydantic by calling `to_dict()` of page_info
        if self.page_info:
            _dict['page_info'] = self.page_info.to_dict()
        # set to None if auth_history_records (nullable) is None
        # and __fields_set__ contains the field
        if self.auth_history_records is None and "auth_history_records" in self.__fields_set__:
            _dict['auth_history_records'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetUserAuthHistoryResponse:
        """Create an instance of GetUserAuthHistoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetUserAuthHistoryResponse.parse_obj(obj)

        _obj = GetUserAuthHistoryResponse.parse_obj({
            "auth_history_records": [GetAuthRequestResponse.from_dict(_item) for _item in obj.get("auth_history_records")] if obj.get("auth_history_records") is not None else None,
            "page_info": UserAuthHistoryPageInfo.from_dict(obj.get("page_info")) if obj.get("page_info") is not None else None
        })
        return _obj


