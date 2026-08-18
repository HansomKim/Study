#final3
a, b = map(int,input().split())
L=[]

a,b = map(int,input().split())
L=list(map(int,input().split()))
first=-1
last=-1
for i in range(len(L)):
    if L[i]>=a and L[i]<=b:
        first=i
        break
for i in range(len(L)-1,-1,-1):
    if L[i]>=a and L[i]<=b:
        last=i
        break
if first==-1:
    print("None")
else:
    print(first,last)
