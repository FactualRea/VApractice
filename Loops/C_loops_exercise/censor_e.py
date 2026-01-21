def censor_e(text):
    sens = ""
    for i in text:
        if i == "e":
            sens += "x"
        else:
            sens += i
    print(sens)
    
censor_e("speedy")  #-> 'sp**dy'
censor_e("pending") #-> 'p*nding'
censor_e("scene")   #-> 'sc*n*'
censor_e("heat")    #-> 'h*at'
