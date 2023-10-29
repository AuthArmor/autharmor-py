# autharmor_python.UserRegistrationsWebAuthnApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_users_registrations_webauthn_registration_id_finish_post**](UserRegistrationsWebAuthnApi.md#v4_users_registrations_webauthn_registration_id_finish_post) | **POST** /v4/users/registrations/webauthn/{registration_id}/finish |   Finish WebAuthn Registration for new user
[**v4_users_registrations_webauthn_registration_id_validate_post**](UserRegistrationsWebAuthnApi.md#v4_users_registrations_webauthn_registration_id_validate_post) | **POST** /v4/users/registrations/webauthn/{registration_id}/validate |   Validate User Registration for WebAuthn
[**v4_users_registrations_webauthn_start_post**](UserRegistrationsWebAuthnApi.md#v4_users_registrations_webauthn_start_post) | **POST** /v4/users/registrations/webauthn/start |   Start WebAuthn Registration for new user
[**v4_users_user_id_registrations_webauthn_registration_id_finish_post**](UserRegistrationsWebAuthnApi.md#v4_users_user_id_registrations_webauthn_registration_id_finish_post) | **POST** /v4/users/{user_id}/registrations/webauthn/{registration_id}/finish |   Finish WebAuthn Registration for existing user
[**v4_users_user_id_registrations_webauthn_start_post**](UserRegistrationsWebAuthnApi.md#v4_users_user_id_registrations_webauthn_start_post) | **POST** /v4/users/{user_id}/registrations/webauthn/start |   Start WebAuthn Registration for existing user


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
    api_instance = autharmor_python.UserRegistrationsWebAuthnApi(api_client)
    registration_id = 'registration_id_example' # str | 
    finish_new_webauthn_user_registration_request = autharmor_python.FinishNewWebauthnUserRegistrationRequest() # FinishNewWebauthnUserRegistrationRequest |  (optional)

    try:
        #   Finish WebAuthn Registration for new user
        api_response = api_instance.v4_users_registrations_webauthn_registration_id_finish_post(registration_id, finish_new_webauthn_user_registration_request=finish_new_webauthn_user_registration_request)
        print("The response of UserRegistrationsWebAuthnApi->v4_users_registrations_webauthn_registration_id_finish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsWebAuthnApi->v4_users_registrations_webauthn_registration_id_finish_post: %s\n" % e)
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
    api_instance = autharmor_python.UserRegistrationsWebAuthnApi(api_client)
    registration_id = 'registration_id_example' # str | 
    validate_webauthn_registration_request = autharmor_python.ValidateWebauthnRegistrationRequest() # ValidateWebauthnRegistrationRequest |  (optional)

    try:
        #   Validate User Registration for WebAuthn
        api_response = api_instance.v4_users_registrations_webauthn_registration_id_validate_post(registration_id, validate_webauthn_registration_request=validate_webauthn_registration_request)
        print("The response of UserRegistrationsWebAuthnApi->v4_users_registrations_webauthn_registration_id_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsWebAuthnApi->v4_users_registrations_webauthn_registration_id_validate_post: %s\n" % e)
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
    api_instance = autharmor_python.UserRegistrationsWebAuthnApi(api_client)
    start_new_webauthn_user_registration_request = autharmor_python.StartNewWebauthnUserRegistrationRequest() # StartNewWebauthnUserRegistrationRequest |  (optional)

    try:
        #   Start WebAuthn Registration for new user
        api_response = api_instance.v4_users_registrations_webauthn_start_post(start_new_webauthn_user_registration_request=start_new_webauthn_user_registration_request)
        print("The response of UserRegistrationsWebAuthnApi->v4_users_registrations_webauthn_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsWebAuthnApi->v4_users_registrations_webauthn_start_post: %s\n" % e)
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
    api_instance = autharmor_python.UserRegistrationsWebAuthnApi(api_client)
    user_id = 'user_id_example' # str | 
    registration_id = 'registration_id_example' # str | 
    username = 'username_example' # str |  (optional)
    finish_add_webauthn_to_user_request = autharmor_python.FinishAddWebauthnToUserRequest() # FinishAddWebauthnToUserRequest |  (optional)

    try:
        #   Finish WebAuthn Registration for existing user
        api_response = api_instance.v4_users_user_id_registrations_webauthn_registration_id_finish_post(user_id, registration_id, username=username, finish_add_webauthn_to_user_request=finish_add_webauthn_to_user_request)
        print("The response of UserRegistrationsWebAuthnApi->v4_users_user_id_registrations_webauthn_registration_id_finish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsWebAuthnApi->v4_users_user_id_registrations_webauthn_registration_id_finish_post: %s\n" % e)
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
    api_instance = autharmor_python.UserRegistrationsWebAuthnApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    start_add_webauthn_to_user_request = autharmor_python.StartAddWebauthnToUserRequest() # StartAddWebauthnToUserRequest |  (optional)

    try:
        #   Start WebAuthn Registration for existing user
        api_response = api_instance.v4_users_user_id_registrations_webauthn_start_post(user_id, username=username, start_add_webauthn_to_user_request=start_add_webauthn_to_user_request)
        print("The response of UserRegistrationsWebAuthnApi->v4_users_user_id_registrations_webauthn_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsWebAuthnApi->v4_users_user_id_registrations_webauthn_start_post: %s\n" % e)
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

