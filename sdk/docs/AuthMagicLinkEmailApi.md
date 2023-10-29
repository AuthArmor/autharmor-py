# autharmor_python.AuthMagicLinkEmailApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_auth_magiclink_email_start_post**](AuthMagicLinkEmailApi.md#v4_auth_magiclink_email_start_post) | **POST** /v4/auth/magiclink_email/start |   Start auth request using Maigclink Email
[**v4_auth_magiclink_email_validate_post**](AuthMagicLinkEmailApi.md#v4_auth_magiclink_email_validate_post) | **POST** /v4/auth/magiclink_email/validate |   Validate auth request for Magiclink Email


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
    api_instance = autharmor_python.AuthMagicLinkEmailApi(api_client)
    start_magiclink_email_auth_request = autharmor_python.StartMagiclinkEmailAuthRequest() # StartMagiclinkEmailAuthRequest |  (optional)

    try:
        #   Start auth request using Maigclink Email
        api_response = api_instance.v4_auth_magiclink_email_start_post(start_magiclink_email_auth_request=start_magiclink_email_auth_request)
        print("The response of AuthMagicLinkEmailApi->v4_auth_magiclink_email_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthMagicLinkEmailApi->v4_auth_magiclink_email_start_post: %s\n" % e)
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
    api_instance = autharmor_python.AuthMagicLinkEmailApi(api_client)
    validate_magiclink_email_auth_request = autharmor_python.ValidateMagiclinkEmailAuthRequest() # ValidateMagiclinkEmailAuthRequest |  (optional)

    try:
        #   Validate auth request for Magiclink Email
        api_response = api_instance.v4_auth_magiclink_email_validate_post(validate_magiclink_email_auth_request=validate_magiclink_email_auth_request)
        print("The response of AuthMagicLinkEmailApi->v4_auth_magiclink_email_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthMagicLinkEmailApi->v4_auth_magiclink_email_validate_post: %s\n" % e)
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

