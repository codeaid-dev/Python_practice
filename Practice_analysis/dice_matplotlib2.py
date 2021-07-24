import matplotlib.pyplot as plt
from dice import Dice

dice1 = Dice()
dice2 = Dice()

# output the result of rolling the dice.
results = [dice1.roll()+dice2.roll() for num in range(1000)]

# count the number of results
max_num = dice1.sides + dice2.sides
y_vals = [results.count(val) for val in range(2, max_num+1)]
x_vals = list(range(2, max_num+1))

fig, ax = plt.subplots()
ax.bar(x_vals, y_vals, width=0.8, tick_label=x_vals)

plt.xlabel('Result')
plt.ylabel('Frequency')
plt.title('The result of 1000 rotations of two 6-sided dices')
#plt.hist(results, bins=dice1.sides+dice2.sides-1, histtype="bar", edgecolor="black", rwidth=0.8)

plt.show()
