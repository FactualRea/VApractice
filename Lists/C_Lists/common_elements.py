def common_elements(arr1, arr2):
    nl =[]
    for i in arr1:
        if i in arr2:
            nl.append(i)
    print(nl)

common_elements(["a", "c", "d", "b"], ["b", "a", "y"]) #-> ['a', 'b']
common_elements([4, 7], [32, 7, 1, 4])# -> [4, 7]
