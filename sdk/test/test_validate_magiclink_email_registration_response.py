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

from autharmor_python.models.validate_magiclink_email_registration_response import ValidateMagiclinkEmailRegistrationResponse  # noqa: E501

class TestValidateMagiclinkEmailRegistrationResponse(unittest.TestCase):
    """ValidateMagiclinkEmailRegistrationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidateMagiclinkEmailRegistrationResponse:
        """Test ValidateMagiclinkEmailRegistrationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidateMagiclinkEmailRegistrationResponse`
        """
        model = ValidateMagiclinkEmailRegistrationResponse()  # noqa: E501
        if include_optional:
            return ValidateMagiclinkEmailRegistrationResponse(
                magiclink_email_registration_type = 'new_user',
                user_id = '',
                username = '',
                email_address = '',
                context_data = {
                    'key' : ''
                    }
            )
        else:
            return ValidateMagiclinkEmailRegistrationResponse(
        )
        """

    def testValidateMagiclinkEmailRegistrationResponse(self):
        """Test ValidateMagiclinkEmailRegistrationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()