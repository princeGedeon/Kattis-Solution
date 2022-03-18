from math import floor

tb,lr=0,0
for i in range(int(input())):
    t,b,l,r=list(map(int,list(input())))
    tb +=0 if t==1 else 1
    tb += 0 if b== 1 else 1
    lr += 0 if l== 1 else 1
    lr += 0 if r== 1 else 1
mins=min(floor(tb/2),floor(lr/2))
print(mins,tb-mins*2,lr-mins*2)