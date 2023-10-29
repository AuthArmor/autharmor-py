# autharmor_python.AuthWebAuthnApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_auth_webauthn_finish_post**](AuthWebAuthnApi.md#v4_auth_webauthn_finish_post) | **POST** /v4/auth/webauthn/finish |   Finish auth request using WebAuthn
[**v4_auth_webauthn_start_post**](AuthWebAuthnApi.md#v4_auth_webauthn_start_post) | **POST** /v4/auth/webauthn/start |  Start auth request using Webauthn
[**v4_auth_webauthn_validate_post**](AuthWebAuthnApi.md#v4_auth_webauthn_validate_post) | **POST** /v4/auth/webauthn/validate |   Validate auth request for WebAuthn


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
    api_instance = autharmor_python.AuthWebAuthnApi(api_client)
    finish_webauthn_auth_request = autharmor_python.FinishWebauthnAuthRequest() # FinishWebauthnAuthRequest |  (optional)

    try:
        #   Finish auth request using WebAuthn
        api_response = api_instance.v4_auth_webauthn_finish_post(finish_webauthn_auth_request=finish_webauthn_auth_request)
        print("The response of AuthWebAuthnApi->v4_auth_webauthn_finish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthWebAuthnApi->v4_auth_webauthn_finish_post: %s\n" % e)
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
    api_instance = autharmor_python.AuthWebAuthnApi(api_client)
    start_webauthn_auth_request = autharmor_python.StartWebauthnAuthRequest() # StartWebauthnAuthRequest |  (optional)

    try:
        #  Start auth request using Webauthn
        api_response = api_instance.v4_auth_webauthn_start_post(start_webauthn_auth_request=start_webauthn_auth_request)
        print("The response of AuthWebAuthnApi->v4_auth_webauthn_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthWebAuthnApi->v4_auth_webauthn_start_post: %s\n" % e)
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
    api_instance = autharmor_python.AuthWebAuthnApi(api_client)
    validate_webauthn_auth_request = autharmor_python.ValidateWebauthnAuthRequest() # ValidateWebauthnAuthRequest |  (optional)

    try:
        #   Validate auth request for WebAuthn
        api_response = api_instance.v4_auth_webauthn_validate_post(validate_webauthn_auth_request=validate_webauthn_auth_request)
        print("The response of AuthWebAuthnApi->v4_auth_webauthn_validate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthWebAuthnApi->v4_auth_webauthn_validate_post: %s\n" % e)
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

