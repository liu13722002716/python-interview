"""
:Author: Mr.Liu
:Create: 2020/6/19 14:03
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
from typing import List
class Node: # 结点类
    def __init__(self,data):
        self.data = data
        self.next = None
    # 重写方法
    def __repr__(self):
        return "Node(%s)" % self.data

class LinkList:   # 链表类
    def __init__(self):
        self.head = None

    # 头部插入结点
    def insert_head(self,data):
        # 创造新的结点
        new_node = Node(data)
        # 如果链表不为空 在头部插入结点
        if self.head is not None:
            new_node.next = self.head
        # 如果链表为空，或者已经构造了新链表
        self.head = new_node

    # 尾部插入结点
    def append(self,data):
        # 如果当前头部为空那么直接插入结点
        if self.head is None:
            self.insert_head(data)
        else:
            # 当temp不是尾部时，那就前进一步
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

    # 中间插入结点
    def insert(self,i,data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            new_node = Node(data) # 创建新结点
            curr = self.head  # 找到链表头部
            pre = self.head # 前一个结点等于当前结点
            # 套路
            j = 1
            while j < i:
                pre = curr
                curr = curr.next
                j += 1
            pre.next = new_node
            new_node.next = curr

    # 直接构建多元表链表
    def linklist(self,obj:List):
        new_node = Node(obj[0])
        self.head = new_node
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next

    # 删除头部结点
    def delete_head(self):
        if self.head is None:
            print("空链表")
        else:
            self.head = self.head.next

    # 删除尾部结点
    def delete_pop(self):
        curr = self.head
        if self.head is None:
            print("空链表")
        else:
            while curr.next.next is not None:
                curr = curr.next
            temp = curr.next
            curr.next = None
            print("删除的尾部结点为:%s"%temp)

    # 删除方法2
    def delete_tail(self):
        pre = self.head
        curr = self.head
        if self.head is None:
            print("空链表")
        else:
            while curr.next is not None:
                pre = curr
                curr = curr.next
            pre.next = None

    # 辅助函数
    def print_list(self):
        # 遍历列表的小技巧
        temp = self.head
        # 当temp部位空时
        while temp is not None:
            # 打印temp.data:temp的头部
            print(temp.data)
            # 再将temp指向下一个temp
            temp = temp.next

    def __repr__(self):
        temp = self.head
        string_repr = ""
        while temp is not None:
            string_repr += '%s -->'%(temp)
            temp = temp.next
        return string_repr + "END"

if __name__ == '__main__':
    ll = LinkList()
    ll.linklist([1, 2, 3, 4, 5,6])
    ll.delete_tail()
    ll.delete_pop()
    ll.delete_head()
    ll.print_list()
    print(ll)



