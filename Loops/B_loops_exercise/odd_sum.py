def odd_sum(max_num):
    sum = 0
    for n in range(1, max_num + 1):
        if n % 2 != 0:
            sum = sum + n
    print(sum)

odd_sum(10)
odd_sum(5)