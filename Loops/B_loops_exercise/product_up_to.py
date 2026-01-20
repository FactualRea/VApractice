def product_up_to(num):
    prod = 1
    for n in range(1, num+1):
        prod = prod * n
    print(prod)

product_up_to(4) #-> 24
product_up_to(5) #-> 120
product_up_to(7)