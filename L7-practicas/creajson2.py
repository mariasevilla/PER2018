import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Agueda',
    'surname': 'Sierra',
    'from': 'Madrid'

})


with open('data2.json', 'w') as outfile:
    json.dump(data, outfile)
