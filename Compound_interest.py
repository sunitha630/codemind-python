def c_i(p,r,t):
    a=p*(1+r/100)**t
    return a
p,r,t=map(int,input().split())
am=c_i(p,r,t)
print("{:.2f}".format(am))
    