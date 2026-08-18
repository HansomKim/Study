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
