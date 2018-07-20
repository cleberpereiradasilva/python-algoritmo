#fibonacci sequence
#Fn = Fn-1 + Fn-2
#ex: F2 = 0,1,1

#exemple 0:
#F6
f=[0,1]
a,b = 0,1
for i in range(1,6):
    a, b = b, b + a
    f.append(b)
print(f)


#exemple 1:
#F6
f=[0,1]
a=0
b=1
for i in range(1,6):
    aux = b
    b += a
    a = aux
    f.append(b)
print(f)

#exemple 2:
f=[0,1]
for i in range(1,6):
    f.append(f[-1]+f[-2])
print(f)


#exemple 3:
def fib(n):
    f=[0,1]
    for i in range(1,6):
        f.append(f[-1]+f[-2])
    return f
f = fib(6)
print(f)
