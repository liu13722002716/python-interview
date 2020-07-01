## 1.定义satck类

    1.定义一个空的栈
    2.定义栈的有效数值个数为0

#### 代码如下:
    class Stack:
        def __init__(self,limit = 10):
            self.stack = [] # 空的栈
            self.size = 0
        
## 2.定义 bool 方法

#### 代码如下:
    def __bool__(self):
        return bool(self.stack)
        
## 3.定义 srt 字符串方法  
 
#### 代码如下:
    def __str__(self): # 转换为字符串格式
        return str(self.stack)

## 4.压栈方法步骤

    1.向新的栈中利用 append 方法直接添加
    2.压栈将栈的有效数值个数加一,就是栈的后面添加数值

#### 代码如下:
    def push(self,data): # 压栈
        stack = self.stack.append(data)
        self.size += 1
        return stack

## 5.弹栈方法步骤

    1.判断当前栈是否为空:
        当栈为空时,没有任何数值可以弹出,那么直接返回 "pop from an empty stack"
        当栈不为空时,利用 pop 方法,将栈中的最后一个插入进去的数值删除,就是弹栈,弹出最后一个插入栈的值
    2.弹栈将栈的有效数值个数减一,就是删除最后一个数值

#### 代码如下:
    def pop(self): # 弹栈
        if self.stack:
            stack = self.stack.pop()
            self.size -= 1
            return stack
        else:
            raise Exception("pop from an empty stack")

## 6.定义 peek (输出最新压栈的呢个值) 方法

#### 代码如下:
    def peek(self):
        if self.stack:
            return self.stack[-1]

## 7.定义栈是否为空,用 bool 方法

#### 代码如下:
    def is_empty(self): # 判断列表是否为空
        return not bool(self.stack)

## 8.定义 count (输出栈的长度) 方法

#### 代码如下:
    def count(self):
        return self.size
    