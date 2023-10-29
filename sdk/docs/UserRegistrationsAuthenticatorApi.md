# autharmor_python.UserRegistrationsAuthenticatorApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_users_registrations_authenticator_registration_id_validate_post**](UserRegistrationsAuthenticatorApi.md#v4_users_registrations_authenticator_registration_id_validate_post) | **POST** /v4/users/registrations/authenticator/{registration_id}/validate |   Validate User Registration for Authenticator
[**v4_users_registrations_authenticator_start_post**](UserRegistrationsAuthenticatorApi.md#v4_users_registrations_authenticator_start_post) | **POST** /v4/users/registrations/authenticator/start |   Start User Registration for Authenticator
[**v4_users_user_id_registrations_authenticator_start_post**](UserRegistrationsAuthenticatorApi.md#v4_users_user_id_registrations_authenticator_start_post) | **POST** /v4/users/{user_id}/registrations/authenticator/start |   Start Authenticator Registration for existing user


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
    api_instance = autharmor_python.UserRegistrationsAuthenticatorApi(api_client)
    registration_id = 'registration_id_example' # str | 
    validate_autharmor_autenticator_registration_request = autharmor_python.ValidateAutharmorAutenticatorRegistrationRequest() # ValidateAutharmorAutenticatorRegistrationRequest |  (optional)

    try:
        #   Validate User Registration for Authenticator
        api_response = api_instance.v4_users_registrations_authenticator_registration_id_validate_post(registration_id, validate_autharmor_autenticator_registration_request=validate_autharmor_autenticator_registration_request)
        print("The response of UserRegistrationsAuthenticatorApi->v4_users_registrations_authenticator_registration_id_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsAuthenticatorApi->v4_users_registrations_authenticator_registration_id_validate_post: %s\n" % e)
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
    api_instance = autharmor_python.UserRegistrationsAuthenticatorApi(api_client)
    start_autharmor_autenticator_registration_new_user_request = autharmor_python.StartAutharmorAutenticatorRegistrationNewUserRequest() # StartAutharmorAutenticatorRegistrationNewUserRequest |  (optional)

    try:
        #   Start User Registration for Authenticator
        api_response = api_instance.v4_users_registrations_authenticator_start_post(start_autharmor_autenticator_registration_new_user_request=start_autharmor_autenticator_registration_new_user_request)
        print("The response of UserRegistrationsAuthenticatorApi->v4_users_registrations_authenticator_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsAuthenticatorApi->v4_users_registrations_authenticator_start_post: %s\n" % e)
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
    api_instance = autharmor_python.UserRegistrationsAuthenticatorApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)

    try:
        #   Start Authenticator Registration for existing user
        api_response = api_instance.v4_users_user_id_registrations_authenticator_start_post(user_id, username=username)
        print("The response of UserRegistrationsAuthenticatorApi->v4_users_user_id_registrations_authenticator_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsAuthenticatorApi->v4_users_user_id_registrations_authenticator_start_post: %s\n" % e)
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

