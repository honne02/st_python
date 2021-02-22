n=int(input())
xs=[]
qs=[]
for i in range(1,n+1):
    x=int(input())
    xs.append(x)
    q=x*x+2*x+1
    qs.append(q)
print(*xs, sep='\n')
print()
print(*qs, sep='\n')