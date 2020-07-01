from typing import Any,Optional,List
class Node:
    def __init__(self,data:Any,next:Optional = None):
        self.data:Any = data
        self.next:Optional = next

    def __repr__(self):
        return f"Node({self.data})" # 字符串格式化输出

class LinkedQueue:
    def __init__(self) -> None:
        self.front:Optional[Node] = None # 头结点
        self.rear:Optional[Node] = None # 尾部结点
        self.size = 0 # 结点长度

    def put(self,item:Any):
        node:Node = Node(item)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

    def pop(self):
        if self.front is None:
            raise Exception("empty queue")
        else:
            node:Node = self.front
            self.front  = node.next
            self.size -= 1
            return node.data

    def get(self,index):
        if index < 0 or index >= self.size:
            raise Exception("索引越界")
        else:
            curr = self.front
            for i in range(0,index):
                curr = curr.next
            return curr

    def is_empty(self) -> bool:
        return self.front is None

    def __repr__(self):
        currend = self.front
        string_repr = ""
        while currend:
            string_repr += f"{currend} <-- "
            currend = currend.next
        return string_repr + "END"

if __name__ == '__main__':
    queue = LinkedQueue()
    for i in range(5):
        queue.put(i)
    print(queue)
    print(queue.pop())
    print(queue)
    print(queue.get(3))
    print(queue.is_empty())
    print(queue.size)

