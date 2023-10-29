# coding: utf-8

"""
    Autharmor

    Autharmor provides A Suite of Authentication and Authorization tools to enhance security and accelerate your business.

    The version of the OpenAPI document: v4
    Contact: support@autharmor.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class CredentialType(str, Enum):
    """
    CredentialType
    """

    """
    allowed enum values
    """
    AUTHARMOR_AUTHENTICATOR = 'autharmor_authenticator'
    WEBAUTHN = 'webauthn'
    MAGICLINK_EMAIL = 'magiclink_email'

    @classmethod
    def from_json(cls, json_str: str) -> CredentialType:
        """Create an instance of CredentialType from a JSON string"""
        return CredentialType(json.loads(json_str))

