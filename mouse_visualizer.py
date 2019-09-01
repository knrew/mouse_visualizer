import sys
import matplotlib.pyplot as plt
# import matplotlib.animation as animation
from os.path import expanduser

import csv_reader


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


def draw(maze_data_name, search_route_name, optimal_route_name):
    fig = plt.figure(1)
    # ax = fig.add_subplot(111)

    maze_data = csv_reader.read_csv(maze_data_name)
    search_route_data = csv_reader.read_csv(search_route_name)
    optimal_rx, optimal_ry = csv_reader.read_csv_xy(optimal_route_name)

    plt.grid(True)
    plt.axis("equal")

    # start = [maze_data[0][6], maze_data[0][6]]
    # goal = [maze_data[0][8], maze_data[0][9]]

    draw_maze(maze_data)

    #
    # draw search process
    #
    point, = plt.plot(0.5, 0.5, "ob")
    for i, row in enumerate(search_route_data):
        point.remove()
        point, = plt.plot(row[0] + 0.5, row[1] + 0.5, "ob")
        fill_square(row[0], row[1])
        plt.text(row[0] + 0.5, row[1] + 0.5, str(i),fontsize=15, color="b")
        plt.pause(0.01)

    #
    # draw optimal route
    #
    optimal_rx = [n + 0.5 for n in optimal_rx]
    optimal_ry = [n + 0.5 for n in optimal_ry]
    plt.plot(optimal_rx, optimal_ry, "-r")

    plt.show()
    print("fin")


if __name__ == '__main__':
    # default file name
    root = expanduser("~/micromouse/")
    maze_data_name = root + '/maze_data/maze8x8.csv'
    search_route_name = root + '/search_route.csv'
    optimal_route_name = root + '/optimal_route.csv'

    args = sys.argv
    for i, arg in enumerate(sys.argv):
        if i == 1:
            maze_data_name = arg
        if i == 2:
            search_route_name = arg
        if i == 3:
            optimal_route_name = arg

    draw(maze_data_name, search_route_name, optimal_route_name)
