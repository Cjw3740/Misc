#l,u,n,s specifies the minimum number of lower, upper, numbers, and special characters the password should have
def rand_PW(l,u,n,s,min_char):
    from random import shuffle
    low = list("abcdefghijklmnopqrstuvwxyz")
    upp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num = list("1234567890")
    spec = list("!@#$%^&*?")
    big = low+upp+num+spec
    shuffle(big)
    shuffle(low)
    shuffle(upp)
    shuffle(num)
    shuffle(spec)
    PW = low[:l]+upp[:u]+num[:n]+spec[:s]+big[:max(0,min_char-l-u-n-s)]
    shuffle(PW)
    PW_str = "".join(char for char in PW)
    print (PW_str); 
