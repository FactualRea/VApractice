def choose_divisibles(numbers, target):
    div = []
    for i in numbers:
        if i % target == 0:
            div.append(i)
    print (div)
    
choose_divisibles([40, 7, 22, 20, 24], 4)
choose_divisibles([9, 33, 8, 17], 3) 
choose_divisibles([4, 25, 1000], 10) 