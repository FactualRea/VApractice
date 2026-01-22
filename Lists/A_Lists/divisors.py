def divisors(num):
    div_list = []
    for n in range(1, num+1):
        if num % n == 0:
            div_list.append(n)
    print(div_list)

divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]
