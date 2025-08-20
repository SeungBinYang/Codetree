a,b,c = map(int,input().split())

if a>b:
    if b>c:
        if a>c: print(b)
        else: print(a)
    elif a>c: print(c)
    else: print(a)
elif b>c:
    if a>c: print(c)
    else: print(a)
else: print(b)
        