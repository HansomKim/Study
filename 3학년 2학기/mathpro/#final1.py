#final1
n=int(input())
L=[]
for i in range(n): 
    s=input()
    if s not in L:
        L.append(s)
L.sort(key=lambda x:(-len(x),x))
for i in L:
    print(i)
