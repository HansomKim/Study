#week 11: 탐색
#리스트/배열 내에서 특정 원소를 탐색하는 방법
#순차 탐색(가장 기본적인 탐색 알고리즘->걍 처음부터 하나씩 차례로 확인)==linear search
#시간복잡도: O(n) 데이터가 큰경우 적합 X, 미리 정렬할 필요가 없음
def LinearSearch(L,n):
    for i in range(len(L)):
        if L[i]==n:
            return i #간혹가다가 이상하게 오류뜨면 return 위치 때문에 그럼
    return -1

L=[9,8,1,2,7,3,6,4,5]
#print(LinearSearch(L,3))  #5번째에 있습니다~~
#print(LinearSearch(L,10))


#이진 탐색(Binary Search)
#내부 데이터가 정렬되어있어야만 사용가능하며 배열의 크기가 작을때는 효율적이지 않다.
#정렬이 되어있으면 빠르게 찾기 가능하다 O(log(n))
#각 단계에서 배열의 반을 제거하면서 찾는 알고리즘{가운데 부터 시작⭐️}->반 날리기 가능

def BinSearch(L,n):
    start = 0
    end = len(L)-1
    
    while start<=end:
        middle = (start+end)>>1
        #print("middle :", middle)
        if L[middle]<n:
            end = middle+1
        elif L[middle]>n:
            end = middle-1
        else:
            return middle
        return -1
#결과 프린트는 뒤에 둠

#보간 탐색(Interpolation Search)
#이진탐색의 최적화, 특정한 케이스에서만 적용이 잘됨, 평균 시간 복잡도 O(log(log(n)))
def interSearch(L,n):
    low = 0
    high = len(L)-1
    
    while n>=L[low] and n<=[high] and low<=high:
        x =  ((high-low)*(n-L[low]))//(L[high]-L[low])+low
        #직선의 방정식 (기울기 계산하는거랑 똑같은 방법으로)
        x = int(x)
        #print("x:",x)
        if L[x]==n:
            return x
        elif L[x]<n:
            low = x+1
        else:
            high=x-1
    return -1

#정렬 리스트
L=[]
for i in range(0,100):
    L.append(i)
    
#print("Binary search")
#print(BinSearch(L,30))
#print(BinSearch(L,200))

#print("Inter search")
#print(interSearch(L,30))

#속도비교를 해보자
import time
import random

#정렬된 데이터 -> 크기를 변해가며 linear/bin

def rand_list(n):
    L=[]
    cnt =0
    while cnt<n:
        a = random.randrange(n*100)
        if a not in L:
            L.append(a)
            cnt=cnt+1
    return L

#정렬된 데이터에서 linear/bin 비교
def compare_linear_bin():
    print("==compare_linear_bin==")
    for i in range(10,1000,100):
        print("data length:", i)
        L = rand_list(i)
        L.sort() #정렬
        Ltime=0
        Btime=0
        for j in range(0, 2000):
            n = random.randrange(i*100)
            start = time.time()
            LinearSearch(L,n) #O(n)
            end = time.time()
            Ltime = Ltime +(end-start)
            
            start = time.time()
            BinSearch(L,n) #O(logn)
            end = time.time()
            Btime = Btime +(end-start)
        print(f"Linear Search : {Ltime: .5f} sec")
        print(f"Binary Search : {Btime: .5f} sec") #Binary Search=>확실히 sort 진행하고 하니까 훨 낫구만!
        
        
def compare_linear_bin_unsort():
    print("==compare_linear_bin_unsort==")
    for i in range(10,1000,100):
        print("data length:", i)
        L = rand_list(i)
        L.sort() #정렬
        Ltime=0
        Btime=0
        for j in range(0, 2000):
            n = random.randrange(i*100)
            start = time.time()
            LinearSearch(L,n) #O(n)
            end = time.time()
            Ltime = Ltime +(end-start)
            
            start = time.time()
            BinSearch(L,n) #O(logn)
            end = time.time()
            Btime = Btime +(end-start)
        print(f"Linear Search : {Ltime: .5f} sec")
        print(f"Sort + Binary Search : {Btime: .5f} sec") #Binary Search=>확실히 sort 진행하고 하니까 훨 낫구만!
        

#compare_linear_bin() #정렬확실시-> binary/정렬x -> Linear
#compare_linear_bin_unsort() #한번 찾음 -> Linear

"""
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

 """   
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