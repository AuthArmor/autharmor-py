# MobileDeviceDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** |  | [optional] 
**model** | **str** |  | [optional] 

## Example

```python
from autharmor_python.models.mobile_device_details import MobileDeviceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MobileDeviceDetails from a JSON string
mobile_device_details_instance = MobileDeviceDetails.from_json(json)
# print the JSON string representation of the object
print MobileDeviceDetails.to_json()

# convert the object into a dict
mobile_device_details_dict = mobile_device_details_instance.to_dict()
# create an instance of MobileDeviceDetails from a dict
mobile_device_details_form_dict = mobile_device_details.from_dict(mobile_device_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


