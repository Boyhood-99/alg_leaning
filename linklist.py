from copy import deepcopy
from typing import *

class Node():
    def __init__(self,item=0,next=None) -> None:
        self.item=item
        self.next=next


class LinkList():
    def __init__(self,) -> None:
        self.head=None

    def is_empty(self):
        return self.head is None
    
    def items(self):
        cur = self.head
        while cur != None:
            yield cur.item
            cur = cur.next

    def length(self):
        len=0
        cur=self.head

        while cur != None:
            len+=1
            cur=cur.next
        return len
    #头部添加节点
    def add(self,item):
        item = item
        if self.is_empty() :
            self.head = Node(item = item)
        else:
            node = Node(item = item,next=self.head)
            self.head = node

        return self.head

    #尾部添加节点
    def append(self,item):
        node=Node(item=item)
        if self.is_empty():
            self.head = node
        else:
            cur=self.head
            while cur.next != None:
                cur=cur.next
            cur.next = node
        return self.head

    def remove(self,item):
        virtual_head = Node(next = self.head)
        cur = virtual_head
        
        while  cur.next != None:
            pre=cur
            cur=cur.next
            if cur.item == item:
                pre.next=cur.next
        self.head = virtual_head.next
        return self.head
    # def remove(self, item: int) -> Node:
    #     dummy_head = Node(next=self.head) #添加一个虚拟节点
    #     cur = dummy_head
    #     while(cur.next!=None):
    #         if(cur.next.item == item):
    #             cur.next = cur.next.next #删除cur.next节点
    #         else:
    #             cur = cur.next
    #     self.head=dummy_head.next
    #     return self.head

    def get(self,index):
        index=index
        cur=self.head
        for i in range(index):
            cur=cur.next
            if cur == None:
                return -1
                
        return cur.item
    
    def addAtIndex(self,index,item):
        index=index
        item=item
        node=Node(item=item)
        if index <= 0:
            self.add(item)
        elif index >self.length():
            pass
        elif index==self.length():
            self.append(item=item)
        else:
            cur=self.head
            for i in range(index-1):
                cur=cur.next
            node.next=cur.next
            cur.next=node

        return

    def deleteAtIndex(self,index):
        
        if index==0:
            self.head=self.head.next
        else:
            cur=self.head
            pre=cur
            for i in range(index):
                if cur.next == None:
                    return '索引无效'
                else:
                    pre=cur
                    cur=cur.next
            pre.next=cur.next
        
        # return '索引'+str(index)+'位置元素已删除'
        return f'索引{index}位置元素已删除'

    #迭代法
    def reverseList(self):
        pre=None
        cur=self.head
        while cur != None:
            tmp = cur.next
            cur.next = pre

            pre=cur
            cur = tmp
        
        self.head = pre
        return self.head
    #递归法
    def reverseList1(self):
        def reverse(pre,cur):
            if not cur:
                self.head = pre
                return self.head
            
            tmp = cur.next
            cur.next = pre

            return reverse(cur, tmp)
        return reverse(None,self.head)
         

    def swapPair(self):
        vir_head = Node(next=self.head)
        pre = vir_head
        # while pre.next != None and pre.next.next != None:
        while pre.next and pre.next.next:
            cur = pre.next
            tmp = cur.next.next

            pre.next = cur.next
            cur.next.next = cur
            cur.next = tmp

            pre = cur
        self.head = vir_head.next
        return  self.head
    
    def removeNthFroEnd(self,n):
        vir_head = Node(next = self.head)
        fast = vir_head
        slow = vir_head
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        self.head = vir_head.next
        return self.head
        


l=LinkList()

for i in range(5):
    l.append(i)


l.remove(0)
print(l.get(5))

l.removeNthFroEnd(4)

a=list(l.items())
print(a)



