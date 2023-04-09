a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180:
    print("Error")
else:
    if b == c and a == b :
        print("Equilateral")
    elif (a == b or b == c or a == c) and a != 60:
        print("Isosceles")
    else:
        print("Scalene")