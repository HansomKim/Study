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

