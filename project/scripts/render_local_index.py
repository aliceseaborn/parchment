import os

def render_local_index(directory):
    directories = str()
    pages = str()
    files = os.listdir(directory)
    for file in files:
        if file[0] != "." and file[0:2] != "0-":
            if os.path.isdir(directory+"/"+file):
                directories += f"\t{file}/0-index.rst\n"
            elif os.path.isfile(directory+"/"+file):
                pages += f"\t{file}\n"
    return "\n\n\n.. toctree::\n\t:maxdepth: 1\n\n"+directories+pages+"\n"

