# coding: utf-8

"""
    Autharmor

    Auth Armor - Auth Anywhere API

    The version of the OpenAPI document: v4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from autharmor_python.models.start_webauthn_auth_response import StartWebauthnAuthResponse  # noqa: E501

class TestStartWebauthnAuthResponse(unittest.TestCase):
    """StartWebauthnAuthResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StartWebauthnAuthResponse:
        """Test StartWebauthnAuthResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StartWebauthnAuthResponse`
        """
        model = StartWebauthnAuthResponse()  # noqa: E501
        if include_optional:
            return StartWebauthnAuthResponse(
                fido2_json_options = '',
                auth_request_id = '',
                aa_guid = ''
            )
        else:
            return StartWebauthnAuthResponse(
        )
        """

    def testStartWebauthnAuthResponse(self):
        """Test StartWebauthnAuthResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
