# TIM BUCHALKA'S COMPLETE PYTHON MASTERCLASS
# BEGINNING
#
# Created by Tim Buchalka, Jean-Paul Roberts, Tim Buchalka's Learn Programming Academy
#
# Challenge:
#
# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next higher power - putting a 1
# # if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this challenge.
#
# The program should cater for numbers up to 65535, i.e. (2 ** 16) -1
#
# Hint: You will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example: 2 ** 8 raises 2 to the power of 8.
#
# As an optional extra, avoid printing leading zeros.
#
# Once the program is working, modify it to print Octal rather than binary.
#
# END OF THE PART, WRITEN BY THE AUTHORS MENTIONED ABOVE
#
# Authors:
# Tim Buchalka
# https://www.udemy.com/user/timbuchalka/
#
# Jean-Paul Roberts
# https://www.udemy.com/user/jeanpaulroberts/
#
#      link to the Complete Python Masterclass of Tim Buchalka and Jean-Paul Roberts at udemy.com:
#      https://www.udemy.com/python-the-complete-python-developer-course/
#
# END OF CHALLENGE TEXT
#
# BEGINNING OF MY OWN SOLUTION

# Initialization of variables for binary number format
binary16 = 0
binary15 = 0
binary14 = 0
binary13 = 0
binary12 = 0
binary11 = 0
binary10 = 0
binary9 = 0
binary8 = 0
binary7 = 0
binary6 = 0
binary5 = 0
binary4 = 0
binary3 = 0
binary2 = 0
binary1 = 0
binary0 = 0

# Initialization of variables for octal number format
octal7 = 0
octal6 = 0
octal5 = 0
octal4 = 0
octal3 = 0
octal2 = 0
octal1 = 0
octal0 = 0

# Remarks:
# Code duplication is not elegant solution (list of variables from 16 to 0 and 5 to 0)
# The output number could be cleaned from zero at the beginning.
# But the code does what expected to be done.

decimalNumber = int(input("Please give a decimal, integer number between 1 and 65535: "))
if ((decimalNumber < 1) or (decimalNumber > 65535)):
    print("Input number is out of valid range!")
else:
    binary16 = (decimalNumber // (2 ** 16))
    binary15 = (decimalNumber % (2 ** 16)) // (2 ** 15)
    binary14 = (decimalNumber % (2 ** 15)) // (2 ** 14)
    binary13 = (decimalNumber % (2 ** 14)) // (2 ** 13)
    binary12 = (decimalNumber % (2 ** 13)) // (2 ** 12)
    binary11 = (decimalNumber % (2 ** 12)) // (2 ** 11)
    binary10 = (decimalNumber % (2 ** 11)) // (2 ** 10)
    binary9 = (decimalNumber % (2 ** 10)) // (2 ** 9)
    binary8 = (decimalNumber % (2 ** 9)) // (2 ** 8)
    binary7 = (decimalNumber % (2 ** 8)) // (2 ** 7)
    binary6 = (decimalNumber % (2 ** 7)) // (2 ** 6)
    binary5 = (decimalNumber % (2 ** 6)) // (2 ** 5)
    binary4 = (decimalNumber % (2 ** 5)) // (2 ** 4)
    binary3 = (decimalNumber % (2 ** 4)) // (2 ** 3)
    binary2 = (decimalNumber % (2 ** 3)) // (2 ** 2)
    binary1 = (decimalNumber % (2 ** 2)) // (2 ** 1)
    binary0 = (decimalNumber % (2 ** 1)) // (2 ** 0)


    octal5 = (decimalNumber % (8 ** 6)) // (8 ** 5)
    octal4 = (decimalNumber % (8 ** 5)) // (8 ** 4)
    octal3 = (decimalNumber % (8 ** 4)) // (8 ** 3)
    octal2 = (decimalNumber % (8 ** 3)) // (8 ** 2)
    octal1 = (decimalNumber % (8 ** 2)) // (8 ** 1)
    octal0 = (decimalNumber % (8 ** 1)) // (8 ** 0)
print(decimalNumber)

print("")
print("BINARY")
print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(binary16,binary15,binary14,binary13,binary12,binary11,binary10,binary9,binary8,binary7,binary6,binary5,binary4,binary3,binary2,binary1,binary0))
print(bin(decimalNumber))

print("")
print("OCTAL")
print("{}{}{}{}{}{}".format(octal5, octal4, octal3, octal2, octal1, octal0))
print(oct(decimalNumber))

#
# for i in range(17):
#     print("{0:>2} in oct is {0:>0o}".format(i))
#
# for i in range(10):
#     print("8 ** {} = {}".format(i, 8**i))





























