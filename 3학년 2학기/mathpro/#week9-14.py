#week9-14[기말고사 전체 범위]
#수프밍(기말)->알고리즘, 자료구조
#알고리즘: 문제를 푸는 절차/방법-> 주어진 문제를 정확하고 효율적으로 해결
#자료구조: 데이터를 정렬하는 방법
#정렬알고리즘: 데이터를 특정 기준에 따라 순서대로 나열 
#시간 복잡도->주어진 알고리즘이 어느정도의 메모리 복잡도를 사용하는가(?), 프로그램의 입력값의 크기와 연산 수행시간의 상관관계
#Big-O notation: 정의된 함수에서 f<g을 만족하는 것을 의미->지수승 커질수록 복쟙,,
# O(1),O(n),O(nsquare)
#느린 정렬 알고리즘
#native way-선택정렬: 다음 리스트에서 크기가 작은 순서대로 나열하는 방법
def selection_sort(L):
    for i in range(len(L)):
        idx=i
        for j in range(i+1, len(L)):
            if L[j]<L[idx]:
                idx = j
        L[i], L[idx] = L[idx], L[i]
        
L=[4,2,1,0,5,3,6]
selection_sort(L)
print(L)

#버블정렬(인접한 두 요소를 비교하며 큰 값을 뒤로 보내는 방식)
def bubble_sort(L):
    for i in range(len(L)-1):
        for j in range(0, len(L)-1-i):
            if L[j]>L[j+1]:
                L[j], L[j+1]=L[j+1], L[j]
                
L=[4,2,1,0,5,3,6]
bubble_sort(L)
print(L)

#insert sort(삽입 정렬): 현재 위치 이전을 정렬되어 있다고 가정하고, 그 이후의 원소를 정렬
#O(nsquare)
def insert_sort(L):
    for i in range(1, len(L)):
        curr = L[i]
        j = i-1
        while j>=0 and curr<L[j]:
            L[j+1] = L[j]
            j = j-1
        L[j+1]=curr

L=[4,2,1,0,5,3,6]
insert_sort(L)
print(L)

#합병 정렬(Merge sort): 배열을 두개로 나눠서 한번에 합침-> O(nlogn)
def merge(L,start,mid,end):
    l = (mid-start)+1
    r = (end-mid)
    
    left = [0]*l
    right = [0]*r
    
    for i in range(l):
        left[i] = L[start+i]
    for i in range(r):
        right[i] = L[mid+1+i]
        
    #merge 단계
    i=0
    j=0
    k=start
    while i<l and j<r:
        if left[i]<right[j]:
            L[k]=left[i]
            i=i+1
        else:
            L[k] = right[j]
            j=j+1
        k=k+1
        
    while i<l:
        L[k] = left[i]
        i=i+1
        k=k+1
    while j<r:
        L[k] = right[j]
        j=j+1
        k=k+1
        
def merge_sort(L, start, end):
    if start<end:
        mid = (start+end)>>1
        merge_sort(L,start,mid)
        merge_sort(L,mid+1,end)
        merge(L,start,mid,end)
        
L=[4,2,1,0,5,3,6]
merge_sort(L,0,len(L)-1)
print(L)
        
        
#퀵 정렬(pivot이라는 기준데이터 기준으로 기준보다 큰 데이터와 작은 데이터 위치 변경)
def part_list(L,start,end):
    pivot = L[end]
    i = start-1
    for j in range(start,end):
        if L[j]<pivot:
            i=i+1
            L[i],L[j] = L[j], L[i]
    i=i+1
    L[i], L[end] = L[end], L[i]
    return i   

def quick_sort(L,start,end):
    if end<=start:
        return
    pivot = part_list(L,start, end)
    quick_sort(L,start,pivot-1)
    quick_sort(L, pivot+1,end)
    return

L=[4,2,1,0,5,3,6]
quick_sort(L,0,len(L)-1)
print(L)

import random
import time

def gen_rand_list(n,a):
    L=[]
    for i in range(n):
        L.append(random.randrange(0,a))
    return L

def copy_list(L):
    ret =[0]*len(L)
    for i in range(len(L)):
        ret[i]=L[i]
    return ret

