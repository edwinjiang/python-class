#!/usr/bin/python
#encoding:utf8

import random

print "You have three chances to guess"

for i in range(1,4):
    inputvalue=raw_input("input number between 12 to 20:")
    randvalue = random.randint(12,20)
    if (int(inputvalue) == randvalue):
        print "Configuration! you are right!"
        break
    else:
        print ("you are not right, it should be " ,randvalue)
        yesno = raw_input("continue or not? Yes(y)/No(n)")
        if yesno == 'n':
            break
