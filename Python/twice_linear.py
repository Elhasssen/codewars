

n = 100
def dbl_linear(n):
    u=[1]
    if n == 0:
        return u
    else:
        for i in range(n):
            y,z=2*u[i]+1,3*u[i]+1
            u.append(y)
            u.append(z)
            u=sorted(u)
        return u

m = dbl_linear(n)
print(dbl_linear(n))        
