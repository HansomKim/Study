#quiz2
n=int(input())
L=[]
for _ in range(n):
    a,b=input().split()
    L.append([int(a),b])
L.sort(key=lambda x:x[0])
for i in L:
    print(i[0],i[1])
