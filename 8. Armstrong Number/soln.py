# General Way
no = 153
saved_no = no
len_of_no = len(str(no))
sum = 0

while no>0:
    temp = (no%10)**len_of_no
    sum+=temp
    no//=10
    
if saved_no == sum:
    print("Armstrong Number")
else:
    print("no")
    
# Pythonic Way
def is_armstrong(n: int) -> bool:
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)
