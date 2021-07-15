from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

dice = Dice()

# output the result of rolling the dice.
results = []
for num in range(1000):
    result = dice.roll()
    results.append(result)

# count the number of results
counts = []
for val in range(1, dice.sides+1):
    cnt = results.count(val)
    counts.append(cnt)

# visualize the result
x_vals = list(range(1, dice.sides+1))
data = [Bar(x=x_vals, y=counts)]

x_axis = {'title': '結果'}
y_axis = {'title': '出現回数'}
layout = Layout(title='6面サイコロを1000回転がした結果', xaxis=x_axis, yaxis=y_axis)
offline.plot({'data': data, 'layout': layout}, filename='result.html')
