"""
:Author: Mr.Liu
:Create: 2020/6/19 10:17
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
class Array: # 构造数组类
    def __init__(self,capacity):
        self.array = [None] * capacity  # 数组长度
        self.size = 0   # 数组有效元素个数

    def  insert(self,index,element): # 插入元素的方法
        if index < 0 or index > self.size: # 判断下标是否越界
            print("数组越界")
        if self.size >= len(self.array): # 判断数组有效个数是否大于数组长度,如果大于数组长度那么就要给数组扩容
            self.addcapacity()
        for i in range(self.size - 1,index - 1,-1): # 将从插入下标开始向后的所有数值,向后移动一位
            self.array[i + 1] = self.array[i]
        self.array[index] = element # 将插入的数值赋值给当前要插入的位置
        self.size += 1 # 记录数组有效个数

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2 # 定义新的数组长度为原来数组长度的二倍
        for i in range(self.size): # 将原来数组的值,赋值给新的数组
            new_array[i] = self.array[i]
        self.array = new_array # 将新的数组变为原来的数组

    def remove(self,index): # 删除元素方法
        if index < 0 or index > self.size: # 判断下标是否越界
            print("数组越界")
        for i in range(index,self.size): # 将删除的位置之后的数,向前移动一位
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def output(self): # 输出方法
        for i in range(self.size):
            print(self.array[i],end=" -> ")

if __name__ == '__main__':
    a = Array(3)
    a.insert(0,10)
    a.insert(1,20)
    a.insert(2,30)
    a.insert(3,40)
    a.remove(1)
    a.output()