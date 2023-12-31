# coding: utf-8

"""
    Autharmor

    Autharmor provides A Suite of Authentication and Authorization tools to enhance security and accelerate your business.

    The version of the OpenAPI document: v4
    Contact: support@autharmor.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from autharmor_python.models.start_add_webauthn_to_user_response import StartAddWebauthnToUserResponse  # noqa: E501

class TestStartAddWebauthnToUserResponse(unittest.TestCase):
    """StartAddWebauthnToUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StartAddWebauthnToUserResponse:
        """Test StartAddWebauthnToUserResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StartAddWebauthnToUserResponse`
        """
        model = StartAddWebauthnToUserResponse()  # noqa: E501
        if include_optional:
            return StartAddWebauthnToUserResponse(
                fido2_json_options = None,
                registration_id = '',
                aa_sig = '',
                user_id = ''
            )
        else:
            return StartAddWebauthnToUserResponse(
        )
        """

    def testStartAddWebauthnToUserResponse(self):
        """Test StartAddWebauthnToUserResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
