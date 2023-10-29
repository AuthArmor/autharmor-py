# StartNewWebauthnUserRegistrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**email_address** | **str** |  | [optional] 
**timeout_in_seconds** | **int** |  | [optional] 
**webauthn_client_id** | **str** |  | [optional] 
**attachment_type** | [**AuthenticatorAttachmentType**](AuthenticatorAttachmentType.md) |  | [optional] 
**resident_key_requirement_type** | [**ResidentKeyRequirementType**](ResidentKeyRequirementType.md) |  | [optional] 
**user_verification_requirement_type** | [**UserVerificationRequirementType**](UserVerificationRequirementType.md) |  | [optional] 

## Example

```python
from autharmor_python.models.start_new_webauthn_user_registration_request import StartNewWebauthnUserRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StartNewWebauthnUserRegistrationRequest from a JSON string
start_new_webauthn_user_registration_request_instance = StartNewWebauthnUserRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print StartNewWebauthnUserRegistrationRequest.to_json()

# convert the object into a dict
start_new_webauthn_user_registration_request_dict = start_new_webauthn_user_registration_request_instance.to_dict()
# create an instance of StartNewWebauthnUserRegistrationRequest from a dict
start_new_webauthn_user_registration_request_form_dict = start_new_webauthn_user_registration_request.from_dict(start_new_webauthn_user_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


