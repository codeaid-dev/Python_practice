import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, averages, highs, lows = [], [], [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y/%m/%d')
        average = float(row[1])
        high = float(row[2])
        low = float(row[3])
        dates.append(date)
        averages.append(average)
        highs.append(high)
        lows.append(low)

fig, ax = plt.subplots()
ax.plot(dates, averages)
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='cyan')
plt.title("Daily average Osaka temps, 2020-2021", fontsize=20)
plt.xlabel("", fontsize=14)
plt.ylabel("Temperature(C)", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(labelsize=14)
plt.grid()
plt.show()
