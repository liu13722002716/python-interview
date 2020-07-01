## 1.定义结点类

    1.定义创造新的结点
    2.定义下一个结点为空
    3.定义重写方法

#### 代码如下:
    class Node: # 结点类
        def __init__(self,data):
            self.data:Any = data
            self.next:Optional = next
        # 重写方法
        def __repr__(self):
            return "Node(%s)" % self.data # 字符串格式化输出
        
## 2.定义 LinkedQueue 队列类
     
    1.定义队列头结点为空
    2.定义队列尾部结点为空
    3.定义队列有效结点个数为0        

#### 代码如下:
    class LinkedQueue:
        def __init__(self) -> None:
            self.front:Optional[Node] = None # 头结点
            self.rear:Optional[Node] = None # 尾部结点
            self.size = 0 # 结点长度

## 3.定义入队方法

    1.创造新的结点
    2.判断队列头部结点是否为空
        当队列头部为空时,直接队列头部与队列尾部都等于新结点
        当队里额头不不为空时,在队列尾部结点后插入新结点,再将尾部结点定义为新插入的结点
    3.队列的结点有效长度加一

#### 代码如下:
    def put(self,item:Any):
        node:Node = Node(item)
        if self.front is None:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1

## 4.定义出队方法

    1.判断队列头部结点是否为空
        当队列头部为空时,此时没有任何结点可以出队,直接返回 "empty queue"
        当队里额头不不为空时,将队列头部的结点指向下一个值,达到出列的效果
    2.队列的结点有效长度减一

#### 代码如下:
    def pop(self):
        if self.front is None:
            raise Exception("empty queue")
        else:
            node:Node = self.front
            self.front  = node.next
            self.size -= 1
            return node.data

## 5.定义查找结点方法

    1.判断索引是否越界
    2.已知查找结点的下标,利用 for 循环找到对应结点的值,并返回该值

#### 代码如下:
    def get(self,index):
        if index < 0 or index >= self.size:
            raise Exception("索引越界")
        else:
            curr = self.front
            for i in range(0,index):
                curr = curr.next
            return curr

## 6.定义 is_empty (判断队列是否为空) 方法

#### 代码如下:
    def is_empty(self) -> bool:
        return self.front is None

## 7.重写方法(输出)

    1.重写方法,将所有结点利用while循环,添加到字符串中输出

#### 代码如下:
    def __repr__(self):
        currend = self.front
        string_repr = ""
        while currend:
            string_repr += f"{currend} <-- "
            currend = currend.next
        return string_repr + "END"
 