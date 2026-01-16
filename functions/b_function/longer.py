def longer(str1, str2):
    if len(str1) > len(str2):
        return str1
    else:
        return str2

print(longer("drum", "piranha"))       # "piranha"
print(longer("basket", "fork"))        # "basket"
print(longer("flannel", "sustainable"))# "sustainable"
print(longer("disrupt", "ability"))    # "disrupt"
print(longer("bird", "shoe"))          # "bird"