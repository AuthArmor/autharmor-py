# autharmor_python.AuthInfoApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_auth_auth_request_id_get**](AuthInfoApi.md#v4_auth_auth_request_id_get) | **GET** /v4/auth/{auth_request_id} |   Get Auth Info


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
    api_instance = autharmor_python.AuthInfoApi(api_client)
    auth_request_id = 'auth_request_id_example' # str | 

    try:
        #   Get Auth Info
        api_response = api_instance.v4_auth_auth_request_id_get(auth_request_id)
        print("The response of AuthInfoApi->v4_auth_auth_request_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthInfoApi->v4_auth_auth_request_id_get: %s\n" % e)
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

