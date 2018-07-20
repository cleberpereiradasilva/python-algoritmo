#pg
q=2
a1=1
n=10
f=[a1]
for i in range(1,10):
    a1 *= q
    f.append(a1)
print(f)

#find a position
q=2
a1=1
n=10 #position
An = a1 * q**(n-1)
print(An)


#sum elements
q=2
a1=1
n=3
Sn = (a1 * (q**n - 1))/(q -1)
print(Sn)
