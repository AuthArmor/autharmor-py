# autharmor-python
Autharmor provides A Suite of Authentication and Authorization tools to enhance security and accelerate your business.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v4
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.autharmor.com/contact](https://www.autharmor.com/contact)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import autharmor_python
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import autharmor_python
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import autharmor_python
from autharmor_python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.autharmor.com
# See configuration.py for a list of all supported configuration parameters.
configuration = autharmor_python.Configuration(
    host = "https://api.autharmor.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]


# Enter a context with an instance of the API client
with autharmor_python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = autharmor_python.AuthInfoApi(api_client)
    auth_request_id = 'auth_request_id_example' # str | 

    try:
        #   Get Auth Info
        api_response = api_instance.v4_auth_auth_request_id_get(auth_request_id)
        print("The response of AuthInfoApi->v4_auth_auth_request_id_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthInfoApi->v4_auth_auth_request_id_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.autharmor.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthInfoApi* | [**v4_auth_auth_request_id_get**](docs/AuthInfoApi.md#v4_auth_auth_request_id_get) | **GET** /v4/auth/{auth_request_id} |   Get Auth Info
*AuthAuthenticatorApi* | [**v4_auth_authenticator_start_post**](docs/AuthAuthenticatorApi.md#v4_auth_authenticator_start_post) | **POST** /v4/auth/authenticator/start |   Start auth request using Authenticator
*AuthAuthenticatorApi* | [**v4_auth_authenticator_validate_post**](docs/AuthAuthenticatorApi.md#v4_auth_authenticator_validate_post) | **POST** /v4/auth/authenticator/validate |  Validate auth request for Auth Armor Authenticator
*AuthMagicLinkEmailApi* | [**v4_auth_magiclink_email_start_post**](docs/AuthMagicLinkEmailApi.md#v4_auth_magiclink_email_start_post) | **POST** /v4/auth/magiclink_email/start |   Start auth request using Maigclink Email
*AuthMagicLinkEmailApi* | [**v4_auth_magiclink_email_validate_post**](docs/AuthMagicLinkEmailApi.md#v4_auth_magiclink_email_validate_post) | **POST** /v4/auth/magiclink_email/validate |   Validate auth request for Magiclink Email
*AuthWebAuthnApi* | [**v4_auth_webauthn_finish_post**](docs/AuthWebAuthnApi.md#v4_auth_webauthn_finish_post) | **POST** /v4/auth/webauthn/finish |   Finish auth request using WebAuthn
*AuthWebAuthnApi* | [**v4_auth_webauthn_start_post**](docs/AuthWebAuthnApi.md#v4_auth_webauthn_start_post) | **POST** /v4/auth/webauthn/start |  Start auth request using Webauthn
*AuthWebAuthnApi* | [**v4_auth_webauthn_validate_post**](docs/AuthWebAuthnApi.md#v4_auth_webauthn_validate_post) | **POST** /v4/auth/webauthn/validate |   Validate auth request for WebAuthn
*UserRegistrationsAuthenticatorApi* | [**v4_users_registrations_authenticator_registration_id_validate_post**](docs/UserRegistrationsAuthenticatorApi.md#v4_users_registrations_authenticator_registration_id_validate_post) | **POST** /v4/users/registrations/authenticator/{registration_id}/validate |   Validate User Registration for Authenticator
*UserRegistrationsAuthenticatorApi* | [**v4_users_registrations_authenticator_start_post**](docs/UserRegistrationsAuthenticatorApi.md#v4_users_registrations_authenticator_start_post) | **POST** /v4/users/registrations/authenticator/start |   Start User Registration for Authenticator
*UserRegistrationsAuthenticatorApi* | [**v4_users_user_id_registrations_authenticator_start_post**](docs/UserRegistrationsAuthenticatorApi.md#v4_users_user_id_registrations_authenticator_start_post) | **POST** /v4/users/{user_id}/registrations/authenticator/start |   Start Authenticator Registration for existing user
*UserRegistrationsGetRegistrationInfoApi* | [**v4_users_registrations_registration_id_get**](docs/UserRegistrationsGetRegistrationInfoApi.md#v4_users_registrations_registration_id_get) | **GET** /v4/users/registrations/{registration_Id} |   Get Registration Info
*UserRegistrationsMagiclinkEmailApi* | [**v4_users_registrations_magiclink_email_registration_id_validate_post**](docs/UserRegistrationsMagiclinkEmailApi.md#v4_users_registrations_magiclink_email_registration_id_validate_post) | **POST** /v4/users/registrations/magiclink_email/{registration_id}/validate |   Validate MagicLink Registration Token
*UserRegistrationsMagiclinkEmailApi* | [**v4_users_registrations_magiclink_email_start_post**](docs/UserRegistrationsMagiclinkEmailApi.md#v4_users_registrations_magiclink_email_start_post) | **POST** /v4/users/registrations/magiclink_email/start |   Start User Registration for MagicLink
*UserRegistrationsMagiclinkEmailApi* | [**v4_users_user_id_magiclink_email_update_start_post**](docs/UserRegistrationsMagiclinkEmailApi.md#v4_users_user_id_magiclink_email_update_start_post) | **POST** /v4/users/{user_id}/magiclink_email/update/start |   Start Change Users Email Address
*UserRegistrationsMagiclinkEmailApi* | [**v4_users_user_id_registrations_magiclink_email_start_post**](docs/UserRegistrationsMagiclinkEmailApi.md#v4_users_user_id_registrations_magiclink_email_start_post) | **POST** /v4/users/{user_id}/registrations/magiclink_email/start |   Create Magiclink Email Record for existing user
*UserRegistrationsWebAuthnApi* | [**v4_users_registrations_webauthn_registration_id_finish_post**](docs/UserRegistrationsWebAuthnApi.md#v4_users_registrations_webauthn_registration_id_finish_post) | **POST** /v4/users/registrations/webauthn/{registration_id}/finish |   Finish WebAuthn Registration for new user
*UserRegistrationsWebAuthnApi* | [**v4_users_registrations_webauthn_registration_id_validate_post**](docs/UserRegistrationsWebAuthnApi.md#v4_users_registrations_webauthn_registration_id_validate_post) | **POST** /v4/users/registrations/webauthn/{registration_id}/validate |   Validate User Registration for WebAuthn
*UserRegistrationsWebAuthnApi* | [**v4_users_registrations_webauthn_start_post**](docs/UserRegistrationsWebAuthnApi.md#v4_users_registrations_webauthn_start_post) | **POST** /v4/users/registrations/webauthn/start |   Start WebAuthn Registration for new user
*UserRegistrationsWebAuthnApi* | [**v4_users_user_id_registrations_webauthn_registration_id_finish_post**](docs/UserRegistrationsWebAuthnApi.md#v4_users_user_id_registrations_webauthn_registration_id_finish_post) | **POST** /v4/users/{user_id}/registrations/webauthn/{registration_id}/finish |   Finish WebAuthn Registration for existing user
*UserRegistrationsWebAuthnApi* | [**v4_users_user_id_registrations_webauthn_start_post**](docs/UserRegistrationsWebAuthnApi.md#v4_users_user_id_registrations_webauthn_start_post) | **POST** /v4/users/{user_id}/registrations/webauthn/start |   Start WebAuthn Registration for existing user
*UsersApi* | [**v4_users_get**](docs/UsersApi.md#v4_users_get) | **GET** /v4/users |   Get Users
*UsersApi* | [**v4_users_user_id_auth_history_get**](docs/UsersApi.md#v4_users_user_id_auth_history_get) | **GET** /v4/users/{user_id}/auth_history |   Get Auth History for User
*UsersApi* | [**v4_users_user_id_get**](docs/UsersApi.md#v4_users_user_id_get) | **GET** /v4/users/{user_id} |   Get User By Id
*UsersApi* | [**v4_users_user_id_put**](docs/UsersApi.md#v4_users_user_id_put) | **PUT** /v4/users/{user_id} |   Update User
*UsersCredentialsApi* | [**v4_users_user_id_credentials_authenticator_get**](docs/UsersCredentialsApi.md#v4_users_user_id_credentials_authenticator_get) | **GET** /v4/users/{user_id}/credentials/authenticator |   Get Users Authenticator Credential list
*UsersCredentialsApi* | [**v4_users_user_id_credentials_credential_id_disable_post**](docs/UsersCredentialsApi.md#v4_users_user_id_credentials_credential_id_disable_post) | **POST** /v4/users/{user_id}/credentials/{credential_id}/disable |   Disable Users Credential by Id
*UsersCredentialsApi* | [**v4_users_user_id_credentials_credential_id_get**](docs/UsersCredentialsApi.md#v4_users_user_id_credentials_credential_id_get) | **GET** /v4/users/{user_id}/credentials/{credential_id} |   Get Users Credential by Credential ID
*UsersCredentialsApi* | [**v4_users_user_id_credentials_get**](docs/UsersCredentialsApi.md#v4_users_user_id_credentials_get) | **GET** /v4/users/{user_id}/credentials |   Get Users Credentials list
*UsersCredentialsApi* | [**v4_users_user_id_credentials_magiclink_email_get**](docs/UsersCredentialsApi.md#v4_users_user_id_credentials_magiclink_email_get) | **GET** /v4/users/{user_id}/credentials/magiclink_email |   Get Users Authenticator Credential list
*UsersCredentialsApi* | [**v4_users_user_id_credentials_webauthn_get**](docs/UsersCredentialsApi.md#v4_users_user_id_credentials_webauthn_get) | **GET** /v4/users/{user_id}/credentials/webauthn |   Get Users WebAuthn Device list
*AutharmorApi* | [**v4_auth_auth_request_id_get**](docs/AutharmorApi.md#v4_auth_auth_request_id_get) | **GET** /v4/auth/{auth_request_id} |   Get Auth Info
*AutharmorApi* | [**v4_auth_authenticator_start_post**](docs/AutharmorApi.md#v4_auth_authenticator_start_post) | **POST** /v4/auth/authenticator/start |   Start auth request using Authenticator
*AutharmorApi* | [**v4_auth_authenticator_validate_post**](docs/AutharmorApi.md#v4_auth_authenticator_validate_post) | **POST** /v4/auth/authenticator/validate |  Validate auth request for Auth Armor Authenticator
*AutharmorApi* | [**v4_auth_magiclink_email_start_post**](docs/AutharmorApi.md#v4_auth_magiclink_email_start_post) | **POST** /v4/auth/magiclink_email/start |   Start auth request using Maigclink Email
*AutharmorApi* | [**v4_auth_magiclink_email_validate_post**](docs/AutharmorApi.md#v4_auth_magiclink_email_validate_post) | **POST** /v4/auth/magiclink_email/validate |   Validate auth request for Magiclink Email
*AutharmorApi* | [**v4_auth_webauthn_finish_post**](docs/AutharmorApi.md#v4_auth_webauthn_finish_post) | **POST** /v4/auth/webauthn/finish |   Finish auth request using WebAuthn
*AutharmorApi* | [**v4_auth_webauthn_start_post**](docs/AutharmorApi.md#v4_auth_webauthn_start_post) | **POST** /v4/auth/webauthn/start |  Start auth request using Webauthn
*AutharmorApi* | [**v4_auth_webauthn_validate_post**](docs/AutharmorApi.md#v4_auth_webauthn_validate_post) | **POST** /v4/auth/webauthn/validate |   Validate auth request for WebAuthn
*AutharmorApi* | [**v4_users_get**](docs/AutharmorApi.md#v4_users_get) | **GET** /v4/users |   Get Users
*AutharmorApi* | [**v4_users_registrations_authenticator_registration_id_validate_post**](docs/AutharmorApi.md#v4_users_registrations_authenticator_registration_id_validate_post) | **POST** /v4/users/registrations/authenticator/{registration_id}/validate |   Validate User Registration for Authenticator
*AutharmorApi* | [**v4_users_registrations_authenticator_start_post**](docs/AutharmorApi.md#v4_users_registrations_authenticator_start_post) | **POST** /v4/users/registrations/authenticator/start |   Start User Registration for Authenticator
*AutharmorApi* | [**v4_users_registrations_magiclink_email_registration_id_validate_post**](docs/AutharmorApi.md#v4_users_registrations_magiclink_email_registration_id_validate_post) | **POST** /v4/users/registrations/magiclink_email/{registration_id}/validate |   Validate MagicLink Registration Token
*AutharmorApi* | [**v4_users_registrations_magiclink_email_start_post**](docs/AutharmorApi.md#v4_users_registrations_magiclink_email_start_post) | **POST** /v4/users/registrations/magiclink_email/start |   Start User Registration for MagicLink
*AutharmorApi* | [**v4_users_registrations_registration_id_get**](docs/AutharmorApi.md#v4_users_registrations_registration_id_get) | **GET** /v4/users/registrations/{registration_Id} |   Get Registration Info
*AutharmorApi* | [**v4_users_registrations_webauthn_registration_id_finish_post**](docs/AutharmorApi.md#v4_users_registrations_webauthn_registration_id_finish_post) | **POST** /v4/users/registrations/webauthn/{registration_id}/finish |   Finish WebAuthn Registration for new user
*AutharmorApi* | [**v4_users_registrations_webauthn_registration_id_validate_post**](docs/AutharmorApi.md#v4_users_registrations_webauthn_registration_id_validate_post) | **POST** /v4/users/registrations/webauthn/{registration_id}/validate |   Validate User Registration for WebAuthn
*AutharmorApi* | [**v4_users_registrations_webauthn_start_post**](docs/AutharmorApi.md#v4_users_registrations_webauthn_start_post) | **POST** /v4/users/registrations/webauthn/start |   Start WebAuthn Registration for new user
*AutharmorApi* | [**v4_users_user_id_auth_history_get**](docs/AutharmorApi.md#v4_users_user_id_auth_history_get) | **GET** /v4/users/{user_id}/auth_history |   Get Auth History for User
*AutharmorApi* | [**v4_users_user_id_credentials_authenticator_get**](docs/AutharmorApi.md#v4_users_user_id_credentials_authenticator_get) | **GET** /v4/users/{user_id}/credentials/authenticator |   Get Users Authenticator Credential list
*AutharmorApi* | [**v4_users_user_id_credentials_credential_id_disable_post**](docs/AutharmorApi.md#v4_users_user_id_credentials_credential_id_disable_post) | **POST** /v4/users/{user_id}/credentials/{credential_id}/disable |   Disable Users Credential by Id
*AutharmorApi* | [**v4_users_user_id_credentials_credential_id_get**](docs/AutharmorApi.md#v4_users_user_id_credentials_credential_id_get) | **GET** /v4/users/{user_id}/credentials/{credential_id} |   Get Users Credential by Credential ID
*AutharmorApi* | [**v4_users_user_id_credentials_get**](docs/AutharmorApi.md#v4_users_user_id_credentials_get) | **GET** /v4/users/{user_id}/credentials |   Get Users Credentials list
*AutharmorApi* | [**v4_users_user_id_credentials_magiclink_email_get**](docs/AutharmorApi.md#v4_users_user_id_credentials_magiclink_email_get) | **GET** /v4/users/{user_id}/credentials/magiclink_email |   Get Users Authenticator Credential list
*AutharmorApi* | [**v4_users_user_id_credentials_webauthn_get**](docs/AutharmorApi.md#v4_users_user_id_credentials_webauthn_get) | **GET** /v4/users/{user_id}/credentials/webauthn |   Get Users WebAuthn Device list
*AutharmorApi* | [**v4_users_user_id_get**](docs/AutharmorApi.md#v4_users_user_id_get) | **GET** /v4/users/{user_id} |   Get User By Id
*AutharmorApi* | [**v4_users_user_id_magiclink_email_update_start_post**](docs/AutharmorApi.md#v4_users_user_id_magiclink_email_update_start_post) | **POST** /v4/users/{user_id}/magiclink_email/update/start |   Start Change Users Email Address
*AutharmorApi* | [**v4_users_user_id_put**](docs/AutharmorApi.md#v4_users_user_id_put) | **PUT** /v4/users/{user_id} |   Update User
*AutharmorApi* | [**v4_users_user_id_registrations_authenticator_start_post**](docs/AutharmorApi.md#v4_users_user_id_registrations_authenticator_start_post) | **POST** /v4/users/{user_id}/registrations/authenticator/start |   Start Authenticator Registration for existing user
*AutharmorApi* | [**v4_users_user_id_registrations_magiclink_email_start_post**](docs/AutharmorApi.md#v4_users_user_id_registrations_magiclink_email_start_post) | **POST** /v4/users/{user_id}/registrations/magiclink_email/start |   Create Magiclink Email Record for existing user
*AutharmorApi* | [**v4_users_user_id_registrations_webauthn_registration_id_finish_post**](docs/AutharmorApi.md#v4_users_user_id_registrations_webauthn_registration_id_finish_post) | **POST** /v4/users/{user_id}/registrations/webauthn/{registration_id}/finish |   Finish WebAuthn Registration for existing user
*AutharmorApi* | [**v4_users_user_id_registrations_webauthn_start_post**](docs/AutharmorApi.md#v4_users_user_id_registrations_webauthn_start_post) | **POST** /v4/users/{user_id}/registrations/webauthn/start |   Start WebAuthn Registration for existing user


## Documentation For Models

 - [AuthDetails](docs/AuthDetails.md)
 - [AuthMethodUseTypeResponse](docs/AuthMethodUseTypeResponse.md)
 - [AuthMethods](docs/AuthMethods.md)
 - [AuthProfileDetails](docs/AuthProfileDetails.md)
 - [AuthResponse](docs/AuthResponse.md)
 - [AuthResponseDetails](docs/AuthResponseDetails.md)
 - [AuthenticatorAttachmentType](docs/AuthenticatorAttachmentType.md)
 - [Credential](docs/Credential.md)
 - [CredentialType](docs/CredentialType.md)
 - [EnrolledAuthMethod](docs/EnrolledAuthMethod.md)
 - [Fido2RegistrationData](docs/Fido2RegistrationData.md)
 - [FinishAddWebauthnToUserRequest](docs/FinishAddWebauthnToUserRequest.md)
 - [FinishAddWebauthnToUserResponse](docs/FinishAddWebauthnToUserResponse.md)
 - [FinishNewWebauthnUserRegistrationRequest](docs/FinishNewWebauthnUserRegistrationRequest.md)
 - [FinishNewWebauthnUserRegistrationResponse](docs/FinishNewWebauthnUserRegistrationResponse.md)
 - [FinishWebauthnAuthRequest](docs/FinishWebauthnAuthRequest.md)
 - [FinishWebauthnAuthResponse](docs/FinishWebauthnAuthResponse.md)
 - [GetAuthRequestResponse](docs/GetAuthRequestResponse.md)
 - [GetRegistrationInfoResponse](docs/GetRegistrationInfoResponse.md)
 - [GetUserAuthHistoryResponse](docs/GetUserAuthHistoryResponse.md)
 - [GetUserCredentialsResponse](docs/GetUserCredentialsResponse.md)
 - [GetUserResponse](docs/GetUserResponse.md)
 - [GetUsersResponse](docs/GetUsersResponse.md)
 - [HashTypes](docs/HashTypes.md)
 - [LocationData](docs/LocationData.md)
 - [MagiclinkEmailRegistrationType](docs/MagiclinkEmailRegistrationType.md)
 - [MobileDeviceDetails](docs/MobileDeviceDetails.md)
 - [RequestDetails](docs/RequestDetails.md)
 - [ResidentKeyRequirementType](docs/ResidentKeyRequirementType.md)
 - [ResponseAuthMethod](docs/ResponseAuthMethod.md)
 - [SecureSignedMessage](docs/SecureSignedMessage.md)
 - [SignatureData](docs/SignatureData.md)
 - [SignedMessageType](docs/SignedMessageType.md)
 - [SigningMethod](docs/SigningMethod.md)
 - [StartAddWebauthnToUserRequest](docs/StartAddWebauthnToUserRequest.md)
 - [StartAddWebauthnToUserResponse](docs/StartAddWebauthnToUserResponse.md)
 - [StartAutharmorAutenticatorRegistrationNewUserRequest](docs/StartAutharmorAutenticatorRegistrationNewUserRequest.md)
 - [StartAutharmorAuthenticatorRegistrationForUserResponse](docs/StartAutharmorAuthenticatorRegistrationForUserResponse.md)
 - [StartAutharmorAuthenticatorRegistrationNewUserResponse](docs/StartAutharmorAuthenticatorRegistrationNewUserResponse.md)
 - [StartAuthenticatorAuthRequest](docs/StartAuthenticatorAuthRequest.md)
 - [StartAuthenticatorAuthResponse](docs/StartAuthenticatorAuthResponse.md)
 - [StartChangeMagiclinkEmailRegistrationRequest](docs/StartChangeMagiclinkEmailRegistrationRequest.md)
 - [StartChangeMagiclinkEmailRegistrationResponse](docs/StartChangeMagiclinkEmailRegistrationResponse.md)
 - [StartMagiclinkEmailAuthRequest](docs/StartMagiclinkEmailAuthRequest.md)
 - [StartMagiclinkEmailAuthResponse](docs/StartMagiclinkEmailAuthResponse.md)
 - [StartMagiclinkEmailRegistrationRequest](docs/StartMagiclinkEmailRegistrationRequest.md)
 - [StartMagiclinkEmailRegistrationResponse](docs/StartMagiclinkEmailRegistrationResponse.md)
 - [StartNewWebauthnUserRegistrationRequest](docs/StartNewWebauthnUserRegistrationRequest.md)
 - [StartNewWebauthnUserRegistrationResponse](docs/StartNewWebauthnUserRegistrationResponse.md)
 - [StartWebauthnAuthRequest](docs/StartWebauthnAuthRequest.md)
 - [StartWebauthnAuthResponse](docs/StartWebauthnAuthResponse.md)
 - [UpdateUserRequest](docs/UpdateUserRequest.md)
 - [User](docs/User.md)
 - [UserAuthHistoryPageInfo](docs/UserAuthHistoryPageInfo.md)
 - [UserVerificationRequirementType](docs/UserVerificationRequirementType.md)
 - [UsersCredentialsResponsePageInfo](docs/UsersCredentialsResponsePageInfo.md)
 - [UsersResponsePageInfo](docs/UsersResponsePageInfo.md)
 - [ValidateAuthResponse](docs/ValidateAuthResponse.md)
 - [ValidateAuthResponseDetails](docs/ValidateAuthResponseDetails.md)
 - [ValidateAutharmorAutenticatorRegistrationRequest](docs/ValidateAutharmorAutenticatorRegistrationRequest.md)
 - [ValidateAutharmorAutenticatorRegistrationResponse](docs/ValidateAutharmorAutenticatorRegistrationResponse.md)
 - [ValidateAutharmorAuthenticatorAuthRequest](docs/ValidateAutharmorAuthenticatorAuthRequest.md)
 - [ValidateMagiclinkEmailAuthRequest](docs/ValidateMagiclinkEmailAuthRequest.md)
 - [ValidateMagiclinkEmailRegistrationRequest](docs/ValidateMagiclinkEmailRegistrationRequest.md)
 - [ValidateMagiclinkEmailRegistrationResponse](docs/ValidateMagiclinkEmailRegistrationResponse.md)
 - [ValidateWebauthnAuthRequest](docs/ValidateWebauthnAuthRequest.md)
 - [ValidateWebauthnRegistrationRequest](docs/ValidateWebauthnRegistrationRequest.md)
 - [ValidateWebauthnRegistrationResponse](docs/ValidateWebauthnRegistrationResponse.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="oauth2"></a>
### oauth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **aarmor.api.request_auth**: Request Auth
 - **aarmor.api.generate_invite_code**: Generate Invite Code


## Author

support@autharmor.com


