# autharmor_python.AutharmorApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_auth_auth_request_id_get**](AutharmorApi.md#v4_auth_auth_request_id_get) | **GET** /v4/auth/{auth_request_id} |   Get Auth Info
[**v4_auth_authenticator_start_post**](AutharmorApi.md#v4_auth_authenticator_start_post) | **POST** /v4/auth/authenticator/start |   Start auth request using Authenticator
[**v4_auth_authenticator_validate_post**](AutharmorApi.md#v4_auth_authenticator_validate_post) | **POST** /v4/auth/authenticator/validate |  Validate auth request for Auth Armor Authenticator
[**v4_auth_magiclink_email_start_post**](AutharmorApi.md#v4_auth_magiclink_email_start_post) | **POST** /v4/auth/magiclink_email/start |   Start auth request using Maigclink Email
[**v4_auth_magiclink_email_validate_post**](AutharmorApi.md#v4_auth_magiclink_email_validate_post) | **POST** /v4/auth/magiclink_email/validate |   Validate auth request for Magiclink Email
[**v4_auth_webauthn_finish_post**](AutharmorApi.md#v4_auth_webauthn_finish_post) | **POST** /v4/auth/webauthn/finish |   Finish auth request using WebAuthn
[**v4_auth_webauthn_start_post**](AutharmorApi.md#v4_auth_webauthn_start_post) | **POST** /v4/auth/webauthn/start |  Start auth request using Webauthn
[**v4_auth_webauthn_validate_post**](AutharmorApi.md#v4_auth_webauthn_validate_post) | **POST** /v4/auth/webauthn/validate |   Validate auth request for WebAuthn
[**v4_users_get**](AutharmorApi.md#v4_users_get) | **GET** /v4/users |   Get Users
[**v4_users_registrations_authenticator_registration_id_validate_post**](AutharmorApi.md#v4_users_registrations_authenticator_registration_id_validate_post) | **POST** /v4/users/registrations/authenticator/{registration_id}/validate |   Validate User Registration for Authenticator
[**v4_users_registrations_authenticator_start_post**](AutharmorApi.md#v4_users_registrations_authenticator_start_post) | **POST** /v4/users/registrations/authenticator/start |   Start User Registration for Authenticator
[**v4_users_registrations_magiclink_email_registration_id_validate_post**](AutharmorApi.md#v4_users_registrations_magiclink_email_registration_id_validate_post) | **POST** /v4/users/registrations/magiclink_email/{registration_id}/validate |   Validate MagicLink Registration Token
[**v4_users_registrations_magiclink_email_start_post**](AutharmorApi.md#v4_users_registrations_magiclink_email_start_post) | **POST** /v4/users/registrations/magiclink_email/start |   Start User Registration for MagicLink
[**v4_users_registrations_registration_id_get**](AutharmorApi.md#v4_users_registrations_registration_id_get) | **GET** /v4/users/registrations/{registration_Id} |   Get Registration Info
[**v4_users_registrations_webauthn_registration_id_finish_post**](AutharmorApi.md#v4_users_registrations_webauthn_registration_id_finish_post) | **POST** /v4/users/registrations/webauthn/{registration_id}/finish |   Finish WebAuthn Registration for new user
[**v4_users_registrations_webauthn_registration_id_validate_post**](AutharmorApi.md#v4_users_registrations_webauthn_registration_id_validate_post) | **POST** /v4/users/registrations/webauthn/{registration_id}/validate |   Validate User Registration for WebAuthn
[**v4_users_registrations_webauthn_start_post**](AutharmorApi.md#v4_users_registrations_webauthn_start_post) | **POST** /v4/users/registrations/webauthn/start |   Start WebAuthn Registration for new user
[**v4_users_user_id_auth_history_get**](AutharmorApi.md#v4_users_user_id_auth_history_get) | **GET** /v4/users/{user_id}/auth_history |   Get Auth History for User
[**v4_users_user_id_credentials_authenticator_get**](AutharmorApi.md#v4_users_user_id_credentials_authenticator_get) | **GET** /v4/users/{user_id}/credentials/authenticator |   Get Users Authenticator Credential list
[**v4_users_user_id_credentials_credential_id_disable_post**](AutharmorApi.md#v4_users_user_id_credentials_credential_id_disable_post) | **POST** /v4/users/{user_id}/credentials/{credential_id}/disable |   Disable Users Credential by Id
[**v4_users_user_id_credentials_credential_id_get**](AutharmorApi.md#v4_users_user_id_credentials_credential_id_get) | **GET** /v4/users/{user_id}/credentials/{credential_id} |   Get Users Credential by Credential ID
[**v4_users_user_id_credentials_get**](AutharmorApi.md#v4_users_user_id_credentials_get) | **GET** /v4/users/{user_id}/credentials |   Get Users Credentials list
[**v4_users_user_id_credentials_magiclink_email_get**](AutharmorApi.md#v4_users_user_id_credentials_magiclink_email_get) | **GET** /v4/users/{user_id}/credentials/magiclink_email |   Get Users Authenticator Credential list
[**v4_users_user_id_credentials_webauthn_get**](AutharmorApi.md#v4_users_user_id_credentials_webauthn_get) | **GET** /v4/users/{user_id}/credentials/webauthn |   Get Users WebAuthn Device list
[**v4_users_user_id_get**](AutharmorApi.md#v4_users_user_id_get) | **GET** /v4/users/{user_id} |   Get User By Id
[**v4_users_user_id_magiclink_email_update_start_post**](AutharmorApi.md#v4_users_user_id_magiclink_email_update_start_post) | **POST** /v4/users/{user_id}/magiclink_email/update/start |   Start Change Users Email Address
[**v4_users_user_id_put**](AutharmorApi.md#v4_users_user_id_put) | **PUT** /v4/users/{user_id} |   Update User
[**v4_users_user_id_registrations_authenticator_start_post**](AutharmorApi.md#v4_users_user_id_registrations_authenticator_start_post) | **POST** /v4/users/{user_id}/registrations/authenticator/start |   Start Authenticator Registration for existing user
[**v4_users_user_id_registrations_magiclink_email_start_post**](AutharmorApi.md#v4_users_user_id_registrations_magiclink_email_start_post) | **POST** /v4/users/{user_id}/registrations/magiclink_email/start |   Create Magiclink Email Record for existing user
[**v4_users_user_id_registrations_webauthn_registration_id_finish_post**](AutharmorApi.md#v4_users_user_id_registrations_webauthn_registration_id_finish_post) | **POST** /v4/users/{user_id}/registrations/webauthn/{registration_id}/finish |   Finish WebAuthn Registration for existing user
[**v4_users_user_id_registrations_webauthn_start_post**](AutharmorApi.md#v4_users_user_id_registrations_webauthn_start_post) | **POST** /v4/users/{user_id}/registrations/webauthn/start |   Start WebAuthn Registration for existing user


# **v4_auth_auth_request_id_get**
> GetAuthRequestResponse v4_auth_auth_request_id_get(auth_request_id)

  Get Auth Info

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.get_auth_request_response import GetAuthRequestResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    auth_request_id = 'auth_request_id_example' # str | 

    try:
        #   Get Auth Info
        api_response = api_instance.v4_auth_auth_request_id_get(auth_request_id)
        print("The response of AutharmorApi->v4_auth_auth_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_auth_auth_request_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request_id** | **str**|  | 

### Return type

[**GetAuthRequestResponse**](GetAuthRequestResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_auth_authenticator_start_post**
> StartAuthenticatorAuthResponse v4_auth_authenticator_start_post(start_authenticator_auth_request=start_authenticator_auth_request)

  Start auth request using Authenticator

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_authenticator_auth_request import StartAuthenticatorAuthRequest
from autharmor_python.models.start_authenticator_auth_response import StartAuthenticatorAuthResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    start_authenticator_auth_request = autharmor_python.StartAuthenticatorAuthRequest() # StartAuthenticatorAuthRequest |  (optional)

    try:
        #   Start auth request using Authenticator
        api_response = api_instance.v4_auth_authenticator_start_post(start_authenticator_auth_request=start_authenticator_auth_request)
        print("The response of AutharmorApi->v4_auth_authenticator_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_auth_authenticator_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_authenticator_auth_request** | [**StartAuthenticatorAuthRequest**](StartAuthenticatorAuthRequest.md)|  | [optional] 

### Return type

[**StartAuthenticatorAuthResponse**](StartAuthenticatorAuthResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_auth_authenticator_validate_post**
> ValidateAuthResponse v4_auth_authenticator_validate_post(validate_autharmor_authenticator_auth_request=validate_autharmor_authenticator_auth_request)

 Validate auth request for Auth Armor Authenticator

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.validate_auth_response import ValidateAuthResponse
from autharmor_python.models.validate_autharmor_authenticator_auth_request import ValidateAutharmorAuthenticatorAuthRequest
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    validate_autharmor_authenticator_auth_request = autharmor_python.ValidateAutharmorAuthenticatorAuthRequest() # ValidateAutharmorAuthenticatorAuthRequest |  (optional)

    try:
        #  Validate auth request for Auth Armor Authenticator
        api_response = api_instance.v4_auth_authenticator_validate_post(validate_autharmor_authenticator_auth_request=validate_autharmor_authenticator_auth_request)
        print("The response of AutharmorApi->v4_auth_authenticator_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_auth_authenticator_validate_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_autharmor_authenticator_auth_request** | [**ValidateAutharmorAuthenticatorAuthRequest**](ValidateAutharmorAuthenticatorAuthRequest.md)|  | [optional] 

### Return type

[**ValidateAuthResponse**](ValidateAuthResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_auth_magiclink_email_start_post**
> StartMagiclinkEmailAuthResponse v4_auth_magiclink_email_start_post(start_magiclink_email_auth_request=start_magiclink_email_auth_request)

  Start auth request using Maigclink Email

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_magiclink_email_auth_request import StartMagiclinkEmailAuthRequest
from autharmor_python.models.start_magiclink_email_auth_response import StartMagiclinkEmailAuthResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    start_magiclink_email_auth_request = autharmor_python.StartMagiclinkEmailAuthRequest() # StartMagiclinkEmailAuthRequest |  (optional)

    try:
        #   Start auth request using Maigclink Email
        api_response = api_instance.v4_auth_magiclink_email_start_post(start_magiclink_email_auth_request=start_magiclink_email_auth_request)
        print("The response of AutharmorApi->v4_auth_magiclink_email_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_auth_magiclink_email_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_magiclink_email_auth_request** | [**StartMagiclinkEmailAuthRequest**](StartMagiclinkEmailAuthRequest.md)|  | [optional] 

### Return type

[**StartMagiclinkEmailAuthResponse**](StartMagiclinkEmailAuthResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_auth_magiclink_email_validate_post**
> ValidateAuthResponse v4_auth_magiclink_email_validate_post(validate_magiclink_email_auth_request=validate_magiclink_email_auth_request)

  Validate auth request for Magiclink Email

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.validate_auth_response import ValidateAuthResponse
from autharmor_python.models.validate_magiclink_email_auth_request import ValidateMagiclinkEmailAuthRequest
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    validate_magiclink_email_auth_request = autharmor_python.ValidateMagiclinkEmailAuthRequest() # ValidateMagiclinkEmailAuthRequest |  (optional)

    try:
        #   Validate auth request for Magiclink Email
        api_response = api_instance.v4_auth_magiclink_email_validate_post(validate_magiclink_email_auth_request=validate_magiclink_email_auth_request)
        print("The response of AutharmorApi->v4_auth_magiclink_email_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_auth_magiclink_email_validate_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_magiclink_email_auth_request** | [**ValidateMagiclinkEmailAuthRequest**](ValidateMagiclinkEmailAuthRequest.md)|  | [optional] 

### Return type

[**ValidateAuthResponse**](ValidateAuthResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_auth_webauthn_finish_post**
> FinishWebauthnAuthResponse v4_auth_webauthn_finish_post(finish_webauthn_auth_request=finish_webauthn_auth_request)

  Finish auth request using WebAuthn

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.finish_webauthn_auth_request import FinishWebauthnAuthRequest
from autharmor_python.models.finish_webauthn_auth_response import FinishWebauthnAuthResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    finish_webauthn_auth_request = autharmor_python.FinishWebauthnAuthRequest() # FinishWebauthnAuthRequest |  (optional)

    try:
        #   Finish auth request using WebAuthn
        api_response = api_instance.v4_auth_webauthn_finish_post(finish_webauthn_auth_request=finish_webauthn_auth_request)
        print("The response of AutharmorApi->v4_auth_webauthn_finish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_auth_webauthn_finish_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **finish_webauthn_auth_request** | [**FinishWebauthnAuthRequest**](FinishWebauthnAuthRequest.md)|  | [optional] 

### Return type

[**FinishWebauthnAuthResponse**](FinishWebauthnAuthResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_auth_webauthn_start_post**
> StartWebauthnAuthResponse v4_auth_webauthn_start_post(start_webauthn_auth_request=start_webauthn_auth_request)

 Start auth request using Webauthn

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_webauthn_auth_request import StartWebauthnAuthRequest
from autharmor_python.models.start_webauthn_auth_response import StartWebauthnAuthResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    start_webauthn_auth_request = autharmor_python.StartWebauthnAuthRequest() # StartWebauthnAuthRequest |  (optional)

    try:
        #  Start auth request using Webauthn
        api_response = api_instance.v4_auth_webauthn_start_post(start_webauthn_auth_request=start_webauthn_auth_request)
        print("The response of AutharmorApi->v4_auth_webauthn_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_auth_webauthn_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_webauthn_auth_request** | [**StartWebauthnAuthRequest**](StartWebauthnAuthRequest.md)|  | [optional] 

### Return type

[**StartWebauthnAuthResponse**](StartWebauthnAuthResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_auth_webauthn_validate_post**
> ValidateAuthResponse v4_auth_webauthn_validate_post(validate_webauthn_auth_request=validate_webauthn_auth_request)

  Validate auth request for WebAuthn

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.validate_auth_response import ValidateAuthResponse
from autharmor_python.models.validate_webauthn_auth_request import ValidateWebauthnAuthRequest
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    validate_webauthn_auth_request = autharmor_python.ValidateWebauthnAuthRequest() # ValidateWebauthnAuthRequest |  (optional)

    try:
        #   Validate auth request for WebAuthn
        api_response = api_instance.v4_auth_webauthn_validate_post(validate_webauthn_auth_request=validate_webauthn_auth_request)
        print("The response of AutharmorApi->v4_auth_webauthn_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_auth_webauthn_validate_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_webauthn_auth_request** | [**ValidateWebauthnAuthRequest**](ValidateWebauthnAuthRequest.md)|  | [optional] 

### Return type

[**ValidateAuthResponse**](ValidateAuthResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_get**
> GetUsersResponse v4_users_get(username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)

  Get Users

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.get_users_response import GetUsersResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users
        api_response = api_instance.v4_users_get(username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of AutharmorApi->v4_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **sort_column** | **str**|  | [optional] 

### Return type

[**GetUsersResponse**](GetUsersResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_registrations_authenticator_registration_id_validate_post**
> ValidateAutharmorAutenticatorRegistrationResponse v4_users_registrations_authenticator_registration_id_validate_post(registration_id, validate_autharmor_autenticator_registration_request=validate_autharmor_autenticator_registration_request)

  Validate User Registration for Authenticator

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.validate_autharmor_autenticator_registration_request import ValidateAutharmorAutenticatorRegistrationRequest
from autharmor_python.models.validate_autharmor_autenticator_registration_response import ValidateAutharmorAutenticatorRegistrationResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    registration_id = 'registration_id_example' # str | 
    validate_autharmor_autenticator_registration_request = autharmor_python.ValidateAutharmorAutenticatorRegistrationRequest() # ValidateAutharmorAutenticatorRegistrationRequest |  (optional)

    try:
        #   Validate User Registration for Authenticator
        api_response = api_instance.v4_users_registrations_authenticator_registration_id_validate_post(registration_id, validate_autharmor_autenticator_registration_request=validate_autharmor_autenticator_registration_request)
        print("The response of AutharmorApi->v4_users_registrations_authenticator_registration_id_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_registrations_authenticator_registration_id_validate_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**|  | 
 **validate_autharmor_autenticator_registration_request** | [**ValidateAutharmorAutenticatorRegistrationRequest**](ValidateAutharmorAutenticatorRegistrationRequest.md)|  | [optional] 

### Return type

[**ValidateAutharmorAutenticatorRegistrationResponse**](ValidateAutharmorAutenticatorRegistrationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_registrations_authenticator_start_post**
> StartAutharmorAuthenticatorRegistrationNewUserResponse v4_users_registrations_authenticator_start_post(start_autharmor_autenticator_registration_new_user_request=start_autharmor_autenticator_registration_new_user_request)

  Start User Registration for Authenticator

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_autharmor_autenticator_registration_new_user_request import StartAutharmorAutenticatorRegistrationNewUserRequest
from autharmor_python.models.start_autharmor_authenticator_registration_new_user_response import StartAutharmorAuthenticatorRegistrationNewUserResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    start_autharmor_autenticator_registration_new_user_request = autharmor_python.StartAutharmorAutenticatorRegistrationNewUserRequest() # StartAutharmorAutenticatorRegistrationNewUserRequest |  (optional)

    try:
        #   Start User Registration for Authenticator
        api_response = api_instance.v4_users_registrations_authenticator_start_post(start_autharmor_autenticator_registration_new_user_request=start_autharmor_autenticator_registration_new_user_request)
        print("The response of AutharmorApi->v4_users_registrations_authenticator_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_registrations_authenticator_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_autharmor_autenticator_registration_new_user_request** | [**StartAutharmorAutenticatorRegistrationNewUserRequest**](StartAutharmorAutenticatorRegistrationNewUserRequest.md)|  | [optional] 

### Return type

[**StartAutharmorAuthenticatorRegistrationNewUserResponse**](StartAutharmorAuthenticatorRegistrationNewUserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_registrations_magiclink_email_registration_id_validate_post**
> ValidateMagiclinkEmailRegistrationResponse v4_users_registrations_magiclink_email_registration_id_validate_post(registration_id, validate_magiclink_email_registration_request=validate_magiclink_email_registration_request)

  Validate MagicLink Registration Token

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.validate_magiclink_email_registration_request import ValidateMagiclinkEmailRegistrationRequest
from autharmor_python.models.validate_magiclink_email_registration_response import ValidateMagiclinkEmailRegistrationResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    registration_id = 'registration_id_example' # str | 
    validate_magiclink_email_registration_request = autharmor_python.ValidateMagiclinkEmailRegistrationRequest() # ValidateMagiclinkEmailRegistrationRequest |  (optional)

    try:
        #   Validate MagicLink Registration Token
        api_response = api_instance.v4_users_registrations_magiclink_email_registration_id_validate_post(registration_id, validate_magiclink_email_registration_request=validate_magiclink_email_registration_request)
        print("The response of AutharmorApi->v4_users_registrations_magiclink_email_registration_id_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_registrations_magiclink_email_registration_id_validate_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**|  | 
 **validate_magiclink_email_registration_request** | [**ValidateMagiclinkEmailRegistrationRequest**](ValidateMagiclinkEmailRegistrationRequest.md)|  | [optional] 

### Return type

[**ValidateMagiclinkEmailRegistrationResponse**](ValidateMagiclinkEmailRegistrationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_registrations_magiclink_email_start_post**
> StartMagiclinkEmailRegistrationResponse v4_users_registrations_magiclink_email_start_post(start_magiclink_email_registration_request=start_magiclink_email_registration_request)

  Start User Registration for MagicLink

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_magiclink_email_registration_request import StartMagiclinkEmailRegistrationRequest
from autharmor_python.models.start_magiclink_email_registration_response import StartMagiclinkEmailRegistrationResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    start_magiclink_email_registration_request = autharmor_python.StartMagiclinkEmailRegistrationRequest() # StartMagiclinkEmailRegistrationRequest |  (optional)

    try:
        #   Start User Registration for MagicLink
        api_response = api_instance.v4_users_registrations_magiclink_email_start_post(start_magiclink_email_registration_request=start_magiclink_email_registration_request)
        print("The response of AutharmorApi->v4_users_registrations_magiclink_email_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_registrations_magiclink_email_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_magiclink_email_registration_request** | [**StartMagiclinkEmailRegistrationRequest**](StartMagiclinkEmailRegistrationRequest.md)|  | [optional] 

### Return type

[**StartMagiclinkEmailRegistrationResponse**](StartMagiclinkEmailRegistrationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_registrations_registration_id_get**
> GetRegistrationInfoResponse v4_users_registrations_registration_id_get(registration_id)

  Get Registration Info

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.get_registration_info_response import GetRegistrationInfoResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    registration_id = 'registration_id_example' # str | 

    try:
        #   Get Registration Info
        api_response = api_instance.v4_users_registrations_registration_id_get(registration_id)
        print("The response of AutharmorApi->v4_users_registrations_registration_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_registrations_registration_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**|  | 

### Return type

[**GetRegistrationInfoResponse**](GetRegistrationInfoResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_registrations_webauthn_registration_id_finish_post**
> FinishNewWebauthnUserRegistrationResponse v4_users_registrations_webauthn_registration_id_finish_post(registration_id, finish_new_webauthn_user_registration_request=finish_new_webauthn_user_registration_request)

  Finish WebAuthn Registration for new user

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.finish_new_webauthn_user_registration_request import FinishNewWebauthnUserRegistrationRequest
from autharmor_python.models.finish_new_webauthn_user_registration_response import FinishNewWebauthnUserRegistrationResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    registration_id = 'registration_id_example' # str | 
    finish_new_webauthn_user_registration_request = autharmor_python.FinishNewWebauthnUserRegistrationRequest() # FinishNewWebauthnUserRegistrationRequest |  (optional)

    try:
        #   Finish WebAuthn Registration for new user
        api_response = api_instance.v4_users_registrations_webauthn_registration_id_finish_post(registration_id, finish_new_webauthn_user_registration_request=finish_new_webauthn_user_registration_request)
        print("The response of AutharmorApi->v4_users_registrations_webauthn_registration_id_finish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_registrations_webauthn_registration_id_finish_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**|  | 
 **finish_new_webauthn_user_registration_request** | [**FinishNewWebauthnUserRegistrationRequest**](FinishNewWebauthnUserRegistrationRequest.md)|  | [optional] 

### Return type

[**FinishNewWebauthnUserRegistrationResponse**](FinishNewWebauthnUserRegistrationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_registrations_webauthn_registration_id_validate_post**
> ValidateWebauthnRegistrationResponse v4_users_registrations_webauthn_registration_id_validate_post(registration_id, validate_webauthn_registration_request=validate_webauthn_registration_request)

  Validate User Registration for WebAuthn

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.validate_webauthn_registration_request import ValidateWebauthnRegistrationRequest
from autharmor_python.models.validate_webauthn_registration_response import ValidateWebauthnRegistrationResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    registration_id = 'registration_id_example' # str | 
    validate_webauthn_registration_request = autharmor_python.ValidateWebauthnRegistrationRequest() # ValidateWebauthnRegistrationRequest |  (optional)

    try:
        #   Validate User Registration for WebAuthn
        api_response = api_instance.v4_users_registrations_webauthn_registration_id_validate_post(registration_id, validate_webauthn_registration_request=validate_webauthn_registration_request)
        print("The response of AutharmorApi->v4_users_registrations_webauthn_registration_id_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_registrations_webauthn_registration_id_validate_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**|  | 
 **validate_webauthn_registration_request** | [**ValidateWebauthnRegistrationRequest**](ValidateWebauthnRegistrationRequest.md)|  | [optional] 

### Return type

[**ValidateWebauthnRegistrationResponse**](ValidateWebauthnRegistrationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_registrations_webauthn_start_post**
> StartNewWebauthnUserRegistrationResponse v4_users_registrations_webauthn_start_post(start_new_webauthn_user_registration_request=start_new_webauthn_user_registration_request)

  Start WebAuthn Registration for new user

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_new_webauthn_user_registration_request import StartNewWebauthnUserRegistrationRequest
from autharmor_python.models.start_new_webauthn_user_registration_response import StartNewWebauthnUserRegistrationResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    start_new_webauthn_user_registration_request = autharmor_python.StartNewWebauthnUserRegistrationRequest() # StartNewWebauthnUserRegistrationRequest |  (optional)

    try:
        #   Start WebAuthn Registration for new user
        api_response = api_instance.v4_users_registrations_webauthn_start_post(start_new_webauthn_user_registration_request=start_new_webauthn_user_registration_request)
        print("The response of AutharmorApi->v4_users_registrations_webauthn_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_registrations_webauthn_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_new_webauthn_user_registration_request** | [**StartNewWebauthnUserRegistrationRequest**](StartNewWebauthnUserRegistrationRequest.md)|  | [optional] 

### Return type

[**StartNewWebauthnUserRegistrationResponse**](StartNewWebauthnUserRegistrationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_auth_history_get**
> GetUserAuthHistoryResponse v4_users_user_id_auth_history_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)

  Get Auth History for User

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.get_user_auth_history_response import GetUserAuthHistoryResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Auth History for User
        api_response = api_instance.v4_users_user_id_auth_history_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of AutharmorApi->v4_users_user_id_auth_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_auth_history_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **sort_column** | **str**|  | [optional] 

### Return type

[**GetUserAuthHistoryResponse**](GetUserAuthHistoryResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_credentials_authenticator_get**
> GetUserCredentialsResponse v4_users_user_id_credentials_authenticator_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)

  Get Users Authenticator Credential list

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.get_user_credentials_response import GetUserCredentialsResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users Authenticator Credential list
        api_response = api_instance.v4_users_user_id_credentials_authenticator_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of AutharmorApi->v4_users_user_id_credentials_authenticator_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_credentials_authenticator_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **sort_column** | **str**|  | [optional] 

### Return type

[**GetUserCredentialsResponse**](GetUserCredentialsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_credentials_credential_id_disable_post**
> Credential v4_users_user_id_credentials_credential_id_disable_post(user_id, credential_id, username=username)

  Disable Users Credential by Id

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.credential import Credential
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    credential_id = 'credential_id_example' # str | 
    username = 'username_example' # str |  (optional)

    try:
        #   Disable Users Credential by Id
        api_response = api_instance.v4_users_user_id_credentials_credential_id_disable_post(user_id, credential_id, username=username)
        print("The response of AutharmorApi->v4_users_user_id_credentials_credential_id_disable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_credentials_credential_id_disable_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **credential_id** | **str**|  | 
 **username** | **str**|  | [optional] 

### Return type

[**Credential**](Credential.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_credentials_credential_id_get**
> Credential v4_users_user_id_credentials_credential_id_get(user_id, credential_id, username=username)

  Get Users Credential by Credential ID

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.credential import Credential
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    credential_id = 'credential_id_example' # str | 
    username = 'username_example' # str |  (optional)

    try:
        #   Get Users Credential by Credential ID
        api_response = api_instance.v4_users_user_id_credentials_credential_id_get(user_id, credential_id, username=username)
        print("The response of AutharmorApi->v4_users_user_id_credentials_credential_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_credentials_credential_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **credential_id** | **str**|  | 
 **username** | **str**|  | [optional] 

### Return type

[**Credential**](Credential.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_credentials_get**
> GetUserCredentialsResponse v4_users_user_id_credentials_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)

  Get Users Credentials list

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.get_user_credentials_response import GetUserCredentialsResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users Credentials list
        api_response = api_instance.v4_users_user_id_credentials_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of AutharmorApi->v4_users_user_id_credentials_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_credentials_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **sort_column** | **str**|  | [optional] 

### Return type

[**GetUserCredentialsResponse**](GetUserCredentialsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_credentials_magiclink_email_get**
> GetUserCredentialsResponse v4_users_user_id_credentials_magiclink_email_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)

  Get Users Authenticator Credential list

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.get_user_credentials_response import GetUserCredentialsResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users Authenticator Credential list
        api_response = api_instance.v4_users_user_id_credentials_magiclink_email_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of AutharmorApi->v4_users_user_id_credentials_magiclink_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_credentials_magiclink_email_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **sort_column** | **str**|  | [optional] 

### Return type

[**GetUserCredentialsResponse**](GetUserCredentialsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_credentials_webauthn_get**
> GetUserCredentialsResponse v4_users_user_id_credentials_webauthn_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)

  Get Users WebAuthn Device list

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.get_user_credentials_response import GetUserCredentialsResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users WebAuthn Device list
        api_response = api_instance.v4_users_user_id_credentials_webauthn_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of AutharmorApi->v4_users_user_id_credentials_webauthn_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_credentials_webauthn_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **page_number** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 
 **sort_direction** | **str**|  | [optional] 
 **sort_column** | **str**|  | [optional] 

### Return type

[**GetUserCredentialsResponse**](GetUserCredentialsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_get**
> GetUserResponse v4_users_user_id_get(user_id, username=username)

  Get User By Id

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.get_user_response import GetUserResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)

    try:
        #   Get User By Id
        api_response = api_instance.v4_users_user_id_get(user_id, username=username)
        print("The response of AutharmorApi->v4_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 

### Return type

[**GetUserResponse**](GetUserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_magiclink_email_update_start_post**
> StartChangeMagiclinkEmailRegistrationResponse v4_users_user_id_magiclink_email_update_start_post(user_id, username=username, start_change_magiclink_email_registration_request=start_change_magiclink_email_registration_request)

  Start Change Users Email Address

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_change_magiclink_email_registration_request import StartChangeMagiclinkEmailRegistrationRequest
from autharmor_python.models.start_change_magiclink_email_registration_response import StartChangeMagiclinkEmailRegistrationResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    start_change_magiclink_email_registration_request = autharmor_python.StartChangeMagiclinkEmailRegistrationRequest() # StartChangeMagiclinkEmailRegistrationRequest |  (optional)

    try:
        #   Start Change Users Email Address
        api_response = api_instance.v4_users_user_id_magiclink_email_update_start_post(user_id, username=username, start_change_magiclink_email_registration_request=start_change_magiclink_email_registration_request)
        print("The response of AutharmorApi->v4_users_user_id_magiclink_email_update_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_magiclink_email_update_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **start_change_magiclink_email_registration_request** | [**StartChangeMagiclinkEmailRegistrationRequest**](StartChangeMagiclinkEmailRegistrationRequest.md)|  | [optional] 

### Return type

[**StartChangeMagiclinkEmailRegistrationResponse**](StartChangeMagiclinkEmailRegistrationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_put**
> User v4_users_user_id_put(user_id, username=username, update_user_request=update_user_request)

  Update User

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.update_user_request import UpdateUserRequest
from autharmor_python.models.user import User
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    update_user_request = autharmor_python.UpdateUserRequest() # UpdateUserRequest |  (optional)

    try:
        #   Update User
        api_response = api_instance.v4_users_user_id_put(user_id, username=username, update_user_request=update_user_request)
        print("The response of AutharmorApi->v4_users_user_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_registrations_authenticator_start_post**
> StartAutharmorAuthenticatorRegistrationForUserResponse v4_users_user_id_registrations_authenticator_start_post(user_id, username=username)

  Start Authenticator Registration for existing user

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_autharmor_authenticator_registration_for_user_response import StartAutharmorAuthenticatorRegistrationForUserResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)

    try:
        #   Start Authenticator Registration for existing user
        api_response = api_instance.v4_users_user_id_registrations_authenticator_start_post(user_id, username=username)
        print("The response of AutharmorApi->v4_users_user_id_registrations_authenticator_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_registrations_authenticator_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 

### Return type

[**StartAutharmorAuthenticatorRegistrationForUserResponse**](StartAutharmorAuthenticatorRegistrationForUserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_registrations_magiclink_email_start_post**
> StartMagiclinkEmailRegistrationResponse v4_users_user_id_registrations_magiclink_email_start_post(user_id, username=username, start_magiclink_email_registration_request=start_magiclink_email_registration_request)

  Create Magiclink Email Record for existing user

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_magiclink_email_registration_request import StartMagiclinkEmailRegistrationRequest
from autharmor_python.models.start_magiclink_email_registration_response import StartMagiclinkEmailRegistrationResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    start_magiclink_email_registration_request = autharmor_python.StartMagiclinkEmailRegistrationRequest() # StartMagiclinkEmailRegistrationRequest |  (optional)

    try:
        #   Create Magiclink Email Record for existing user
        api_response = api_instance.v4_users_user_id_registrations_magiclink_email_start_post(user_id, username=username, start_magiclink_email_registration_request=start_magiclink_email_registration_request)
        print("The response of AutharmorApi->v4_users_user_id_registrations_magiclink_email_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_registrations_magiclink_email_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **start_magiclink_email_registration_request** | [**StartMagiclinkEmailRegistrationRequest**](StartMagiclinkEmailRegistrationRequest.md)|  | [optional] 

### Return type

[**StartMagiclinkEmailRegistrationResponse**](StartMagiclinkEmailRegistrationResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_registrations_webauthn_registration_id_finish_post**
> FinishAddWebauthnToUserResponse v4_users_user_id_registrations_webauthn_registration_id_finish_post(user_id, registration_id, username=username, finish_add_webauthn_to_user_request=finish_add_webauthn_to_user_request)

  Finish WebAuthn Registration for existing user

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.finish_add_webauthn_to_user_request import FinishAddWebauthnToUserRequest
from autharmor_python.models.finish_add_webauthn_to_user_response import FinishAddWebauthnToUserResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    registration_id = 'registration_id_example' # str | 
    username = 'username_example' # str |  (optional)
    finish_add_webauthn_to_user_request = autharmor_python.FinishAddWebauthnToUserRequest() # FinishAddWebauthnToUserRequest |  (optional)

    try:
        #   Finish WebAuthn Registration for existing user
        api_response = api_instance.v4_users_user_id_registrations_webauthn_registration_id_finish_post(user_id, registration_id, username=username, finish_add_webauthn_to_user_request=finish_add_webauthn_to_user_request)
        print("The response of AutharmorApi->v4_users_user_id_registrations_webauthn_registration_id_finish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_registrations_webauthn_registration_id_finish_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **registration_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **finish_add_webauthn_to_user_request** | [**FinishAddWebauthnToUserRequest**](FinishAddWebauthnToUserRequest.md)|  | [optional] 

### Return type

[**FinishAddWebauthnToUserResponse**](FinishAddWebauthnToUserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_users_user_id_registrations_webauthn_start_post**
> StartAddWebauthnToUserResponse v4_users_user_id_registrations_webauthn_start_post(user_id, username=username, start_add_webauthn_to_user_request=start_add_webauthn_to_user_request)

  Start WebAuthn Registration for existing user

### Example

* OAuth Authentication (oauth2):
```python
import time
import os
import autharmor_python
from autharmor_python.models.start_add_webauthn_to_user_request import StartAddWebauthnToUserRequest
from autharmor_python.models.start_add_webauthn_to_user_response import StartAddWebauthnToUserResponse
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
    api_instance = autharmor_python.AutharmorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    start_add_webauthn_to_user_request = autharmor_python.StartAddWebauthnToUserRequest() # StartAddWebauthnToUserRequest |  (optional)

    try:
        #   Start WebAuthn Registration for existing user
        api_response = api_instance.v4_users_user_id_registrations_webauthn_start_post(user_id, username=username, start_add_webauthn_to_user_request=start_add_webauthn_to_user_request)
        print("The response of AutharmorApi->v4_users_user_id_registrations_webauthn_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutharmorApi->v4_users_user_id_registrations_webauthn_start_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **username** | **str**|  | [optional] 
 **start_add_webauthn_to_user_request** | [**StartAddWebauthnToUserRequest**](StartAddWebauthnToUserRequest.md)|  | [optional] 

### Return type

[**StartAddWebauthnToUserResponse**](StartAddWebauthnToUserResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

