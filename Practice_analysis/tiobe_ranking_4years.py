import csv
import matplotlib.pyplot as plt

filename = 'tiobe_ranking_4years.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    languages,rank2021,rank2016,rank2011,rank2006 = [],[],[],[],[]
    index2021 = header_row.index('2021')
    index2016 = header_row.index('2016')
    index2011 = header_row.index('2011')
    index2006 = header_row.index('2006')
    for row in reader:
        language = row[0]
        try:
            r1 = int(row[index2021])
            r2 = int(row[index2016])
            r3 = int(row[index2011])
            r4 = int(row[index2006])
        except ValueError:
            print(f'データが欠けています{row[0]}')
        else:
            languages.append(language)
            rank2021.append(r1)
            rank2016.append(r2)
            rank2011.append(r3)
            rank2006.append(r4)
fig, ax = plt.subplots()
ax.plot(languages,rank2021)
ax.plot(languages,rank2016)
ax.plot(languages,rank2011)
ax.plot(languages,rank2006)

plt.title("Language Ranking 2006-2021", fontsize=24)
plt.xlabel("Languages", fontsize=14)
plt.ylabel("Years", fontsize=14)
fig.autofmt_xdate()
ax.tick_params(labelsize=14)
ax.set_axisbelow(True)
ax.invert_yaxis()
plt.grid()
plt.show()