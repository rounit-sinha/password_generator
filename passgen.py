
try:

    from string import ascii_letters, digits, punctuation, join

except ImportError:

    from string import ascii_letters, digits, punctuation

from random import choice, sample, randint


def isEven(integer):

    """Return Boolean: True if input is even, False if not."""

    return integer % 2 == 0



def RandPass(size = 8):

    """This is the password generator"""

    s0 = "!@#$%^&*- _~+-=" 
    s1 = ascii_letters 
    s3 = digits
    

    s = s0 + s1

    s_full = s + s3

    passlen = size.get()

    new_password = ""


    if isEven(passlen) == True:

        front = passlen // 5

    else:

        front = passlen // 2

    mid = 2

    previous = passlen - (front + mid) - 1



    pass0 = "".join(choice(s0)) 
    pass1 = "".join(sample(s_full,front ))

    pass2 = "".join(sample(s3,mid))

    pass3 = "".join(sample(s, previous ))

    if passlen != len(pass0 + pass1 + pass2 + pass3):

        pass2 = "".join(sample(s3,passlen - (front+previous+1) ))



    if pass3[:-1] == ' ': 
        temp = list(pass3)

        temp[:-1] = choice(s)

        pass3 = ''.join(str(e) for e in temp)

    new_password = pass0 + pass1 + pass2 + pass3    

    

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



