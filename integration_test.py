#!/usr/bin/env python3

import os

input = ["20200929_131032.jpg", "IMG-20200929-WA0001.jpg", "signal-2020-09-12-115134.jpg"]
expected = ["20200929_131032.jpg", "20200929_WA0001.jpg", "20200912_115134.jpg"]
test_dir = "test-tmp"

def main():
    create_working_dir()
    run_program()
    check_dir()

def create_working_dir():
    os.system("mkdir " + test_dir)
    for f in input:
        os.system("touch {}/{}".format(test_dir, f))

def run_program():
    os.system("./pictures_rename.py {}".format(test_dir))

def check_dir():
    os.system("ls {}".format(test_dir))
    os.system("rm -r {}".format(test_dir))

main()
