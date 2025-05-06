
# Mathematical Way
no = 123
while no > 0:
    dgt = no % 10       # Getting the unit digit
    no //= 10
    print (dgt, end=" ")



# Pythonic Way
no = 123
generated_no = list(str(no))
print(generated_no)



# Recursive Way
no = 123
def findDgt(no : int):
    if no == 0:
        return
    print(no%10, end=" ")
    findDgt(no // 10)
findDgt(no)