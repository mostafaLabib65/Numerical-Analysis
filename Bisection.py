def bisection(Xl,Xu,es,iterations):
    Xl = float(Xl)
    Xu = float(Xu)
    es = float(es)
    iterations = int(iterations)
    Xo = 0
    for i in range (iterations):
        Xr = (Xl + Xu) /2
        ea = abs((Xr - Xo)/Xr)
        if(ea < es):
            return Xr
        if (((pow(Xr,3) - 25) * (pow(Xl,3) -25)) < 0 ):
            Xu = Xr
        elif (((pow(Xr,3) - 25) * (pow(Xl,3) -25)) > 0 ):
            Xl = Xr
        else:
            return Xr
        Xo = Xr
        print(i)
    return Xr

print(bisection(2,3,pow(10,-4),500))