def sum_up_to(num):
    sum = 0
    for n in range(1, num+1):
        sum = sum + n
    print(sum)

sum_up_to(4)  #-> 10
sum_up_to(5)  #-> 15
sum_up_to(2)