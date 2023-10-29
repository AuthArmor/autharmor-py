# StartAddWebauthnToUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout_in_seconds** | **int** |  | [optional] 
**webauthn_client_id** | **str** |  | [optional] 
**attachment_type** | [**AuthenticatorAttachmentType**](AuthenticatorAttachmentType.md) |  | [optional] 
**resident_key_requirement_type** | [**ResidentKeyRequirementType**](ResidentKeyRequirementType.md) |  | [optional] 
**user_verification_requirement_type** | [**UserVerificationRequirementType**](UserVerificationRequirementType.md) |  | [optional] 

## Example

```python
from autharmor_python.models.start_add_webauthn_to_user_request import StartAddWebauthnToUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartAddWebauthnToUserRequest from a JSON string
start_add_webauthn_to_user_request_instance = StartAddWebauthnToUserRequest.from_json(json)
# print the JSON string representation of the object
print StartAddWebauthnToUserRequest.to_json()

# convert the object into a dict
start_add_webauthn_to_user_request_dict = start_add_webauthn_to_user_request_instance.to_dict()
# create an instance of StartAddWebauthnToUserRequest from a dict
start_add_webauthn_to_user_request_form_dict = start_add_webauthn_to_user_request.from_dict(start_add_webauthn_to_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


