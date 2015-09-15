import sys
import time

def checkBounds(x): #returns x when 0 < x < 20 else returns 0
    if (x == abs(x) & x <= 20):
        return x
    print("value out of bounds!")
    return 0

def printSquare(x): #draws a square with the size x*x
    for i in range(0, x): #draws first row
        sys.stdout.write("* ")
    sys.stdout.write('\n')
    if (x > 2):
        for i in range(1, x - 1): #draws all rows except first and last
            sys.stdout.write("* ") #draws first dot in row
            for j in range(1, x - 1): #draws all but first and last dots in row
                if (i >= x - j):
                    sys.stdout.write("  ")
                else:
                    sys.stdout.write("* ")
            sys.stdout.write("* ") #draws last dot in row
            sys.stdout.write('\n')
    if (x > 1):
        for i in range(0, x):
            sys.stdout.write("* ") #draws last row if x>1
        sys.stdout.write('\n')
        return

print("This is the square builder. This program prints a square with the top left corner colored, and the bottom right empty." + '\n')
sizeStr = raw_input("Please insert a number between 1 and 20" + '\n')

try:
    size = int(sizeStr)
    printSquare(checkBounds(size))
except ValueError:
    print("this is not a number!" + '\n')
time.sleep(5)
