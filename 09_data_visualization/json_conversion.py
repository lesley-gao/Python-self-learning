import json

# Prepare a list where each element is a dictionary, and convert it to JSON
data = [{"name": "Lily", "age": 11}, {"name": "Lucy", "age": 13}, {"name": "Jim", "age": 16}]
json_str = json.dumps(data)
print(type(json_str))    # <class 'str'>
print(json_str)          # [{"name": "Lily", "age": 11}, {"name": "Lucy", "age": 13}, {"name": "Jim", "age": 16}]

# Prepare a dictionary and convert it to JSON
d = {"name": "Jay", "addr": "New Zealand"}
json_str = json.dumps(d)
print(type(json_str))    # <class 'str'>
print(json_str)          # {"name": "Jay", "addr": "New Zealand"}

# Convert a JSON string into a Python data type (a list of dictionaries)
s = ' [{"name": "Lily", "age": 11}, {"name": "Lucy", "age": 13}, {"name": "Jim", "age": 16}]'
l = json.loads(s)
print(type(l))           # <class 'list'>
