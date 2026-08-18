#final2
N=int(input())
req=list(map(int,input().split()))
req.sort()
s=0
sum=0
for x in req:
    s+=x
    if s<=N:
        sum=x
    else:
        break
print(sum)


#약간의 오류가 있음