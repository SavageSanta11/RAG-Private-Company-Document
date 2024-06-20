import json

# Assuming your JSON file is named 'data.json'
file_path = '../datasets/response.json'

# Open the file and load its contents
with open(file_path, 'r') as file:
    data = json.load(file)

# Now 'data' contains the JSON content from the file
print(data[:5])