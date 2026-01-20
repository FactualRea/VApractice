def div_by_either(num1, num2, max_num):
    prod = 1
    for n in range(1, max_num):
        if n % num1 == 0 or n % num2 == 0:
            print(n)


div_by_either(4, 3, 16)