#final_problem and solution
#question 1
#성적이 낮은 학생 순서대로 출력하기
#입력조건[첫 번째 줄에 학생수 N이 입력된다. 두번째 줄부터 학생 이름과 점수가 순서대로 입력된다.]
#출력조건[성적이 낮은 순서대로 학생이름 출력, 성적이 같은 경우에는 순서 상관 없음]
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
#나이순 정렬
#입력조건[첫번재 줄에 회원 수 N이 입력된다, 두번째 줄 부터 N개의 회원의 나이와 이름이 주어진다.]
#출력조건[나이가 작은 순서대로 출력]
n = int(input())
L=[]

for i in range(n):
    a,b = input().split()
    L.append([int(a),b])
    
L = sorted(L, key=lambda x:x[0])

for i in L:
    print(i[0], i[1])


#question 3
#두 배열의 원소 교체
#목표: 길이 N인 배열 A,B에 대해서 A의 원소를 K<=번 B의 원소와 바꿔서 배열 A의 모든 원소의 합이 최대로 하는것
#입력조건[첫번째 줄에 N과 K 입력,두번째 줄에 N개의 배열 A의 원소가 입력]
#출력조건[배열 A의 모든 원소의 합]

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
#입력조건[첫번째 줄에는 수열의 크기를 입력받고 그 이후 부터는 수열을 입력]
#출력조건[최대인 수열의 합]
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

#문제 1
#입력 조건[첫 번째 줄에 입력받을 개수 입력, 두번째 줄에 숫자가 공백으로 구분, 세번째 줄에 찾고자 하는 숫자의 수 입력, 네번째 쭐에 차즌 ㄴ숫자가 주어짐]
#출력 조건[각 숫자가 존재하면 yes, 아니면 no 가 출력된다]
#여기서 언어가 파이썬이니까 필요가 없음 사실상(입력받을 개수입력)
n= int(input()) 
L = list(map(int,input().split()))

nf = int(input())
Lf = list(map(int,input().split()))

L.sort()

for i in Lf:
    idx = BinSearch(L,i)
    if idx == -1:
        print("no", end="")
    else:
        print("yes", end="")
# Case 1 중복 제거 + 정렬
L = list(map(int,input().split()))

nL=[]
for i in L:
    idx = LinearSearch(nL,i)
    if idx == -1:
        nL.append(i)
        
nL.sort()
print(nL)

#정렬 후 중복 제거 (중복 더 많을때 효율적임!!)
L.sort()
ret = [L[0]]

for i in range(1, len(L)):
    if L[i]!=L[i-1]:
        ret.append(L[i])
        
print(ret)


def compare_q2():
     for i in range(10,10000,1000):
         L=[]
         for _ in range(i):
             L.append(random.randrange(i>>1))
             
         delsort=0
         sortdel=0
        
         start = time.time()
        
         nL=[]
         for i in L:
            idx = LinearSearch(nL,i)
            if idx == -1:
                nL.append(i)
            nL.sort()
            end = time.time()
            delsort = delsort + (end-start)
            
            L.sort()
            ret =[L[0]]
            for i in range(1, len(L)):
                if L[i]!=L[i-1]:
                    ret.append(L[i])
            end = time.time()
            sortdel = sortdel+(end-start)
            
            print(f"Delete and sort : {delsort: .5f} sec")
            print(f"Sort and delete : {sortdel: .5f} sec")
            
#week 12
#탐색 문제: 빨대 자르기
#입력[첫째줄에는 가지고 있는 빨대 개수 N과 필요한 빨대수 K가 입력된다. 그 후 빨대의 길이가 N개 입력된다.
#출력[K개를 만들 수 있는 최대 빨대의 길이가 출력된다, K개 보다 많이 만드는 것도 K개를 만드는것에 포함
#이미 자른 빨대는 붙일 수 없다.
#결국 자르는 길이를 이진탐색으로 구하는것!=>시작과 끝을 알아야됨
n, k = map(int,input().split())
L=[]

for _ in range(n):
    a=int(input())
    L.append(a)
    
    
def find_max(L):
    ret = L[0]
    for i in range(1, len(L)):
        if L[i]>ret:
            ret = L[i]
    return ret
     
#탐색
start = 1
end = max(L)
best = 0

while start<=end:
    mid = (start+end)>>1 #자르는 길이
    tmp = 0 #mid로 잘랐을때 나오는 갯수
    for i in L:
        tmp = tmp +(i//mid)
    if tmp>=k: #찾음
        best = mid
        start = mid+1 #찾았지만, 종료하지 않고 더 길게 자를 수는 없는지?
    else:
        end = mid-1



#문제1: 중복이 있는 배열을 중복 없이 정렬하는 함수 만들기(using BST)
#입력[중복이 있는 정렬된지 않는 배열]
#출력[중복없이 정렬된 배열] #위에 insert문 부터 보면됨!!
print("====================")
B=[1,4,2,3,1,4,2,3,1,2]
p1 = bstree()
for i in B:
    p1.insert(i)
    
p1.print_tree()
ret = p1.inorder_stact()
print(ret)