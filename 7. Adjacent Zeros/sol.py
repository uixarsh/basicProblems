no = 11010

while no>0:
    x = 0 if no%10 == 0 else None
    no//=10
    if x is not None and no%10 == x:
        print("Adjacent zero found")
        break
else:
    print("no adjacent zeros")