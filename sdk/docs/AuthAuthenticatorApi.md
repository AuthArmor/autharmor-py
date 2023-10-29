# autharmor_python.AuthAuthenticatorApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_auth_authenticator_start_post**](AuthAuthenticatorApi.md#v4_auth_authenticator_start_post) | **POST** /v4/auth/authenticator/start |   Start auth request using Authenticator
[**v4_auth_authenticator_validate_post**](AuthAuthenticatorApi.md#v4_auth_authenticator_validate_post) | **POST** /v4/auth/authenticator/validate |  Validate auth request for Auth Armor Authenticator


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
    api_instance = autharmor_python.AuthAuthenticatorApi(api_client)
    start_authenticator_auth_request = autharmor_python.StartAuthenticatorAuthRequest() # StartAuthenticatorAuthRequest |  (optional)

    try:
        #   Start auth request using Authenticator
        api_response = api_instance.v4_auth_authenticator_start_post(start_authenticator_auth_request=start_authenticator_auth_request)
        print("The response of AuthAuthenticatorApi->v4_auth_authenticator_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthAuthenticatorApi->v4_auth_authenticator_start_post: %s\n" % e)
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
    api_instance = autharmor_python.AuthAuthenticatorApi(api_client)
    validate_autharmor_authenticator_auth_request = autharmor_python.ValidateAutharmorAuthenticatorAuthRequest() # ValidateAutharmorAuthenticatorAuthRequest |  (optional)

    try:
        #  Validate auth request for Auth Armor Authenticator
        api_response = api_instance.v4_auth_authenticator_validate_post(validate_autharmor_authenticator_auth_request=validate_autharmor_authenticator_auth_request)
        print("The response of AuthAuthenticatorApi->v4_auth_authenticator_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthAuthenticatorApi->v4_auth_authenticator_validate_post: %s\n" % e)
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

