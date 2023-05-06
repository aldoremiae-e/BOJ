str = input()
l = len(str)
newstr = ''
for i in range(l):
    if str[i].islower():
        newstr += str[i].upper()
    else:
        newstr += str[i].lower()
print(newstr)