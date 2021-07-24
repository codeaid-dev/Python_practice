import json
from datetime import datetime

filename = 'osaka.json'
with open(filename) as f:
    data = json.load(f)

dates = data[1]['timeSeries'][0]['timeDefines']
weathers = data[1]['timeSeries'][0]['areas'][0]['weatherCodes']
pops = data[1]['timeSeries'][0]['areas'][0]['pops']
temps_min = data[1]['timeSeries'][1]['areas'][0]['tempsMin']
temps_max = data[1]['timeSeries'][1]['areas'][0]['tempsMax']

filename = 'weathercodes.json'
with open(filename) as f:
    codes = json.load(f)

reports = []
for s in weathers:
    reports.append(codes[s][0])

for i,d in enumerate(dates):
    print(d.replace(d[10:],''))
    print(f'天気：{reports[i]}')
    print(f'降水確率：{pops[i]}%')
    print(f'最高気温：{temps_max[i]}℃')
    print(f'最低気温：{temps_min[i]}℃')
    print('')
