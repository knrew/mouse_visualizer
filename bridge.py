import sys
import subprocess
from os.path import expanduser

import mouse_visualizer


def main(root_directory, program_name, maze_data_name, search_route_name, optimal_route_name):
    print(maze_data_name)

    build_directory = root_directory + "/build/"
    solver_directory = root_directory + program_name

    subprocess.check_call(["mkdir", "-p", build_directory], cwd=root_directory)
    subprocess.check_call(["cmake", solver_directory], cwd=build_directory)
    subprocess.check_call(["make"], cwd=build_directory)

    command = ["./" + program_name, maze_data_name, search_route_name, optimal_route_name]
    subprocess.check_call(command, cwd=build_directory)

    mouse_visualizer.draw(maze_data_name, search_route_name, optimal_route_name)


if __name__ == '__main__':
    # default file name
    program_name = "maze_solver"
    root = expanduser("~/") + "/micromouse/"
    maze_data_name = root + "/maze_data/maze8x8.csv"
    search_route_name = root + "/search_route.csv"
    optimal_route_name = root + "/optimal_route.csv"

    args = sys.argv
    for i, arg in enumerate(sys.argv):
        if i == 1:
            maze_data_name = root + arg
        if i == 2:
            search_route_name = root + arg
        if i == 3:
            optimal_route_name = root + arg

    main(root, program_name, maze_data_name, search_route_name, optimal_route_name)
