# RequestDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** |  | [optional] 
**auth_profile_details** | [**AuthProfileDetails**](AuthProfileDetails.md) |  | [optional] 
**origin_location_data** | [**LocationData**](LocationData.md) |  | [optional] 
**auth_method** | [**AuthMethods**](AuthMethods.md) |  | [optional] 

## Example

```python
from autharmor_python.models.request_details import RequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDetails from a JSON string
request_details_instance = RequestDetails.from_json(json)
# print the JSON string representation of the object
print RequestDetails.to_json()

# convert the object into a dict
request_details_dict = request_details_instance.to_dict()
# create an instance of RequestDetails from a dict
request_details_form_dict = request_details.from_dict(request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


