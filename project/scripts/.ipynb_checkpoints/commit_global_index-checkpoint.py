def commit_global_index(directory):
    index_file_path = directory+"index.rst"
    remove_index(index_file_path)
    index = render_global_index(directory)
    with open(index_file_path, mode='r') as file:
        content = file.read()
        file.close()
    commit_page_changes(index_file_path, content+index)

