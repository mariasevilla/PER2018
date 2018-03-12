import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Maria',
    'surname': 'Sevilla',
    'from': 'Madrid'

})


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
