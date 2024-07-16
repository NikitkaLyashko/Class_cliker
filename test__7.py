z=[]
d=[]
for i in range(0,27,1):
    if i%2==0:
        m=2*i-1
        z.append(m)

    else:
        n=i**2+1
        z.append(n)


for s in z:
    if s<2.5:
        d.append(2.5*s)
    if s>=2.5:
        d.append(s/2.5)



