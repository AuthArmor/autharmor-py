# autharmor_python.UsersCredentialsApi

All URIs are relative to *https://api.autharmor.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_users_user_id_credentials_authenticator_get**](UsersCredentialsApi.md#v4_users_user_id_credentials_authenticator_get) | **GET** /v4/users/{user_id}/credentials/authenticator |   Get Users Authenticator Credential list
[**v4_users_user_id_credentials_credential_id_disable_post**](UsersCredentialsApi.md#v4_users_user_id_credentials_credential_id_disable_post) | **POST** /v4/users/{user_id}/credentials/{credential_id}/disable |   Disable Users Credential by Id
[**v4_users_user_id_credentials_credential_id_get**](UsersCredentialsApi.md#v4_users_user_id_credentials_credential_id_get) | **GET** /v4/users/{user_id}/credentials/{credential_id} |   Get Users Credential by Credential ID
[**v4_users_user_id_credentials_get**](UsersCredentialsApi.md#v4_users_user_id_credentials_get) | **GET** /v4/users/{user_id}/credentials |   Get Users Credentials list
[**v4_users_user_id_credentials_magiclink_email_get**](UsersCredentialsApi.md#v4_users_user_id_credentials_magiclink_email_get) | **GET** /v4/users/{user_id}/credentials/magiclink_email |   Get Users Authenticator Credential list
[**v4_users_user_id_credentials_webauthn_get**](UsersCredentialsApi.md#v4_users_user_id_credentials_webauthn_get) | **GET** /v4/users/{user_id}/credentials/webauthn |   Get Users WebAuthn Device list


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
    api_instance = autharmor_python.UsersCredentialsApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users Authenticator Credential list
        api_response = api_instance.v4_users_user_id_credentials_authenticator_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of UsersCredentialsApi->v4_users_user_id_credentials_authenticator_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCredentialsApi->v4_users_user_id_credentials_authenticator_get: %s\n" % e)
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
    api_instance = autharmor_python.UsersCredentialsApi(api_client)
    user_id = 'user_id_example' # str | 
    credential_id = 'credential_id_example' # str | 
    username = 'username_example' # str |  (optional)

    try:
        #   Disable Users Credential by Id
        api_response = api_instance.v4_users_user_id_credentials_credential_id_disable_post(user_id, credential_id, username=username)
        print("The response of UsersCredentialsApi->v4_users_user_id_credentials_credential_id_disable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCredentialsApi->v4_users_user_id_credentials_credential_id_disable_post: %s\n" % e)
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
    api_instance = autharmor_python.UsersCredentialsApi(api_client)
    user_id = 'user_id_example' # str | 
    credential_id = 'credential_id_example' # str | 
    username = 'username_example' # str |  (optional)

    try:
        #   Get Users Credential by Credential ID
        api_response = api_instance.v4_users_user_id_credentials_credential_id_get(user_id, credential_id, username=username)
        print("The response of UsersCredentialsApi->v4_users_user_id_credentials_credential_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCredentialsApi->v4_users_user_id_credentials_credential_id_get: %s\n" % e)
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
    api_instance = autharmor_python.UsersCredentialsApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users Credentials list
        api_response = api_instance.v4_users_user_id_credentials_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of UsersCredentialsApi->v4_users_user_id_credentials_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCredentialsApi->v4_users_user_id_credentials_get: %s\n" % e)
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
    api_instance = autharmor_python.UsersCredentialsApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users Authenticator Credential list
        api_response = api_instance.v4_users_user_id_credentials_magiclink_email_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of UsersCredentialsApi->v4_users_user_id_credentials_magiclink_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCredentialsApi->v4_users_user_id_credentials_magiclink_email_get: %s\n" % e)
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
    api_instance = autharmor_python.UsersCredentialsApi(api_client)
    user_id = 'user_id_example' # str | 
    username = 'username_example' # str |  (optional)
    page_number = 56 # int |  (optional)
    page_size = 56 # int |  (optional)
    sort_direction = 'sort_direction_example' # str |  (optional)
    sort_column = 'sort_column_example' # str |  (optional)

    try:
        #   Get Users WebAuthn Device list
        api_response = api_instance.v4_users_user_id_credentials_webauthn_get(user_id, username=username, page_number=page_number, page_size=page_size, sort_direction=sort_direction, sort_column=sort_column)
        print("The response of UsersCredentialsApi->v4_users_user_id_credentials_webauthn_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersCredentialsApi->v4_users_user_id_credentials_webauthn_get: %s\n" % e)
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

