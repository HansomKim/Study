#final5

n=int(input())
L=[]
for _ in range(n):
    s=input()
    if s=="delete":
        if len(L)>0:
            L.pop()
    else:
        L.append(int(s))
if len(L)==0:
    print(0)
else:
    print(sum(L))

