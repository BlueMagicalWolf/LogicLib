def and_g(a, b):
    ab = a+b
    if ab == 2:
        z = "1"
    else:
        z = "0"
    return(z)

def buf(a):
    z = a
    return(z)

def or_g(a, b):
    ab = a+b
    if ab == 0:
        z = "0"
    else:
        z = "1"
    return(z)

def xor_g(a, b):
    ab = a+b
    if ab == 1:
        z = "1"
    else:
        z = "0"
    return(z)

def inv(a):
    if a == 1:
        z = "0"
    else:
        z = "1"
    return(z)

def nand_g(a, b):
    ab = a+b
    if ab == 2:
        z = "0"
    else:
        z = "1"
    return(z)

def nor_g(a, b):
    ab = a+b
    if ab == 0:
        z = "1"
    else:
        z = "0"
    return(z)

def xnor_g(a, b):
    ab = a+b
    if ab == 1:
        z = "0"
    else:
        z = "1"
    return(z)
