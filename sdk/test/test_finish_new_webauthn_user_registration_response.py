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

from autharmor_python.models.finish_new_webauthn_user_registration_response import FinishNewWebauthnUserRegistrationResponse  # noqa: E501

class TestFinishNewWebauthnUserRegistrationResponse(unittest.TestCase):
    """FinishNewWebauthnUserRegistrationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FinishNewWebauthnUserRegistrationResponse:
        """Test FinishNewWebauthnUserRegistrationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FinishNewWebauthnUserRegistrationResponse`
        """
        model = FinishNewWebauthnUserRegistrationResponse()  # noqa: E501
        if include_optional:
            return FinishNewWebauthnUserRegistrationResponse(
                registration_validation_token = '',
                user_id = '',
                username = ''
            )
        else:
            return FinishNewWebauthnUserRegistrationResponse(
        )
        """

    def testFinishNewWebauthnUserRegistrationResponse(self):
        """Test FinishNewWebauthnUserRegistrationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
