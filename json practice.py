import json

with open("rps/rps.json", "r") as f:
    data = json.load(f)
print(data['counter'])

data['counter'] += 1
with open('rps/rps.json', 'w') as f:
    json.dump(data, f, indent=2)

with open("rps/rps.json", "r") as f:
    data = json.load(f)
print(data['counter'])