#테스트 함수 길이가 n인 배열 정렬 확인
def test_sort_speed(n):
    time_isort=0
    time_ssort=0
    time_msort=0
    time_qsort=0
    for i in range(1000):
        L1 = gen_rand_list(n,n*2)
        L2 = copy_list(L1)
        L3 = copy_list(L1)
        L4 = copy_list(L1)
        
        #selection sort
        start = time.time()
        selection_sort(L1)
        end = time.time()
        time_ssort = time_ssort+(end-start)
        
        #insert sort
        start =time.time()
        insert_sort(L2)
        end = time.time()
        time_isort = time_isort+(end-start)
        
        #quick sort
        start = time.time()
        quick_sort(L3,0,n-1)
        end = time.time()
        time_qsort = time_qsort+(end-start)
        
        #merge sort
        start = time.time()
        merge_sort(L4,0,n-1)
        end = time.time()
        time_msort = time_msort+(end-start)
        
    print("==sort speed test length:", n)
    print(f"Selection sort: {time_ssort: .5f} sec")
    print(f"Insert sort: {time_ssort: .5f} sec")
    print(f"Quick sort: {time_ssort: .5f} sec")
    print(f"Merge sort: {time_ssort: .5f} sec")
    
test_sort_speed(10)
test_sort_speed(1000)

#week10 (문제풀이)
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

#week 13-1
#알고리즘: 문제를 푸는 절차/ 방법
#자료구조: 효율적으로 데이터를 저장하고 관리하는 방법(1)추상적 자료구조(자료구조의 동작과 규칙만 정의) (2)구체적 자료구조: 데이터를 실제로 저장하고 관리하는 방법
#추상적 자료구조(스택, 큐, 그래프), 구체적 구현 방법(배열, 링크드 리스트 기반, 인접 리스트, 인접 행렬)
#객체: 어떤 속성값과 행동을 가지고 있는 데이터->매서드: 호출될 때 객체에 대해 특정 연산 수행하는 함수, b.append(3) b라는 어펜드에다가~~하라 이런식
#클래스: 객체를 생성하기 위한 템플릿

#배열: Linked list vs list (메모리상에서 연속적으로 저장, 삽입/삭제 원활)
#singly linked list, doubly linked list

