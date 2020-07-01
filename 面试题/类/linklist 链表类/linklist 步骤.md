## 1.定义结点类

    1.定义创造新的结点
    2.定义下一个结点为空
    3.定义重写方法

#### 代码如下:
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
        # 重写方法
        def __repr__(self):
            return "Node(%s)"%(self.data)

## 2.定义链表类

    1.定义链表头部为空
    2.定义链表尾部为空
    3.定义链表的有效结点个数为0

#### 代码如下:
    class LinkList:
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0
        
## 3.查找结点方法步骤

    1.要想遍历链表,首先要找到链表的头部
    2.已知次数,适合用for循环找到查找的结点

#### 代码如下:
    def get(self,index):
        # 要想遍历链表,首先要找到链表的头部
        curr = self.head
        # 已知次数,适合用for循环
        for i in range(1,index):
            curr = curr.next
        return curr
    
## 4.增加结点的步骤

    1.创造新的结点
    2.判断索引是否越界
    3.判断头部结点是否为空
        如果为空,新建结点就是链表头部和尾部
        如果不为空
            当插入结点位置为头部时,直接在头部插入结点,之后将新插入的结点定义为链表头部
            当插入结点位置为尾部时,直接在列表尾部插入结点,之后将新插入的结点定义为链表尾部
            当在中间任意位置插入新结点时,利用查找方法找到插入位置,将新插入结点的下一结点定义链接为当前结点的下一结点,
            之后再将当前的下一节点链接为新插入结点,完成在中间任意位置插入结点
    4.插入结点后链表有效结点个数加一
    
#### 代码如下:
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

## 5.删除结点的步骤

    1.判断索引是否越界
    2.判断需要删除结点位置:
        当删除结点为首部结点时,直接删除头部结点,将头部结点定义为,之前头部结点的下一节点
        当删除结点为尾部结点时,利用查找方法,找到尾部的前一节点,将前一结点的下一结点(也就是尾部结点)定义为空,即删除
    3.删除结点后将链表有效结点个数减一

#### 代码如下:
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

## 6.反转当前链表输出方法步骤

    1.定义当前结点为空,当前下一结点为链表头部
    2.利用while循环,将链表头部指向当前结点,之后当前结点向后移动一位,链表头部结点也向后移动一位,再次循环,达到反转链表效果
     
#### 代码如下:
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

## 7.打印辅助方法

    1.利用while循环,打印链表中的每一项
    2.重写方法,将所有结点利用while循环,添加到字符串中输出

#### 代码如下:
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


