# SecureSignedMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signed_data** | **str** |  | [optional] 
**signature_data** | [**SignatureData**](SignatureData.md) |  | [optional] 
**signed_data_type** | [**SignedMessageType**](SignedMessageType.md) |  | [optional] 
**signature_validation_details** | **object** |  | [optional] 

## Example

```python
from autharmor_python.models.secure_signed_message import SecureSignedMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SecureSignedMessage from a JSON string
secure_signed_message_instance = SecureSignedMessage.from_json(json)
# print the JSON string representation of the object
print SecureSignedMessage.to_json()

# convert the object into a dict
secure_signed_message_dict = secure_signed_message_instance.to_dict()
# create an instance of SecureSignedMessage from a dict
secure_signed_message_form_dict = secure_signed_message.from_dict(secure_signed_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


