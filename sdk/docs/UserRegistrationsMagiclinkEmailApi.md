# autharmor_python.UserRegistrationsMagiclinkEmailApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_users_registrations_magiclink_email_registration_id_validate_post**](UserRegistrationsMagiclinkEmailApi.md#v4_users_registrations_magiclink_email_registration_id_validate_post) | **POST** /v4/users/registrations/magiclink_email/{registration_id}/validate |   Validate MagicLink Registration Token
[**v4_users_registrations_magiclink_email_start_post**](UserRegistrationsMagiclinkEmailApi.md#v4_users_registrations_magiclink_email_start_post) | **POST** /v4/users/registrations/magiclink_email/start |   Start User Registration for MagicLink
[**v4_users_user_id_magiclink_email_update_start_post**](UserRegistrationsMagiclinkEmailApi.md#v4_users_user_id_magiclink_email_update_start_post) | **POST** /v4/users/{user_id}/magiclink_email/update/start |   Start Change Users Email Address
[**v4_users_user_id_registrations_magiclink_email_start_post**](UserRegistrationsMagiclinkEmailApi.md#v4_users_user_id_registrations_magiclink_email_start_post) | **POST** /v4/users/{user_id}/registrations/magiclink_email/start |   Create Magiclink Email Record for existing user


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
    api_instance = autharmor_python.UserRegistrationsMagiclinkEmailApi(api_client)
    registration_id = 'registration_id_example' # str | 
    validate_magiclink_email_registration_request = autharmor_python.ValidateMagiclinkEmailRegistrationRequest() # ValidateMagiclinkEmailRegistrationRequest |  (optional)

    try:
        #   Validate MagicLink Registration Token
        api_response = api_instance.v4_users_registrations_magiclink_email_registration_id_validate_post(registration_id, validate_magiclink_email_registration_request=validate_magiclink_email_registration_request)
        print("The response of UserRegistrationsMagiclinkEmailApi->v4_users_registrations_magiclink_email_registration_id_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsMagiclinkEmailApi->v4_users_registrations_magiclink_email_registration_id_validate_post: %s\n" % e)
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
    api_instance = autharmor_python.UserRegistrationsMagiclinkEmailApi(api_client)
    start_magiclink_email_registration_request = autharmor_python.StartMagiclinkEmailRegistrationRequest() # StartMagiclinkEmailRegistrationRequest |  (optional)

    try:
        #   Start User Registration for MagicLink
        api_response = api_instance.v4_users_registrations_magiclink_email_start_post(start_magiclink_email_registration_request=start_magiclink_email_registration_request)
        print("The response of UserRegistrationsMagiclinkEmailApi->v4_users_registrations_magiclink_email_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsMagiclinkEmailApi->v4_users_registrations_magiclink_email_start_post: %s\n" % e)
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
    api_instance = autharmor_python.UserRegistrationsMagiclinkEmailApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    start_change_magiclink_email_registration_request = autharmor_python.StartChangeMagiclinkEmailRegistrationRequest() # StartChangeMagiclinkEmailRegistrationRequest |  (optional)

    try:
        #   Start Change Users Email Address
        api_response = api_instance.v4_users_user_id_magiclink_email_update_start_post(user_id, username=username, start_change_magiclink_email_registration_request=start_change_magiclink_email_registration_request)
        print("The response of UserRegistrationsMagiclinkEmailApi->v4_users_user_id_magiclink_email_update_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsMagiclinkEmailApi->v4_users_user_id_magiclink_email_update_start_post: %s\n" % e)
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
    api_instance = autharmor_python.UserRegistrationsMagiclinkEmailApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    start_magiclink_email_registration_request = autharmor_python.StartMagiclinkEmailRegistrationRequest() # StartMagiclinkEmailRegistrationRequest |  (optional)

    try:
        #   Create Magiclink Email Record for existing user
        api_response = api_instance.v4_users_user_id_registrations_magiclink_email_start_post(user_id, username=username, start_magiclink_email_registration_request=start_magiclink_email_registration_request)
        print("The response of UserRegistrationsMagiclinkEmailApi->v4_users_user_id_registrations_magiclink_email_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsMagiclinkEmailApi->v4_users_user_id_registrations_magiclink_email_start_post: %s\n" % e)
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

