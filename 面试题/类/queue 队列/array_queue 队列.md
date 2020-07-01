## 1.定义 Queue (队列) 类

    1.定义一条空的记录,用来记录队列的结点
    2.定义队列的有效数值个数开始为0
    3.定义队列的头部为0 

#### 代码如下:
    class Queue:
        def __init__(self):
            self.entries = [] # 一条记录
            self.length = 0 # 计数
            self.front = 0

## 2.重写方法

#### 代码如下:
    def __str__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

## 3.入队方法

    1.利用 append 方法,直接向记录列表中插入数值
    2.队列的有效数值个数加一

#### 代码如下:
    def put(self,item): # 入队 enqueue
        self.entries.append(item)
        self.length += 1

## 4.出队方法

    1.判断队列头部是否为0
        当队列头部为0时,没有任何数值可以出列,直接返回 "队列无数值!"
        当队列头部不为0时,删除队列第一个入队的值,将记录列表第一个值出队,剩下从第二个值到最后一个值
    2.队列有效数值个数减一

#### 代码如下:
    def get(self): # 出队 dequeue
        if self.length == 0:
            raise Exception("队列无数值!")
        else:
            dequeued = self.entries[self.front]
            self.length -= 1
            self.entries = self.entries[1:]
            return dequeued

## 5.定义队列第一个结点方法

#### 代码如下:
    def front1(self):
        return self.entries[0]

## 6.定义 size (输出队列长度) 方法

#### 代码如下:
    def size(self):
        return self.length
