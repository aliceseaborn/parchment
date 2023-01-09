import os

def recursively_list_directories(root_directory, directories):
    for file in os.listdir(root_directory):
        if file[0] != ".":
            directory = os.path.join(root_directory, file)
            if os.path.isdir(directory):
                directories.append(directory)
                recursively_list_directories(directory, directories)

