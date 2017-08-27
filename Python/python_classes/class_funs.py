#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : Aug 23, 2017 Wed
class mango:
    def func(self):
        a, b = 8, 9
        return a+b

    def func2(self, x,y):
        c = self.func()
        z = x + y + c
        return z

def main():
    """Run main function."""
    a = mango().func2(1,1)
    print(a)


if __name__ == "__main__":
    main()
