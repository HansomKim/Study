#week10 (문제풀이)
#question 1
n = int(input())
L=[]

for i in range(n):
    a,b = input().split()
    print("type a:", type(a))
    print("type b:", type(b))
    L.append([a,int(b)])
    
def ssort(L):
    for i in range(len(L)):
        idx = i
        for j in range(i+1,len(L)):
            if L[idx][1]>L[j][1]:
                idx = j
            L[i],L[idx] = L[idx], L[i]
            
#ssort(L)
L = sorted(L,key = lambda x: x[1]) #이러면 sort 필요 없어지니까

for i in range(len(L)):
    print(L[i][0], end="")
    

#question 2
n = int(input())
L=[]

for i in range(n):
    a,b = input().split()
    L.append([int(a),b])
    
L = sorted(L, key=lambda x:x[0])

for i in L:
    print(i[0], i[1])


#question 3
n, k = map(int, input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

def ssort(L):
    for i in range(len(L)):
        idx = i
        for j in range(i+1, len(L)):
            if L[j]<L[idx]:
                idx = j
        L[i], L[idx] = L[idx], L[i]
        
def ssort_d(L):
    for i in range(len(L)):
        idx = i
        for j in range(i+1, len(L)):
            if L[j]>L[idx]:
                idx = j
        L[i], L[idx] = L[idx], L[i]
        
ssort(A)
ssort_d(B)
#sort + B[::-1] nlogn + n
print("A:", A)
print("B: ",B)


for i in range(k):
    if A[i]<B[i]:
        A[i]=B[i]
    else:
        break
    
print(sum(A))

#question 4: 입력 받는거 정렬해야함
n = int(input())
L = []
for i in range(n):
    L.append(int(input()))
    
L.sort()  #L=[-3,-2,-1,0,0,0,1,5,9,7] 큰 애들은 애초에 묶어버림
start =0
end = len(L)-1
total=0
#음수 부분은 묶는게 좋다. 아니면 0과 곱해서 0으로 만들자!
while start<end:
    if L[start]<1 and L[start+1]<1:
        total = total +(L[start]*L[start+1])
        start = start+2
    else: 
        break

while end>0:
    if L[end]>1 and L[end-1]>1:
        total = total+L[end]*L[end-1]
        end = end-2
        
    else:
        break
    
    print(total)
