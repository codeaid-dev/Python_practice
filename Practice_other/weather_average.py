import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, averages = [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y/%m/%d')
        average = float(row[1])
        dates.append(date)
        averages.append(average)

fig, ax = plt.subplots()
ax.plot(dates, averages)
plt.title("Daily average Osaka temps, 2020-2021", fontsize=20)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature(C)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(labelsize=14)
plt.grid()
plt.show()