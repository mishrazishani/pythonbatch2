#quad roots
def discri(x,y,z):
dis=(y*y)-4(x*z):
return dis;

def roots(a1,b1,d1):
r1=(-b1+cmath.sqrt(d1))/(2*a1)
r2=(-b1-cmath.sqrt(d1))/(2*a1)
return r1,r2;

print("enter the coefficients")
a=float(input("a- "))
b=float(input("b- "))
c=float(input("c- "))

d=discri(a,b,c)

if(d==0):
    r2,r1=roots(a,b,c)
    print("real and equal roots")
    print("r1","\n r2")
    
 elif(d>0):
    print("roots are distinct and real")
    print("r1","\n r2")
 else:
    print("roots are imaginary")
    r2,r1=roots(a,b,d)
    print ("r1","\n r2")
    
