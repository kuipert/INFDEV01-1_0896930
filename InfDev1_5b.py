#program checks on length and amount of different characters and uses an integer number to check it's strength.
s = raw_input("Choose what password to check \n")
strength = 0
lower = False
upper = False
digit = False
nonDigit = False

strength += (len(s) - 8) / 4 #gives +1 for every 4 keys used, starts at -2
for i in s:
    if i.islower():
        lower = True
    elif i.isupper():
        upper = True
    elif i.isdigit():
        digit = True
    else:
        nonDigit = True

if lower == True:
    strength += 1
if upper == True:
    strength += 1
if digit == True:
    strength += 1
if nonDigit == True:
    strength += 1

if strength > 5:
    print("strong")
elif strength > 3:
    print("medium")
else:
    print("weak")