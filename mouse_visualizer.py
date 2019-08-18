import matplotlib.pyplot as plt
import matplotlib.animation as animation
from os.path import expanduser

import csv_reader

home = expanduser("~/")
maze_data_name = home + '/micromouse/maze8x8.csv'
search_route_name = home + '/micromouse/search_route.csv'
opt_route_name = home + '/micromouse/optimal_route.csv'


def draw_maze(data):
    obj = []

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
            obj.append(plt.plot(wx, wy, 'k'))
        if row[east] == 1:
            # print("east")
            wx = [row[cx] + 1, row[cx] + 1]
            wy = [row[cy], row[cy] + 1]
            obj.append(plt.plot(wx, wy, 'k'))
        if row[south] == 1:
            # print("south")
            wx = [row[cx], row[cx] + 1]
            wy = [row[cy], row[cy]]
            obj.append(plt.plot(wx, wy, 'k'))
        if row[west] == 1:
            # print("west")
            wx = [row[cx], row[cx]]
            wy = [row[cy], row[cy] + 1]
            obj.append(plt.plot(wx, wy, 'k'))

    obj.append(plt.plot(row[sx] + 0.5, row[sy] + 0.5, "og"))
    obj.append(plt.plot(row[gx] + 0.5, row[gy] + 0.5, "xg"))
    return obj


def fill_square(x, y, color='y', alpha=0.5):
    fill_x = [x, x + 1, x + 1, x]
    fill_y = [y, y, y + 1, y + 1]
    return plt.fill(fill_x, fill_y, color=color, alpha=alpha)


def main():
    fig = plt.figure(1)
    plt.grid(True)
    plt.axis("equal")

    # ax = fig.add_subplot(111)

    maze_data = csv_reader.read_csv(maze_data_name)
    start = [maze_data[0][6], maze_data[0][6]]
    goal = [maze_data[0][8], maze_data[0][9]]
    draw_maze(maze_data)

    ims = []

    search_rx, search_ry = [], []
    search_route_data = csv_reader.read_csv(search_route_name)
    point, = plt.plot(-1, -1, "ob")
    for i, row in enumerate(search_route_data):
        point.remove()
        point, = plt.plot(row[0] + 0.5, row[1] + 0.5, "ob")
        fill_square(row[0], row[1])
        plt.pause(0.05)

    opt_rx, opt_ry = csv_reader.read_csv_xy(opt_route_name)
    opt_rx = [n + 0.5 for n in opt_rx]
    opt_ry = [n + 0.5 for n in opt_ry]

    # plt.plot(search_rx, search_ry, "ob")
    plt.plot(opt_rx, opt_ry, "-r")
    plt.show()
    print("fin")


if __name__ == '__main__':
    main()
