#!/usr/bin/env python3

import os
from unittests import assert_similars

input = ["20200929_131032.jpg", "IMG-20200929-WA0001.jpg", "signal-2020-09-12-115134.jpg", "VID-20200829-WA0006.mp4"]
expected = ["20200929_131032.jpg", "20200929_WA0001.jpg", "20200912_115134.jpg", "20200829_WA0006.mp4"]
test_dir = "test-tmp with spaces"

def main():
    clean()
    create_working_dir()
    run_program()
    check_dir()
    clean()

def create_working_dir():
    run("mkdir '{}'".format(test_dir))
    for f in input:
        run("touch '{}/{}'".format(test_dir, f))

def run_program():
    run("./pictures_rename.py '{}'".format(test_dir))

def check_dir():
    assert_similars(expected, os.listdir(test_dir))

def clean():
    rmdir(test_dir)

def rmdir(d):
    if os.path.isdir(d):
        run("rm -r '{}'".format(d))

def run(cmd):
    os.system(cmd)

main()
