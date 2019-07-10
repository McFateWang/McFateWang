m=100
r=0.035
rd=0.05
n=3
a=0
b=0

for i in range(1,n+1):
    a+=(m*r*i)/(1+rd)**i
    b+=(m*r)/(1+rd)**i
a=a+m*n/(1+rd)**n
b=b+m/(1+rd)**n

D=a/b
DM=D/(1+rd)
print(b,D,DM)