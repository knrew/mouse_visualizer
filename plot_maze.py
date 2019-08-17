import matplotlib.pyplot as plt
import csv
import pandas as pd

file_path = '../maze5x5.csv'

show_animation = True

cx = 0
cy = 1
north = 2
east = 3
south = 4
west = 5
sx = 6
sy = 7
gx = 8
gy = 9

data = []
with open(file_path, newline='') as f:
    dataReader = csv.reader(f)
    header = next(dataReader)
    # print(header)
    for row in dataReader:
        for i, c in enumerate(row):
            row[i] = int(c)
        # print(row)
        data.append(row)
        if row[north] == 1:
            print("north")
            wx = [row[cx], row[cx] + 1]
            wy = [row[cy] + 1, row[cy] + 1]
            plt.plot(wx, wy, 'k')
        if row[east] == 1:
            print("east")
            wx = [row[cx] + 1, row[cx] + 1]
            wy = [row[cy], row[cy] + 1]
            plt.plot(wx, wy, 'k')
        if row[south] == 1:
            print("south")
            wx = [row[cx], row[cx] + 1]
            wy = [row[cy], row[cy]]
            plt.plot(wx, wy, 'k')
        if row[west] == 1:
            print("west")
            wx = [row[cx], row[cx]]
            wy = [row[cy], row[cy] + 1]
            plt.plot(wx, wy, 'k')

plt.plot(row[sx] + 0.5, row[sy] + 0.5, "og")
plt.plot(row[gx] + 0.5, row[gy] + 0.5, "xb")
plt.grid(True)
plt.axis("equal")
plt.show()
print("poyo")
