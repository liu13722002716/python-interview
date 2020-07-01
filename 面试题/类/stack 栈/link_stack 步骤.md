## 1.定义结点类

    1.定义创造新的结点
    2.定义下一个结点为空
    3.定义重写方法

#### 代码如下:
    class Node:
        def __init__(self,data:Any,next:Optional = None):
            self.data:Any = data
            self.next:Optional[Node] = next
        # 重写方法
        def __repr__(self):
            return f"Node({self.data})"
        
## 2.定义栈类   

    1.定义栈的头部为空
    2.定义栈的有效结点为0     
        
#### 代码如下:
    class LinkedStack:
        def __init__(self) -> NoReturn:
            self.top:Optional[Node] = None
            self.size = 0

## 3.定义压栈方法步骤

    1.创造新的结点
    2.判断栈的头部是否为空
        当栈的头部为空时,新建结点就是栈的头部
        当栈的头部不为空时,将新建的结点插入头部结点的前面,再将头部结点定义为新的结点
    3.将栈的有效结点个数加一

#### 代码如下:
    def push(self,item:Any): # 压栈
        node:Node = Node(item)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

## 4.定义弹栈方法步骤

    1.判断栈的头部是否为空:
        当栈的头部为空时,没有结点可以弹出,直接返回 "pop from empty stack"
        当栈的头部不为空时,将站的头部结点定义为头部结点的下一个结点,实现弹栈的效果
    2.将栈的有效结点个数减一

#### 代码如下:
    def pop(self): # 弹栈
        if self.top is None:
            raise Exception("pop from empty stack")
        else:
            node = self.top
            self.top = node.next
            self.size -= 1
            return node.data

## 5.定义 is_empty (判断是否为空)方法

#### 代码如下:
    def is_empty(self): # 判断是否为空
        return self.top is None

## 6.定义 count (栈的长度) 方法 

#### 代码如下:
    def count(self):
        return self.size

## 7.重写方法(输出)

    1.重写方法,将所有结点利用while循环,添加到字符串中输出

#### 代码如下:
    def __repr__(self):
        current = self.top
        string_repr = ""
        while current:
            string_repr += f"{current} --> "
            current = current.next
        return string_repr + "END"

        