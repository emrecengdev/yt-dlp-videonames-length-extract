import json

with open('output.json', 'r') as f:
    data = json.load(f)
    for i, video in enumerate(data['entries'], start=1):
        print(f"{i}. **{video['title']}** - {video['duration']} seconds")
