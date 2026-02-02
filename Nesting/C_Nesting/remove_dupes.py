def remove_dupes(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(remove_dupes(["x", "y", "y", "x", "z"]))  # ['x', 'y', 'z']
print(remove_dupes([False, False, True, False]))  # [False, True]
print(remove_dupes([42, 5, 7, 42, 7, 3, 7, 7]))  # [42, 5, 7, 3]
