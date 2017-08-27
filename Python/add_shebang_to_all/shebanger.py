#!/usr/local/bin/python3

import os


def shebang_dir(dir, ext=".py", sb="#!/usr/local/bin/python3"):
    """Add a shebang to the top of every specified file type in a directory.

    Is always recursive.

    shebang_dir(dir, ext=".py", sb="#!/usr/local/bin/python3")

    Args:
        dir: The root directory from which the shebanging should start.
        ext: The file extension that the files you want shebanged should have.
        sb: The shebang that you want added to the top of the file.
    """
    for root, dirs, files in os.walk(dir):  # recursively explore directories
        for file in files:
            if file.endswith(ext):  # right file type
                print("Shebanging", file, "...")
                if root == dir:  # In the original specified directory
                    fullpath = dir
                else:  # in a sub directory
                    fullpath = os.path.join(dir, root)

                with open(os.path.join(fullpath, file), "r+") as f:  # reading and writing
                    data = f.read()  # get contents
                    f.seek(0)  # goto top of file
                    f.write(sb + "\n\n" + data)  # adds shebang to the top
    print("Finished!")
