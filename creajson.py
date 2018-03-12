import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Maria',
    'surname': 'Sevilla',
    'from': 'Madrid'

})


with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
