from plotly.graph_objs import Bar, Layout
from plotly import offline
from dice import Dice

dice1 = Dice()
dice2 = Dice()

# output the result of rolling the dice.
#results = []
#for num in range(1000):
#    result = dice1.roll() + dice2.roll()
#    results.append(result)
results = [dice1.roll()+dice2.roll() for num in range(1000)]

# count the number of results
#counts = []
max_num = dice1.sides + dice2.sides
#for val in range(2, max_num+1):
#    cnt = results.count(val)
#    counts.append(cnt)
counts = [results.count(val) for val in range(2, max_num+1)]

# visualize the result
x_vals = list(range(2, max_num+1))
data = [Bar(x=x_vals, y=counts)]

x_axis = {'title': '結果', 'dtick': 1}
y_axis = {'title': '出現回数'}
layout = Layout(title='2個の6面サイコロを1000回転がした結果', xaxis=x_axis, yaxis=y_axis)
offline.plot({'data': data, 'layout': layout}, filename='res_two.html')