# 2 Pointer way
str = "reefer"
lft_ptr = 0
rgt_ptr = len(str)-1
while rgt_ptr>lft_ptr:
    if str[lft_ptr] != str[rgt_ptr]:
        print('Not a Valid palindrome')
        break
    lft_ptr+=1
    rgt_ptr-=1
else:
    print("Valid Palindrome")

# Pythonic Way
str = "refer"
print("Valid palindrome") if str == str[::-1] else print("Not a valid palindrome")