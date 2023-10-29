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

from autharmor_python.models.finish_add_webauthn_to_user_request import FinishAddWebauthnToUserRequest  # noqa: E501

class TestFinishAddWebauthnToUserRequest(unittest.TestCase):
    """FinishAddWebauthnToUserRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FinishAddWebauthnToUserRequest:
        """Test FinishAddWebauthnToUserRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FinishAddWebauthnToUserRequest`
        """
        model = FinishAddWebauthnToUserRequest()  # noqa: E501
        if include_optional:
            return FinishAddWebauthnToUserRequest(
                aa_sig = '0',
                authenticator_response_data = autharmor_python.models.fido2_registration_data.fido2_registration_data(
                    id = '', 
                    attestation_object = '', 
                    client_data = '', ),
                webauthn_client_id = ''
            )
        else:
            return FinishAddWebauthnToUserRequest(
                aa_sig = '0',
                authenticator_response_data = autharmor_python.models.fido2_registration_data.fido2_registration_data(
                    id = '', 
                    attestation_object = '', 
                    client_data = '', ),
        )
        """

    def testFinishAddWebauthnToUserRequest(self):
        """Test FinishAddWebauthnToUserRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()