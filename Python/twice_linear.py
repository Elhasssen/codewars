

# this one is too complex
def dbl_linear_version(n):
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
     


def dbl_linear(n):
    u = [1]
    x,y = 0,0
    if n == 0 :
        return 0
    else:
        while len(u) <= n:
            a,b=2*u[x]+1,3*u[y]+1
            if a == b :
                u.append(a)
                x += 1 
                y += 1
            elif a>b:
                u.append(b)
                y += 1
            elif b>a:
                u.append(a)
                x += 1   
            
        return u[n]