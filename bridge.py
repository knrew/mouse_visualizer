import subprocess

import mouse_visualizer


#
# build = "./cmake-build-debug/"
# mpl_dir = "./mpl_files/sample/"
# file_list_path = "./mpl_files/sample_list.txt"
# result_path = "./result.txt"


def main():
    micromouse_directory = mouse_visualizer.home + "/micromouse/"
    build_directory = micromouse_directory + "/build/"
    solver_directory = micromouse_directory + "/maze_solver/"
    program_name = "maze_solver"

    subprocess.check_call(["mkdir", "-p", build_directory], cwd=micromouse_directory)
    subprocess.check_call(["cmake", solver_directory], cwd=build_directory)
    subprocess.check_call(["make"], cwd=build_directory)
    
    subprocess.check_call([build_directory + "/maze_solver", mouse_visualizer.maze_data_name, mouse_visualizer.search_route_name, mouse_visualizer.opt_route_name], cwd=build_directory)
    
    mouse_visualizer.main()
    
if __name__ == '__main__':
    main()
