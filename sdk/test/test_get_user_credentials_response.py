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

from autharmor_python.models.get_user_credentials_response import GetUserCredentialsResponse  # noqa: E501

class TestGetUserCredentialsResponse(unittest.TestCase):
    """GetUserCredentialsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetUserCredentialsResponse:
        """Test GetUserCredentialsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetUserCredentialsResponse`
        """
        model = GetUserCredentialsResponse()  # noqa: E501
        if include_optional:
            return GetUserCredentialsResponse(
                credential_records = [
                    autharmor_python.models.credential.credential(
                        name = '', 
                        credential_id = '', 
                        date_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        device_type = 'autharmor_authenticator', 
                        enabled = True, )
                    ],
                page_info = autharmor_python.models.users_credentials_response_page_info.users_credentials_response_page_info(
                    currnet_page_number = 56, 
                    currnet_page_size = 56, 
                    total_page_count = 56, 
                    total_record_count = 56, )
            )
        else:
            return GetUserCredentialsResponse(
        )
        """

    def testGetUserCredentialsResponse(self):
        """Test GetUserCredentialsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
