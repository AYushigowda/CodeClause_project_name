# to generate a password with specific restrictions: \
# NO numbers or special characters in 1st position
# NO space at the end of the string
try:
    from string import ascii_letters, digits, punctuation, join
except ImportError:
    from string import ascii_letters, digits, punctuation
from random import choice, sample, randint
# specific imports to make this small, fast, efficient

#=====================================METHODS===================================
def isEven(integer):
    """Return Boolean: True if input is even, False if not."""
    return integer % 2 == 0

def RandPass(size = 8):
    """This is the password generator"""
    s0 = ascii_letters # upper AND lower cases
    s1 = digits
    s3 = "!$%^&*- _~" # this set of special characters contains a space
	# 's3' can be CUSTOMIZED to include only allowed characters
    s = s0 + s1
    s_full = s + s3
    passlen = size.get()
    new_password = ""

    # assigning specific sizes for each section of the pw generated
    if isEven(passlen) == True:
        frnt = passlen // 3
    else:
        frnt = passlen // 2
    mid = 2
    bck = passlen - (frnt + mid) - 1

    p0 = "".join(choice(s0)) # NO punctuations as 1st character!!!
    p1 = "".join(sample(s_full,frnt ))
    p2 = "".join(sample(s3,mid))
    # forces a minimum number of punctuations in the middle
    p3 = "".join(sample(s,bck ))
    # sometimes integer division reduces the size of the desired password length, the following adjusts it back
    if passlen != len(p0 + p1 + p2 + p3):
        p2 = "".join(sample(s3,passlen - (frnt+bck+1) ))

    if p3[:-1] == ' ': # to avoid having an empty space at the end of password
        temp = list(p3)
        temp[:-1] = choice(s)
        p3 = ''.join(str(e) for e in temp)
    new_password = p0 + p1 + p2 + p3    
    
    if passlen <= 8:
        msg = 'VERY WEAK'
        colorVal = "#6d0001"
    elif passlen <=10:
        msg = 'WEAK'
        colorVal = "#cc0000"
    elif passlen <=12:
        msg = 'DECENT'
        colorVal = "#fc8600"
    elif passlen <=14:
        msg = 'GOOD'
        colorVal = "#eae200"
    elif passlen <=16:
        msg = 'STRONG'
        colorVal = "#9ff400"
    elif passlen <=18:
        msg = 'VERY STRONG'
        colorVal = "#007715"
    elif passlen >18:
        msg = 'EXCELLENT'
        colorVal = "#001fef"
    else:
        pass

    return new_password, msg, colorVal
