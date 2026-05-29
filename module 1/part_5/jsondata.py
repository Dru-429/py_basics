# here we gonna see how to manage JSON type data in python 
import json

json_string = '{"name":"Dru"}'
data = json.loads(json_string)

print(data["name"])

data = {
  "name": "Dhruv",
  "role": "AI Engineer"
}
json_data = json.dumps(data)
print(json_data)

#writting json in a file

with open("data.json", "w") as file:
  json.dump(data, file, indent=4)
#indent-4 makes it looks prettier by procviding spaces 
  
with open("data.json", "r") as file:
  data = json.load(file)
  
  print(data)