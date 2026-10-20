print("===AREA CALCULATOR===")
print("SHAPE-IN-FOCUS")

print("1.SQUARE")

print("2.TRIANGLE")

print("3.PARALLELOGRAM")

print("4.CIRLCE")

AREA=int(input("CHOOSE THE SHAPE"))

if AREA=="1":
    s= int(input("ENTER WIDTH "))
    print(s+"m")
    u=s*s
    print(u + "sq.m")