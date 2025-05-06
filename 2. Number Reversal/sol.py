
# Pythonic Way
temp=[]
no=1234560
while no>0:
    temp.append(str(no%10))
    no//=10
x = "".join(temp)
print(int(x))



# Pythonic Way
no = 1234560
temp=""
new_data = list(str(no))[::-1]
for dgt in new_data:
    temp+=dgt
print(int(temp))



# Mathematical Way
no = 123456
rev_no = 0
while no>0:
    temp = no % 10
    rev_no = rev_no*10 + temp
    no //= 10
print(rev_no)



# Recursive Way
no = 1234560
def reverse_no(no : int) -> int:
    if no == 0: 
        return 0
    return (no % 10) * (10 ** (len(str(no)) - 1)) + reverse_no(no//10)

print(reverse_no(no))