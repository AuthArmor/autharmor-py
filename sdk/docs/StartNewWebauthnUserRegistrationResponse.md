# StartNewWebauthnUserRegistrationResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fido2_json_options** | **object** |  | [optional] 
**registration_id** | **str** |  | [optional] 
**aa_sig** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.start_new_webauthn_user_registration_response import StartNewWebauthnUserRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StartNewWebauthnUserRegistrationResponse from a JSON string
start_new_webauthn_user_registration_response_instance = StartNewWebauthnUserRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print StartNewWebauthnUserRegistrationResponse.to_json()

# convert the object into a dict
start_new_webauthn_user_registration_response_dict = start_new_webauthn_user_registration_response_instance.to_dict()
# create an instance of StartNewWebauthnUserRegistrationResponse from a dict
start_new_webauthn_user_registration_response_form_dict = start_new_webauthn_user_registration_response.from_dict(start_new_webauthn_user_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


