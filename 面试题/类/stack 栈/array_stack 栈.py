"""
:Author: Mr.Liu
:Create: 2020/6/23 16:31
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
class Stack:
    def __init__(self,limit = 10):
        self.stack = [] # 空的栈
        self.size = 0

    def __bool__(self):
        return bool(self.stack)

    def __str__(self): # 转换为字符串格式
        return str(self.stack)

    def push(self,data): # 压栈
        stack = self.stack.append(data)
        self.size += 1
        return stack

    def pop(self): # 弹栈
        if self.stack:
            stack = self.stack.pop()
            self.size -= 1
            return stack
        else:
            raise Exception("pop from an empty stack")

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self): # 判断列表是否为空
        return not bool(self.stack)

    def count(self):
        return self.size

if __name__ == '__main__':
    stack = Stack()
    for i in range(10):
        stack.push(i)
    print(stack)
    for i in range(5):
        stack.pop()
    print(stack)
    print(stack.peek())
    print(stack.count())
    print(stack.is_empty())