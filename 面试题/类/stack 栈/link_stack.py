"""
:Author: Mr.Liu
:Create: 2020/6/23 16:31
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
from typing import Any,Optional,NoReturn
class Node:
    def __init__(self,data:Any,next:Optional = None):
        self.data:Any = data
        self.next:Optional[Node] = next

    def __repr__(self):
        return f"Node({self.data})"

class LinkedStack:
    def __init__(self) -> NoReturn:
        self.top:Optional[Node] = None
        self.size = 0

    def push(self,item:Any): # 压栈
        node:Node = Node(item)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self): # 弹栈
        if self.top is None:
            raise Exception("pop from empty stack")
        else:
            node = self.top
            self.top = node.next
            self.size -= 1
            return node.data

    def is_empty(self): # 判断是否为空
        return self.top is None

    def count(self):
        return self.size

    def __repr__(self):
        current = self.top
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        return string_repr + "END"

if __name__ == '__main__':
    stack = LinkedStack()
    stack.push(10)
    stack.push(9)
    stack.push(8)
    print(stack)
    print(stack.pop())
    print(stack.count())
    print(stack)
    print(stack.is_empty())