import csv
import matplotlib.pyplot as plt

filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    averages = []
    for row in reader:
        average = float(row[1])
        averages.append(average)

fig, ax = plt.subplots()
ax.plot(averages)
plt.title("Daily average temperatures, 2020-2021", fontsize=20)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature(C)", fontsize=14)
ax.tick_params(labelsize=14)

plt.show()