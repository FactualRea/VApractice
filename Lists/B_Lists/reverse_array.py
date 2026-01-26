def reverse_array(arr):
    nl = []
    for i in range(len(arr)-1, -1):
        nl.append(i)
    print(nl)
    
reverse_array(["zero", "one", "two", "three"])# -> ['three', 'two', 'one', 'zero']
reverse_array([7, 1, 8])# -> [8, 1, 7]