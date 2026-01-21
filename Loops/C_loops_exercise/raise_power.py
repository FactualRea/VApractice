def raise_power(num, exponent):
    answer = 1
    for n in range(exponent):
        answer *= num
    print(answer)

raise_power(2, 5)  #-> 32
raise_power(4, 3)  #-> 64
raise_power(10, 4) #-> 10000
raise_power(7, 2)  #-> 49