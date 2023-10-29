# StartAddWebauthnToUserResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fido2_json_options** | **object** |  | [optional] 
**registration_id** | **str** |  | [optional] 
**aa_sig** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.start_add_webauthn_to_user_response import StartAddWebauthnToUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartAddWebauthnToUserResponse from a JSON string
start_add_webauthn_to_user_response_instance = StartAddWebauthnToUserResponse.from_json(json)
# print the JSON string representation of the object
print StartAddWebauthnToUserResponse.to_json()

# convert the object into a dict
start_add_webauthn_to_user_response_dict = start_add_webauthn_to_user_response_instance.to_dict()
# create an instance of StartAddWebauthnToUserResponse from a dict
start_add_webauthn_to_user_response_form_dict = start_add_webauthn_to_user_response.from_dict(start_add_webauthn_to_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


