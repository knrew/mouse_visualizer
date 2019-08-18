import matplotlib.pyplot as plt
import csv

maze_data_name = '../maze8x8.csv'
search_route_name = '../search_route.csv'
opt_route_name = '../opt_route.csv'

fig = plt.figure(1)
ax = fig.add_subplot(111)


def plot_maze(data):
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

    for row in data:
        if row[north] == 1:
            # print("north")
            wx = [row[cx], row[cx] + 1]
            wy = [row[cy] + 1, row[cy] + 1]
            im = plt.plot(wx, wy, 'k')
        if row[east] == 1:
            # print("east")
            wx = [row[cx] + 1, row[cx] + 1]
            wy = [row[cy], row[cy] + 1]
            plt.plot(wx, wy, 'k')
        if row[south] == 1:
            # print("south")
            wx = [row[cx], row[cx] + 1]
            wy = [row[cy], row[cy]]
            plt.plot(wx, wy, 'k')
        if row[west] == 1:
            # print("west")
            wx = [row[cx], row[cx]]
            wy = [row[cy], row[cy] + 1]
            plt.plot(wx, wy, 'k')

    plt.plot(row[sx] + 0.5, row[sy] + 0.5, "og")
    plt.plot(row[gx] + 0.5, row[gy] + 0.5, "xg")

    ax.grid(which="major", axis="x", color="k", alpha=0.5, linestyle="-", linewidth=1)
    ax.grid(which="major", axis="y", color="k", alpha=0.5, linestyle="-", linewidth=1)

    plt.grid(True)
    plt.axis("equal")


def read_csv(file_name):
    data = []
    with open(file_name, newline='') as f:
        dataReader = csv.reader(f)
        header = next(dataReader)
        for row in dataReader:
            for i, c in enumerate(row):
                row[i] = float(c)
            data.append(row)
    return data


def read_csv_xy(file_name):
    x, y = [], []
    with open(file_name, newline='') as f:
        dataReader = csv.reader(f)
        header = next(dataReader)
        for row in dataReader:
            for i, c in enumerate(row):
                row[i] = int(c)
            x.append(row[0])
            y.append(row[1])
    return x, y


def main():
    maze_data = read_csv(maze_data_name)
    plot_maze(maze_data)

    search_route_data = read_csv(search_route_name)
    for row in search_route_data:
        plt.plot(row[0] + 0.5, row[1] + 0.5, "ob")
        plt.pause(0.01)

    opt_rx, opt_ry = read_csv_xy(opt_route_name)
    opt_rx = [n + 0.5 for n in opt_rx]
    opt_ry = [n + 0.5 for n in opt_ry]
    plt.plot(opt_rx, opt_ry, "-r")

    plt.show()
    print("fin")


if __name__ == '__main__':
    main()
