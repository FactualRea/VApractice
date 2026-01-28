def print_combinations(arr1, arr2):
    for i in arr1:
        for j in arr2:
            print(i, j)

colors = ["gray", "cream", "cyan"]
clothes = ["shirt", "flannel"]
print_combinations(colors, clothes)