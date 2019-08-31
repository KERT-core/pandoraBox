#!/usr/bin/python3
# -*- coding: utf-8 -*-

#default two class object comparison
class numbering:
    def __init__(self, num1, num2):
        super(numbering, self).__init__()
        self.num1 = num1
        self.num2 = num2

#Comparing two class object with solution
class numbering_improved:
    def __init__(self, num1, num2):
        super(numbering_improved, self).__init__()
        self.num1 = num1
        self.num2 = num2

    def __eq__(self, other):
        if not isinstance(other, numbering_improved):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.num1 == other.num1 and self.num2 == other.num2

    def __hash__(self):
        return hash(('num1', self.name, 'num2', self.lineNum))

if __name__ == "__main__":
    aNum = numbering(1, 2)
    bNum = numbering(1, 2)

    if aNum == bNum:
        print("true")
    else:
        print("false")
    #This provides output of False

    #With Implementation of __eq__
    aNumI = numbering_improved(1, 2)
    bNumI = numbering_improved(1, 2)

    print(aNumI.__eq__(bNumI))
    #This Provides Output of True

    #With Implementation of __hash__
    aNumI_h = numbering_improved(1, 2)
    bNumI_h = numbering_improved(1, 2)

    if aNumI_h == bNumI_h:
        print("True")
    else:
        print("Talse")
