def number_range(min_value, max_value, step):
    ans_ls = []
    for i in range(min_value, max_value + 1, step):
        ans_ls.append(i)
    print(ans_ls)
    
number_range(10, 40, 5)# -> [10, 15, 20, 25, 30, 35, 40]
number_range(14, 24, 3)# -> [14, 17, 20, 23]
number_range(8, 35, 6)# -> [8, 14, 20, 26, 32]
