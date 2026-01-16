def funny_sound(str1, str2):
    word = str1[0:3:] + str2[0:3:]
    return word

print(funny_sound("tiger", "spoon"))       # "tigspo"
print(funny_sound("computer", "phone"))    # "compho"
print(funny_sound("skate", "bottle"))      # "skabot"
print(funny_sound("frog", "ashtray"))      # "froash"
