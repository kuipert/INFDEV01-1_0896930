#encryption program: changes text N places on the alphabet
s = raw_input("Enter what text to encrypt \n")
x = input("Enter how many places to change the text \n")
alphaLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphaUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
newS = ""
for i in range(len(s)):
    if s[i].islower():
        newS += alphaLower[(alphaLower.index(s[i]) + x) % 26]
    elif s[i].isupper():
        newS += alphaUpper[(alphaUpper.index(s[i]) + x) % 26]
    else:
        newS += s[i]
print(newS)