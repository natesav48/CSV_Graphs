import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('crash_catalonia.csv', 'r') as csvfile:
    csvplots = csv.reader(csvfile, delimiter=',')

    for row in csvplots:
        x.append(row[0].strip('"'))
        y.append(int(row[1].strip('"')))

plt.bar(x, y)
plt.ylabel("car crashes")
plt.xlabel("day of the week")
plt.title("car crashes per day of the week")




#second one

with open('nates_file.csv', 'r') as csvfile:
    csvplots = csv.reader(csvfile, delimiter=',')

    for row in csvplots:
        x.append(row[0].strip('"'))
        y.append(int(row[1].strip('"')))

x = []
y = []


plt.plot(x, y)


plt.title("Simple Plot")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()
