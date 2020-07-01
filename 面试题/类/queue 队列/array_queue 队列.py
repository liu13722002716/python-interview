"""
:Author: Mr.Liu
:Create: 2020/6/24 14:34
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
class Queue:
    def __init__(self):
        self.entries = [] # 一条记录
        self.length = 0 # 计数
        self.front = 0

    def __str__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    def put(self,item): # 入队 enqueue
        self.entries.append(item)
        self.length += 1

    def get(self): # 出队 dequeue
        if self.length == 0:
            raise Exception("队列无数值!")
        else:
            dequeued = self.entries[self.front]
            self.length -= 1
            self.entries = self.entries[1:]
            return dequeued

    def front1(self):
        return self.entries[0]

    def size(self):
        return self.length

queue = Queue()
queue.put(10)
queue.put(9)
queue.put(8)
print(queue)
print(queue.get())
print(queue)














