#!/usr/bin/python3
# -*- coding: utf-8 -*-

class numbering:
    def __init__(self, num1, num2):
        super(numbering, self).__init__()
        self.num1 = num1
        self.num2 = num2

if __name__ == "__main__":
    a = numbering(1, 2)
    print(a.num1)
