#week9
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
