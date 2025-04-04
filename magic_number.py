import random
import math
import itertools
import os
from time import sleep as slp
from time import time

def addSub(n):
    n = str(n)
    big = int("".join(sorted(n, reverse=True)))
    small = int("".join(sorted(n)))
    return str(big - small)


def isMagic(n):
    maxLengh = 0
    maxNum = 0
    magicNum = 0
    magicNums= []
    for i in range(int("1" + "0"*(n-1)), int("1" + "0"*(n))):
        n = str(i)
        seen = []
        count = 0
        while True:
            new_n = addSub(n)
            count += 1
            if new_n == "0":
                break
            elif new_n in seen:
                magicNum = int(new_n)
                magicSet = seen.copy()
                if count > maxLengh:
                    maxLengh = count
                    maxNum = i
                break
            else:
                seen.append(new_n)
            n = new_n

    if magicNum != int(magicSet[-1]):
        magicNum = [magicSet, magicNum]

    return (maxLengh-1), maxNum, magicNums

 
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    digits = input("Enter the number of digits: ")
    try:
        digits = int(digits)
    except ValueError:
        print("Please enter a valid number.")
        slp(1)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    starttime = time()
    lenghth, num, magicNum = isMagic(digits)
    endtime = time()
    elapsed = endtime - starttime
    os.system('cls' if os.name == 'nt' else 'clear')
    print("The magic number/set is:", magicNum)
    slp(1)
    print("The number with the longest chain is:", num, "with a chain of length", lenghth)
    slp(1)
    print("Elapsed time:", elapsed, "seconds")
    slp(1)
    cont = input("Would you like to try again? (y/n): ")
    if cont.lower() != "y":
        break