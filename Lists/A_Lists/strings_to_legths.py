def strings_to_lengths(strings):
    len_list = []
    for l in strings:
        len_list.append(len(l))
    print(len_list)

strings_to_lengths(["belly", "echo", "irony", "pickled"]) #-> [5, 4, 5, 7]
strings_to_lengths(["on", "off", "handmade"]) #-> [2, 3, 8]