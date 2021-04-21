import numpy as np

a=lambda x1,x2,x3:[
    (((x1-34.05)**2)+((x2+56.05)**2)+((x3-0)**2)-137.10**2),
    (((x1-82.46)**2)+((x2-0)**2)+((x3-0)**2)-145.97**2),
    (((x1-74.63)**2)+((x2+31.35)**2)+((x3-0)**2)-144.93**2)
    ]
b=lambda x1,x2,x3:[
    [2*(x1-34.05),2*(x2+56.05),2*(x3)],
    [2*(x1-82.46),2*(x2-0),2*(x3)],
    [2*(x1-74.63),2*(x2+31.35),2*(x3)]
    ]

def metodo_new(a,b,ini,tol):
    x=ini
    error=1*10**3
    n=0
    while error>tol:
        dx=-np.linalg.solve(b(*x),a(*x))
        error=np.linalg.norm(dx)/np.linalg.norm(x)
        x+=dx
        n+=1
    print(round(x[0],2),"|",round(x[1],2),"|",round(x[2],2))

ini=[1,1,1]
tol=1*10**-5
metodo_new(a,b,ini,tol)