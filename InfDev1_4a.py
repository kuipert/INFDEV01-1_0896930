def convert(_s, x): #returns converted value (from _s to c), or null if input is wrong
    if _s == "c":
        return x
    if _s == "k":
        return x - 273.15
    if _s == "f":
        return ((x - 32) / (9/5))
    return

def calc(_s, x): #returns converted value (from c to _s), or null if input is wrong
    if _s == "c":
        return x
    if _s == "k":
        return x + 237.15
    if _s == "f":
        return (x * (9/5) + 32)
    return

def tempCalc():
    print("From what type to what type do you want to calculate?")
    print(" C = Celcius \n K = Kelvin \n F = Fahrenheit")
    typeA = str.lower(raw_input("Type the first letter of the first type \n"))
    typeB = str.lower(raw_input("Type the first letter of the second type \n"))
    num = input("Type the value of what you want to convert \n")
    try:
        c = convert(typeA, num)
        y = calc(typeB, c)
        print(str(round(y, 2)) + str.upper(typeB))
    except:
        print("something went wrong, please try again with different values")

def absCalc():
    x = input("What number do you want an absolute value of? \n")
    absX = abs(x)
    print("The absolute value of " + str(x) + " is " + str(absX))

prg = input("Choose what program to run \n (1 for temperature calculator, 2 for calculating absolute numbers \n")
if prg == 1:
    tempCalc()
elif prg == 2:
    absCalc()
else:
    print("No program was chosen \n shutting down...")