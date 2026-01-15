if True:
    print("foo")
    
if False:
    print("bar")

#Snippet 0-2
if False or False:
    print("boop")
    
if True or False:
    print("beep")
    
#Snippet 0-3

num = 40

if num > 0:
    print("zip")
    
if num % 2 == 0:
    print("zoop")
    

#Snippet 0-4

word = "jeep"

if word[0] == "d":
    print("yer")
else:
    print("nah")
    

#Snippet 0-5

sentence = "roger that"

if sentence[-1] == "t":
    print("ends in t")
else:
    print("does not end in t")
    
if len(sentence) < 4:
    print("short")
else:
    print("long")

#Snippet 1-0

qty = 38

if qty > 30 and qty % 5 == 4:
    print("swish")
else:
    print("swoosh")
    
if qty > 0:
    print("pos")
    
#Snippet 1-1

a = "celery"
b = "SQUASH"

if a == a.upper():
    print("alpha")

if b == b.upper():
    print("beta")


#Snippet 1-2

number = 9

if number > 4:
    print("ding")
elif number % 3 == 0:
    print("dong")

#Snippet 1-3

z = 12 

if z > 10:
    print("vroom")

if z % 3== 0:
    print("skrrt")

#Snippet 2-1

nonsense = "blog trust fund tattooed williamsburg poke roof party"
has_ok = "ok" in nonsense

if has_ok:
    print("yet")
elif len(nonsense) >10:
    print("yo")
else:
    print("no")

has_zoo = "zoo" in nonsense
has_fun = "fun" in nonsense

if has_zoo and has_ok:
    print("cool")
elif has_ok:
    print("rad")
elif has_fun:
    print("dope")
else:
    print("nope")

#Snippet 2-2

q = 25
if q % 3 == 0 and q % 5 == 0:
    print("both")
elif q % 3 == 0 or q % 5 == 0:
    print("either")
else:
    print("neither")

r = 9
if r % 3 == 0 and r % 5 == 0:
    print("both")
elif r % 3 == 0 or r % 5 == 0:
    print("either")
else:
    print("neither")

s = 15
if s % 3 == 0 and s % 5 == 0:
    print("both")
elif s % 3 == 0 or s % 5 == 0:
    print("either")
else:
    print("neither")