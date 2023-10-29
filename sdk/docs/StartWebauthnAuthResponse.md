# StartWebauthnAuthResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fido2_json_options** | **str** |  | [optional] 
**auth_request_id** | **str** |  | [optional] 
**aa_guid** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.start_webauthn_auth_response import StartWebauthnAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartWebauthnAuthResponse from a JSON string
start_webauthn_auth_response_instance = StartWebauthnAuthResponse.from_json(json)
# print the JSON string representation of the object
print StartWebauthnAuthResponse.to_json()

# convert the object into a dict
start_webauthn_auth_response_dict = start_webauthn_auth_response_instance.to_dict()
# create an instance of StartWebauthnAuthResponse from a dict
start_webauthn_auth_response_form_dict = start_webauthn_auth_response.from_dict(start_webauthn_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


