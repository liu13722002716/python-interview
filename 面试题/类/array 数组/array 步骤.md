## 1.定义数组类

    1.定义数组的长度
    2.定义数组的有效数值个数

#### 代码如下:
    class Array: # 构造数组类
        def __init__(self,capacity):
            self.array = [None] * capacity  # 数组长度
            self.size = 0   # 数组有效元素个数

## 2.增加数组有效数据的步骤

    1.判断下标是否越界
    2.判断数组长度是否需要扩容
    3.在任意下标处插入数据,当在下标为2处插入数据时,那么下标为2之后的数据就要都全部向后移动一位,实现增加数据的效果

#### 代码如下:
    def  insert(self,index,element): # 插入元素的方法
        if index < 0 or index > self.size: # 判断下标是否越界
            print("数组越界")
        if self.size >= len(self.array): # 判断数组有效个数是否大于数组长度,如果大于数组长度那么就要给数组扩容
            self.addcapacity()
        for i in range(self.size - 1,index - 1,-1): # 将从插入下标开始向后的所有数值,向后移动一位
            self.array[i + 1] = self.array[i]
        self.array[index] = element # 将插入的数值赋值给当前要插入的位置
        self.size += 1 # 记录数组有效个数
    
## 3.数组扩容方法步骤

    1.定义新的数组长度为原来数组长度的二倍
    2.将原来数组的值,赋值给新的数组
    3.将新的数组变为原来的数组

#### 代码如下:
    def remove(self,index): # 删除元素方法
        if index < 0 or index > self.size: # 判断下标是否越界
            print("数组越界")
        for i in range(index,self.size): # 将删除的位置之后的数,向前移动一位
            self.array[i] = self.array[i + 1]
        self.size -= 1
    
## 4.定义输出方法

#### 代码如下:
    def output(self): # 输出方法
        for i in range(self.size):
            print(self.array[i],end=" -> ")