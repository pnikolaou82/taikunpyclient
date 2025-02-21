# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**file** | **str** |  | [optional] 
**rules** | [**List[Rule]**](Rule.md) |  | [optional] 
**interval** | **int** |  | [optional] 
**evaluation_time** | **float** |  | [optional] 
**last_evaluation** | **datetime** |  | [optional] 

## Example

```python
from taikunpycore.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


