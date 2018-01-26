from random import shuffle
def rand_PW(l,u,n,s,min_char):
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
    PW = low[:l]+upp[:u]+num[:n]+spec[:s]+big[:min_char-l-u-n-s]
    shuffle(PW)
    PW_str = ""
    for i in range(len(PW)):
        PW_str = PW_str + PW[i]

    print (PW_str);
