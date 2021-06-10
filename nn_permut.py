#code
n=99

def small(i):
    t=[]
    while(i>0):
        t.append(i%10)
        i=i//10
    #print(t)
    t=sorted(t)
    #print(t)
    r=0
    for j in range(0,len(t)):
        r=(r*10)+t[j]
    return(r)

count=0
for i in range(0,n):

    k=small(i)
    #print(k)
    if(i==k):
        count+=1
print(count)