#doubly linked list를 (이전 노드 다음 노드의 값을 알아야함) 구현해보자!!

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class dblist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 #append&delete&search
        
    def append(self,data):
        newnode = Node(data)
        if self.head: #head가 있음
            self.tail = newnode
            self.tail.next = newnode
            newnode.prev = self.tail
            self.size +=1     
        else: #head가 없음. 초기화된list
            self.head = newnode
            self.tail = newnode
            self.size +=1
            
            
    def delete(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                self.head = curr.next
                if curr.next:
                    curr.next.prev = None
                else: #self.next.none(self.head=tail)
                    self.tail = None
            elif curr == self.tail:
                self.tail = curr.prev
                curr.prev.next = None
            else: 
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
            self.size-=1
            return
            curr= curr.next
        print("Not found")
                
def selection_sort(self):
    curr = self.head
    while curr:
        min_node = curr
        next_node = curr.next
        while next_node:
            if next_node.data<min_node.data:
                min_node = next_node
            next_node = next_node.next
        
        curr.data, min_node.data = min_node.data, curr.data
        curr = curr.next
    
    def insert_sort(self):
        curr = self.head.next
        while curr:
            min_node = curr
            prev_node =curr.prev
            next_node = curr.next
            
            while prev_node and prev_node.data>min_node.data:
                prev_node = prev_node.prev
                #min_node 먼저 끊고 그 양쪽 사이에 붙여야함!
                
            if min_node.prev: #min_node가 head가 아님
                min_node.prev.next = min_node.next
            if min_node.next: #min_node가 tail이 아님
                min_node.next.prev = min_node.prev
                
            if prev_node is None: #head 에 minnode
                min_node.prev = None
                min_node.next = self.head
                self.head.prev = min_node
                self.head =min_node
                
            else: #head는 아님
                min_node.next = prev_node.next
                min_node.prev = prev_node
                
                if prev_node.next:
                    prev_node.next.prev = min_node
                prev_node.next = min_node
                
            if min_node.next is None:
                    self.tail = min_node
                    
                curr = next_node
                
                
                
    def print_fwd(self):
        curr = self.head
        while curr: #None 아닐때까지. tail 까지
            print(curr.data, end="<->")
            curr = curr.next
        print("None")
    
    def print_back(self):
        curr = self.tail
        while curr:
            print(curr.data, end="->")
            curr = curr.prev
        print("Head")
        
tlist = dblist()
tlist.append(4)
tlist.append(3)
tlist.print_fwd()
tlist.print_back()
tlist.delete(2)
tlist.print_fwd()
print("===selection sort===")
tlist.selection sort()
tlist.insert_sort()
tlist.print_fwd()

#장점: 단순한 구조로 되어있어 추가 삽입 삭제가 쉬움
#단점: 헤드 노드의 정보만 가지고 있어서 특정 노드를 탐색하는데 많은 연산이 걸림.

#week13-2
#Stack=Last-in First-Out: push(데이터 추가),pop(데이터 제거),peek(맨 위 데이터 변환)
#배열 구현 or Linked list

from typing import TypeAlias


class stack_array:
    def __init__(self):
        self.stack = []
        
    def push(self,data):
        self.stack.append(data)
        
    def is_empty(self):
        return len(self.stack)==0 #True: empty, False: Not empty
    
    def pop(self):
        if self.is_empty()==True:
            print("empty stack")
        else:
            return self.stack.pop()
    def peek(self):
        if self.is_empty()==True:
            print("empty stack")
        else:
            return self.stack[-1]
        
class sNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class stack_llist():
    def __init__(self):
        self.top = None
        self.size=0
        
    def push(self,data):
        newnode = sNode(data)
        newnode.next = self.top
        self.top = newnode
        self.size +=1
        
    def pop(self):
        if self.size==0:
            print("stack empty")
        else:
            data=self.top.data
            self.top = self.top.next
            self.size -=1
            return data
    def print_stack(self):
        curr = self.top
        while curr:
            print(curr.data)
            print("ㅣ")
            curr = curr.next
        print("====")

class queue_list:
    def __init__(self):
        self.queue=[]
        
    def enqueue(self,data):
        self.queue.append(data)
        
    def is_empty(self):
        return len(self.queue)==0
    
    def dequeue(self): #연산량이 O(n)
        if self.is_empty():
            print("queue empty")
        else:
            return self.queue.pop(0)
        
 class queue_llist:
     def __init__(self):
         self.head = None
         self.tail = None
         self.size = 0
         
    def enqueue(self,data):
        newnode = sNode(data)
        if self.tail:
            self.tail.next = newnode
            self.tail = newnode
            self.sixe+=1
        else:
            self.tail = newnode
            self.head = newnode
            self.size +=1
            
        
    def dequeue(self):
        if self.size ==0:
            print("empty queue")
        else: 
            data = self.head
            if self.head.next: #self.head!=tail
                self head= self.head.next 
            else:
                self.head = None
                self.tail = None    
            self.size -=1
            return data
        
    def print_queue(self):
        curr = self.head
                
                    
slist = stack_llist()
slist.push(3)
slist.push(5)
slist.push(7)
slist.print_stack()
print(slist.pop())
slist.print_stack()
print(slist.pop())
print(slist.pop())
slist.print_stack()
print(slist.pop())

lq = queue_llist()
lq.enqueue(3)
lq.enqueue(5)
lq.enqueue(7)
lq.print_queue()
print(lq.dequeue())
print(lq.dequeue())
print(lq.dequeue())
print(lq.queue)
print(lq.dequeue())

#stack은 텍스트 에디터의 undo/redo 할때 쓴다

#Queue: First-in First Out
#skims 팝업 생각하기! Enqueue: 맨 뒤 데이터 추가, Dequeue:맨 앞 데이터 제거, Peek:맨 앞 데이터 반환
#배열로 구현 ㄱㄴ Linked list 도 ㄱㄴ

#week14
#트리: 계층적 데이터를 표현하기 위해 사용되는 비선형 자료구조
#노드(node)와 간선(edge)로 구성되어있음
#이진트리: 자식을 2명만 가지고 있을때
#경로: 한 노드에서 다른 노드로 가는 순서, 깊이(루트 노드에서 특정노드까지 경로의 길이, 높이: 루트 노드로 부터 가장 깊은 리프 노드까지의 거리

#트리순회(중위순회는 왼쪽,루트,오른쪽)(전위순회는 루트,왼쪽, 오른쪽),(후위순회는 왼쪽,오른쪽,루트)
#In order traversal(left->root->right)

#N-ary 트리 구현(Left Child Right Sibling)->Node에 대한 class만
from typing import NoDefault


class nNode:
    def __init__(self,data):
        self.data = data
        self.leftchild =None
        self.right_s = None
        
def add_child(parent, child):
    if not parent.leftchild: #자식없음
        parent.leftchild = child
    else: 
        curr = parent.leftchild
        while curr.right_s:
            curr = curr.right_s
        curr.right_s = child
    
def print_display(node,lvl=0):
    if node is None:
        return
    print(" "*lvl+str(node.data))
    print_display(node.leftchild, lvl+1)
    print_display(node.right_s, lvl)

root = nNode("A")
c1 = nNode("B")
c2 = nNode("C")
c3 = nNode("D")
c4 = nNode("F")

add_child(root,c1)
add_child(root,c2)
add_child(root,c4)
print_display(root)

#이진 탐색 트리: 트리 삽입시 데이터를 정렬한 상태로 삽입,leftM<root<right일때
#노드 삽입(root node 삽입, 작으면 왼쪽에다가 배열시키면됨)

class bNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class bstree:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = bNode(data)
        else:
            self._insert(self.root,data)
            
    def _insert(self, node, data): #1<root<r
        if data<node.data:
            if node.left is None:
                node.left = bNode(data)
            else:
                self._insert(node.left,data)
        elif data>node.data: #이러면 중복 되지 않고 출력이 나오게됨(같을 때는 보통 고려 안함)
            if node.right is None:
                node.right = bNode(data)
            else:
                self._insert(node.right,data)
        
    def search(self,data):
        return self._search(self.root,data)
    def _search(self,node,data):
        if node is None:
            return 0
        if node.data ==data:
            return 1
        elif node.data == data:
            return self._search(node.right,data)
        else:
            return self._search(node.left,data)
        
    def remove(self,data):
        if self.search(data):
            self._remove(self.root,data)
        else: 
            print("data does not exist")
            
    def _remove(self,node,data):
        if node is None:
            return None
        
        if data<node.data:
            node.left = self._remove(node.left,data)
            return node
        
        elif data>node.data:
            node.right = self._remove(node.right,data)
            return node
        else: ##node.data==data
            if node.left is None and node.right is None:
                return None
            elif node.right:
                node.data = self._sucessor(node)
                node.right = self._remove(node.right,node.data)
            else:
                node.data = self._predessor(node)
                node.left = self._remove(node.left,node.data)
                return node
            
    def _sucessor(self, node):
        curr = node.right
        while curr.right:
            curr = curr.left
        return curr.data
    
    def _predessor(self,node):
        curr = node.left
        while curr.right:
            curr = curr.right
        return curr.data
    
        
    def display_inorder(self):
        if self.root is None:
            print("empty tree")
        else:
            self._display_inorder(self.root)
            
    def _display_inorder(self, node):
        if node is not None:
            self._display_inorder(node.left)
            print(node.data, end="->")
            self._display_inorder(node.right)      
            
    def inorder_stact(self):
        if self.root is None:
            print("empty tree")
            return
        curr = self.root
        stack = []
        ret = []
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ret.append(curr.data)
            curr = curr.right
                
    def print_tree(self):
        if self.root is None:
            print("empty tree")
        else:
            self._print_tree(self.root,0)
            
    def _print_tree(self,node,lvl):
        if node is not None:
            self._print_tree(node.right, lvl+1)
            print("  "*lvl+str(node.data))
            self._print_tree(node.left,lvl+1)
            
bst = bstree()
bst.insert(4)
bst.insert(6)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)

print("== bst ==")
bst.print_tree()

print("8??:", bst.search(8))
print("5??:", bst.search(5))

bst.display_inorder()
print("")
ret = bst.inorder_stact()
print("ret:", ret)

bst.remove(4) #왼쪽에서 지우고 올리나 오른쪽에서 지우고 올리나 상관없음
bst.print_tree()

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