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

from autharmor_python.models.validate_auth_response_details import ValidateAuthResponseDetails  # noqa: E501

class TestValidateAuthResponseDetails(unittest.TestCase):
    """ValidateAuthResponseDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidateAuthResponseDetails:
        """Test ValidateAuthResponseDetails
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidateAuthResponseDetails`
        """
        model = ValidateAuthResponseDetails()  # noqa: E501
        if include_optional:
            return ValidateAuthResponseDetails(
                auth_history_id = '',
                result_code = 56,
                result_message = '',
                authorized = True,
                auth_details = autharmor_python.models.auth_details.auth_details(
                    request_details = autharmor_python.models.request_details.request_details(
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        auth_profile_details = autharmor_python.models.auth_profile_details.auth_profile_details(
                            user_id = '', 
                            username = '', ), 
                        origin_location_data = autharmor_python.models.location_data.location_data(
                            latitude = '', 
                            longitude = '', 
                            ip_address = '', ), 
                        auth_method = 'MobileDevice', ), 
                    response_details = autharmor_python.models.auth_response_details.auth_response_details(
                        date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        secure_signed_message = autharmor_python.models.secure_signed_message.secure_signed_message(
                            signed_data = '', 
                            signature_data = autharmor_python.models.signature_data.signature_data(
                                hash_value = '', 
                                auth_method_usetype = 'biometric', 
                                signing_method = 'AuthArmor_ECDsa', 
                                hash_method = 'Sha256', ), 
                            signed_data_type = 'AuthResponse', 
                            signature_validation_details = null, ), 
                        mobile_device_details = autharmor_python.models.mobile_device_details.mobile_device_details(
                            platform = '', 
                            model = '', ), ), ),
                context_data = {
                    'key' : ''
                    }
            )
        else:
            return ValidateAuthResponseDetails(
        )
        """

    def testValidateAuthResponseDetails(self):
        """Test ValidateAuthResponseDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
