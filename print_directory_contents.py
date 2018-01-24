import os

directories = []
def print_directory_contents(path):
    """
    This function takes the name of a directory
    and prints out the paths files within that
    directory as well as any files contained in
    contained directories.
    This is without using os.walk
    This displays walking through nested structures

    """
    if os.path.isdir(path):
        children = os.listdir(path)
        for child in children:
            child_path = os.path.join(path, child)
            print_directory_contents(child_path)
    else:
        print(path)
        directories.append(path)

    return directories

directories = print_directory_contents('.')
