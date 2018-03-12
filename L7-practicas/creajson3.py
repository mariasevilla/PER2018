import json

data = {}
data['tema2'] = []
data['temas']=[]

({
    'nombre': 'biofisica',
    'curso': '1º',
    'titulación': 'Ingenieria biomedica',
    'temas:': data['temas'].append({
    'numero':'1','titulo': 'Electroestatica', 'horas':'20'})
    'temas':data['temas'].append({
    'numero':'2','titulo': 'Magnetoestatica', 'horas':'20'})
    'temas':data['temas'].append({
    'numero':'3','titulo': 'Ecuaciones de Maxwell', 'horas':'20'})
    'temas':data['temas'].append({
    'numero':'4','titulo': 'biofisica', 'horas':'20'})

})


with open('asignatura.json', 'w') as outfile:
    json.dump(data, outfile)
