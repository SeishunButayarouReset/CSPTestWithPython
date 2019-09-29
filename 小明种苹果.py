N,M=map(eval,input().split())
a=[]
T,k,P=0,0,0
for i in range(N):
    a.append(list(map(eval,input().split())))
for i in a:
    T+=sum(i)
for i in range(len(a)):
    Pr=0
    for j in range(1,len(a[i])):
        Pr+=a[i][j]
    if abs(Pr)>P:
        P=abs(Pr)
        k=i+1
print("{} {} {}".format(T,k,P))
        
    
