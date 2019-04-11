def quzheng(x):
    x=int(x)
    if x%5 !=0:
        a = x%10
        if a==1 or a==2 or a==0:
            x=x//10*10
        elif a==8 or a==9:
            x=x//10*10 +10
        else:
            x=x//10*10+5
    else:
        x=x
    return x