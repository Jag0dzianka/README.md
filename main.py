x=int(input("podaj pierwszą liczbę:"))
y=int(input("podaj drugą liczbę:"))
while x!=y:
    if x>y:
        x=x-y
    else:
        y=y-x
print(x)
