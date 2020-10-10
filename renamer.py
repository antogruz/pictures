#!/usr/bin/env python3
from unittests import assert_equals, Tester
import re

class Renamer():
    def __init__(self, formats):
        self.formats = formats

    def rename(self, s):
        for f in self.formats:
            if f.belongs(s):
                return f.rename(s)
        return s

class WAformat():
    def belongs(self, s):
        return "IMG" in s

    def rename(self, s):
        s = re.sub("IMG-", "", s)
        return dashToUnderscore(s)

class SignalFormat():
    def belongs(self, s):
        return "signal" in s

    def rename(self, s):
        s = re.sub("signal-", "", s)
        s = re.sub("-", "", s, 2)
        return dashToUnderscore(s)

def dashToUnderscore(s):
    return re.sub("-", "_", s)

class PicturesTester(Tester):
    def __init__(self):
        self.renamer = Renamer([WAformat(), SignalFormat()])

    def rename(self, s):
        return self.renamer.rename(s)

    def testUnknownFormatStaysTheSame(self):
        name="unknown_format.jpg"
        assert_equals(name, self.rename(name))

    def testWAformatIsTransformed(self):
        assert_equals("20200929_WA0001.jpg", self.rename("IMG-20200929-WA0001.jpg"))
        assert_equals("20200930_WA0013.jpg", self.rename("IMG-20200930-WA0013.jpg"))

    def testSignalFormatIsTransformed(self):
        assert_equals("20200912_115134.jpg", self.rename("signal-2020-09-12-115134.jpg"))

if __name__ == "__main__":
    PicturesTester().runTests()

