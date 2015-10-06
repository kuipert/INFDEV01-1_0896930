s = raw_input("enter your sentence to invert \n")
#print(s[::-1])
ls = list(s)
invS = ""
for i in range(len(ls)):
    invS += ls.pop()
print(invS)