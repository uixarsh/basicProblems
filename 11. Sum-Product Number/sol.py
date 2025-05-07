
def digit_sum(nos : list) -> int:
    return sum(nos)

def digit_product(nos : list) -> int:
    prod = 1
    for no in nos:
        prod*=no
    return prod

num = 144
digit_list = [int(n) for n in str(num)]
sum_prod = digit_sum(digit_list) * digit_product(digit_list)

if num == sum_prod:
    print("The sum-prod is equal")
else:
    print("Not sum-prod")