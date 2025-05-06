
# Loops Way
arr = [1, 2, 3, 4, 5, 6]
length = len(arr)-1
while length != -1:
    print(arr[length], end=" ")
    length-=1

# Pythonic Way
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr[::-1])


# Recursion Way
arr = [1,2,3,4,5,6,7,8,9,10]
def reverse(arr, size):
    if size == -1:
        return
    print(arr[size], end=" ")
    return reverse(arr, size-1)

reverse(arr, len(arr)-1)