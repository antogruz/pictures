#!/usr/bin/env python3

from renamer import Renamer, WAformat, SignalFormat
import sys
import os

def main():
    working_directory = sys.argv[1]

    renamer = Renamer([WAformat(), SignalFormat()])
    for f in os.listdir(working_directory):
        if f != renamer.rename(f):
            os.system("mv {}/{} {}/{}".format(working_directory, f, working_directory, renamer.rename(f)))

main()
