## 1.定义结点类

    1.定义创造新的结点
    2.定义下一个结点为空
    3.定义重写方法

#### 代码如下:
    class Node: # 结点类
        def __init__(self,data):
            self.data = data
            self.next = None
        # 重写方法
        def __repr__(self):
            return "Node(%s)" % self.data
        
## 2.定义链表类

    1.定义链表头部为空

#### 代码如下:
    class LinkList:   # 链表类
        def __init__(self):
            self.head = None

## 3.头部插入结点步骤

    1.创造新的结点
    2.判断链表头部是否为空
        如果链表头部为空，新建结点就是根节点
        如果链表头部不为空,在头部插入结点

#### 代码如下:
    def insert_head(self,data):
        # 创造新的结点
        new_node = Node(data)
        # 如果链表不为空 在头部插入结点
        if self.head is not None:
            new_node.next = self.head
        # 如果链表为空，或者已经构造了新链表
        self.head = new_node

## 4.尾部插入结点步骤

    1.判断链表头部是否为空
        如果链表头部为空,那么直接插入结点
        如果链表头部不为空,通过while循环找到当前结点的尾部后,在尾部后面插入结点

#### 代码如下:
    def append(self,data):
        # 如果当前头部为空那么直接插入结点
        if self.head is None:
            self.insert_head(data)
        else:
            # 当temp不是尾部时，那就前进一步
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(data)

## 5.中间插入节点步骤

    1.判断链表头部是否为空
        如果当前链表头部为空或者插入位置为首位时,直接在头部插入结点
        如果当前链表头部不为空
            创建新结点
            找到链表头部
            前一个结点等于当前结点
            找到当前插入位置后,将当前结点的后一个结点链接为新的结点,新的结点的后一个结点链接为,当前结点的下一个结点,完成在中间插入结点
            
#### 代码如下:
    def insert(self,i,data):
        if self.head is None or i == 1:
            self.insert_head(data)
        else:
            new_node = Node(data) # 创建新结点
            curr = self.head  # 找到链表头部
            pre = self.head # 前一个结点等于当前结点
            # 套路
            j = 1
            while j < i:
                pre = curr
                curr = curr.next
                j += 1
            pre.next = new_node
            new_node.next = curr

## 6.直接构建多元表链表步骤
    
    1.根据 from typing import List 自带模块,添加一个列表
    2.当前链表头部定义为列表的第一项数值
    3.通过 for 循环遍历列表从第二个值开始,将列表的所有值链接到链表中

#### 代码如下:
    def linklist(self,obj:List):
        new_node = Node(obj[0])
        self.head = new_node
        curr = self.head
        for i in obj[1:]:
            curr.next = Node(i)
            curr = curr.next

## 7.删除头部结点:

    1.判断链表头部是否为空
        如果当前链表头部为空,那么就不用删除,直接输出为 "空链表"
        如果当前链表头部不为空,那么,我们删除第一个结点

#### 代码如下: 
    def delete_head(self):
        if self.head is None:
            print("空链表")
        else:
            self.head = self.head.next
     
## 8.删除尾部结点

    1.判断链表头部是否为空
        如果当前链表头部为空,那么就不用删除,直接输出为 "空链表"
        如果当前链表头部不为空,那么通过while循环,找到链表的最后一项,删除即可
       
#### 代码如下:   
    def delete_pop(self):
        curr = self.head
        if self.head is None:
            print("空链表")
        else:
            while curr.next.next is not None:
                curr = curr.next
            temp = curr.next
            curr.next = None
            print("删除的尾部结点为:%s"%temp)

## 9.打印辅助方法

    1.利用while循环,打印链表中的每一项
    2.重写方法,将所有结点利用while循环,添加到字符串中输出

#### 代码如下:
    def print_list(self):
        # 遍历列表的小技巧
        temp = self.head
        # 当temp部位空时
        while temp is not None:
            # 打印temp.data:temp的头部
            print(temp.data)
            # 再将temp指向下一个temp
            temp = temp.next  
    
    def __repr__(self):
        temp = self.head
        string_repr = ""
        while temp is not None:
            string_repr += '%s -->'%(temp)
            temp = temp.next
        return string_repr + "END"