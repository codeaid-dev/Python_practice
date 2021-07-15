import matplotlib.pyplot as plt
from dice import Dice

dice = Dice()

# output the result of rolling the dice.
results = [dice.roll() for num in range(1000)]

# count the number of results
y_vals = [results.count(val) for val in range(1, dice.sides+1)]
x_vals = list(range(1, dice.sides+1))

fig = plt.figure()
ax = fig.add_subplot(111) #1行1列目1番目
ax.bar(x_vals, y_vals, width=0.8, tick_label=x_vals)

plt.xlabel('Result')
plt.ylabel('Frequency')
plt.title('The result of 1000 rotations of the 6-sided dice')
#plt.hist(results, bins=dice.sides, histtype="bar", edgecolor="black", rwidth=0.8)

plt.show()
