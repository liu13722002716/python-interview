from typing import List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    # 重写方法
    def __repr__(self):
        return "Node(%s)"%(self.data)

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index):
        # 要想遍历链表,首先要找到链表的头部
        curr = self.head
        # 已知次数,适合用for循环
        for i in range(1,index):
            curr = curr.next
        return curr

    def insert(self,index,data):
        new_node = Node(data) # 创造新的结点
        if index < 0 or index > self.size:  # 索引越界
            raise Exception("索引越界")
        elif self.size == 0: # 空链表
            self.head = new_node
            self.tail = new_node
        elif index == 0: # 头部插入结点
            new_node.next = self.head
            self.head = new_node
        elif index == self.size: # 尾部插入结点
            self.tail.next = new_node
            self.tail = new_node
        else: # 中间插入结点
            prev = self.get(index - 1)
            new_node.next = prev.next # 需要注意,把要插入的结点的后继结点做好
            prev.next = new_node # 在处理前驱结点
        self.size += 1

    def remove(self,index):
        if index < 0 or index >= self.size:
            raise Exception("索引越界")
        elif index == 0:
            remove_node = self.head
            self.head = self.head.next
        elif index == self.size:
            prev = self.get(index - 1)
            remove_node = prev.next
            prev.next = None
        else:
            prev = self.get(index)
            remove_node = prev.next
            prev.next = prev.next.next
        self.size -= 1
        return "删除的结点为:%s"%(remove_node)

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            if prev is None:
                curr.next = prev
            else:
                curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def print_list(self):
        curr = self.head
        while curr:
            print(curr)
            curr = curr.next

    def __repr__(self):
        curr = self.head
        string_repr = ""
        while curr:
            string_repr += "%s -->"%(curr)
            curr = curr.next
        return string_repr + "END"


if __name__ == '__main__':
    # node = Node(10)
    # print(node)
    ll = LinkList()
    ll.insert(0,1)
    ll.insert(1,2)
    ll.insert(2,3)
    ll.insert(3,4)
    print(ll.get(5))
    print(ll)
    ll.remove(3)
    print(ll)
    ll.reverse()
    print(ll)