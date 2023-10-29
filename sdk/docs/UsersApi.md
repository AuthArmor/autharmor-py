# autharmor_python.UsersApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_users_get**](UsersApi.md#v4_users_get) | **GET** /v4/users |   Get Users
[**v4_users_user_id_auth_history_get**](UsersApi.md#v4_users_user_id_auth_history_get) | **GET** /v4/users/{user_id}/auth_history |   Get Auth History for User
[**v4_users_user_id_get**](UsersApi.md#v4_users_user_id_get) | **GET** /v4/users/{user_id} |   Get User By Id
[**v4_users_user_id_put**](UsersApi.md#v4_users_user_id_put) | **PUT** /v4/users/{user_id} |   Update User


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
    api_instance = autharmor_python.UsersApi(api_client)
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users
        api_response = api_instance.v4_users_get(username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of UsersApi->v4_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v4_users_get: %s\n" % e)
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
    api_instance = autharmor_python.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Auth History for User
        api_response = api_instance.v4_users_user_id_auth_history_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of UsersApi->v4_users_user_id_auth_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v4_users_user_id_auth_history_get: %s\n" % e)
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
    api_instance = autharmor_python.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)

    try:
        #   Get User By Id
        api_response = api_instance.v4_users_user_id_get(user_id, username=username)
        print("The response of UsersApi->v4_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v4_users_user_id_get: %s\n" % e)
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
    api_instance = autharmor_python.UsersApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    update_user_request = autharmor_python.UpdateUserRequest() # UpdateUserRequest |  (optional)

    try:
        #   Update User
        api_response = api_instance.v4_users_user_id_put(user_id, username=username, update_user_request=update_user_request)
        print("The response of UsersApi->v4_users_user_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->v4_users_user_id_put: %s\n" % e)
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

