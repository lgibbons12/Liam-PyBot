import json
with open("quizlet.json", "r") as f:
    data = json.load(f)

num = len(data['terms'])

for i in (0, len(data['terms'])):
    print(i)
    print(data['terms'][i])
