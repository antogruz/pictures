#!/usr/bin/env python3

from renamer import Renamer, WAformat, SignalFormat
import sys
import os

def main():
    working_directory = sys.argv[1]

    renamer = Renamer([WAformat(), SignalFormat()])
    for f in os.listdir(working_directory):
        mv(working_directory, f, renamer.rename(f))

def mv(dir, a, b):
    if a != b:
        os.rename(path(dir, a), path(dir, b))

def path(dir, name):
    return dir + "/" + name


main()
