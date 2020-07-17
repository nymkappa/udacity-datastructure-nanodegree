#########################################################################################
#
# For this problem, the goal is to write code for finding all files under a directory
# (and all directories beneath it) that end with ".c"
#
#########################################################################################

import os

def find_files(suffix, path, file_list):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system
      file_list(list): list of string representing file names

    Returns:
       a list of paths
    """
    if len(path) == 0:
        return []

    files = os.listdir(path)

    # Do deep field search
    for entry in files:
        # Generate next path
        if path[len(path) - 1] == '/':
            entry = path + entry
        else:
            entry = path + '/' + entry

        # If we have a directory, call self again, otherwise, simply list the file
        if os.path.isdir(entry):
            find_files(suffix, entry, file_list)
        elif entry.endswith(suffix):
            file_list.append(entry)

    file_list.sort()


###############################################################################
# Tests
###############################################################################

print ("Find all .c files in testdir")
file_list = []
find_files(".c", "./testdir", file_list)
print ("Expect: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']")
print ("Output:", file_list, "\n")
assert len(file_list) == 4
assert str(file_list) == "['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']"

print ("Find all .c files in testdir/subdir1")
file_list = []
find_files(".c", "./testdir/subdir1", file_list)
print ("Expect: ['./testdir/subdir1/a.c']")
print ("Output:", file_list, "\n")
assert len(file_list) == 1
assert str(file_list) == "['./testdir/subdir1/a.c']"

print ("Find all .h files in testdir/subdir1")
file_list = []
find_files(".h", "./testdir/subdir1", file_list)
print ("Expect: ['./testdir/subdir1/a.h']")
print ("Output: ", file_list, "\n")
assert len(file_list) == 1
assert str(file_list) == "['./testdir/subdir1/a.h']"

print ("Find all files in testdir/subdir1")
file_list = []
find_files("", "./testdir/subdir1", file_list)
print ("Expect: ['./testdir/subdir1/a.c', './testdir/subdir1/a.h']")
print ("Output: ", file_list, "\n")
assert len(file_list) == 2
assert str(file_list) == "['./testdir/subdir1/a.c', './testdir/subdir1/a.h']"

print ("Find all .c files in testdir/subdir3")
file_list = []
find_files(".c", "./testdir/subdir3", file_list)
print ("Expect: ['./testdir/subdir3/subsubdir1/b.c']")
print ("Output: ", file_list, "\n")
assert len(file_list) == 1
assert str(file_list) == "['./testdir/subdir3/subsubdir1/b.c']"

print ("Find all abcdef files in current directory")
file_list = []
find_files("abcdef", "./", file_list)
print ("Expect: []")
print ("Output: ", file_list, "\n")
assert len(file_list) == 0
assert str(file_list) == "[]"

print ("Find all .gitkeep files in current directory")
file_list = []
find_files(".gitkeep", "./", file_list)
print ("Expect: ['./testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep']")
print ("Output: ", file_list, "\n")
assert len(file_list) == 2
assert str(file_list) == "['./testdir/subdir2/.gitkeep', './testdir/subdir4/.gitkeep']"

print ("Call the function with invalid pattern (None)")
file_list = []
find_files(None, "", file_list)
print ("Expect: []")
print ("Output: ", file_list, "\n")
assert len(file_list) == 0
assert str(file_list) == "[]"

print ("All test passed")

