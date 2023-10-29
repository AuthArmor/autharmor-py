# autharmor_python.UserRegistrationsGetRegistrationInfoApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_users_registrations_registration_id_get**](UserRegistrationsGetRegistrationInfoApi.md#v4_users_registrations_registration_id_get) | **GET** /v4/users/registrations/{registration_Id} |   Get Registration Info


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
    api_instance = autharmor_python.UserRegistrationsGetRegistrationInfoApi(api_client)
    registration_id = 'registration_id_example' # str | 

    try:
        #   Get Registration Info
        api_response = api_instance.v4_users_registrations_registration_id_get(registration_id)
        print("The response of UserRegistrationsGetRegistrationInfoApi->v4_users_registrations_registration_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserRegistrationsGetRegistrationInfoApi->v4_users_registrations_registration_id_get: %s\n" % e)
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

