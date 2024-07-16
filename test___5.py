import random
y=[]
x=[]
for b in range(0,27,1):
    n = random.randint(1, 30)
    x.append(n)

for c in x:
    a=6.85*c*c-1.52

    if a<0:
        m=c**3-0.62

    if a>=0:
        v=1/c**2



    y.append(a)





