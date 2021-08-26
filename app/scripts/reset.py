from os import getcwd, path, makedirs
import shutil


files = [
    "/images"
]


def reset():
    workdir = path.abspath(getcwd()) + "/assets"
    if path.exists(workdir):
        shutil.rmtree(workdir)
        [makedirs(workdir + file) for file in files]
    else:
        [makedirs(workdir + file) for file in files]
