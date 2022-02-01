import json
import requests

from nobel_model import LaureateModel

response = requests.get('http://api.nobelprize.org/v1/laureate.json')
laureate_json_data = response.text

# # transforming a json string into a dictionary
laureate_data = json.loads(laureate_json_data)
# print(laureate_data['laureates'][0])
# print('-' * 100)
# print(laureate_data['laureates'][0]['prizes'][0]['affiliations'][0]['name'])

instance_of_LaureateModel = LaureateModel(laureate_data)
print(instance_of_LaureateModel.__dict__.keys())

print(instance_of_LaureateModel.laureates[0].firstname)
print('-' * 100)
print(instance_of_LaureateModel.laureates[0].prizes[0].affiliations[0].name)
print(instance_of_LaureateModel.laureates[0].items())