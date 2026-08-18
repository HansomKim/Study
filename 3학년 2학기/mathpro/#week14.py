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