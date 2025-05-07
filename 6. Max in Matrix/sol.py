lst = [
    [1,2,3],
    [4,5,16],
    [7,8,9]
]

# General Approach
max_no = lst[0][0]
for row in lst:
    for ele in row:
        if ele > max_no:
            max_no = ele

print(max_no)

# Pythonic Way
max_no = max(ele for row in lst for ele in row)
print(max_no)
