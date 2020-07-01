"""
:Author: Mr.Liu
:Create: 2020/6/23 19:46
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
说明:
返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:
    输入: numbers = [2, 7, 11, 15], target = 9
    输出: [1,2]
    解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
"""

# 方法1
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 # 首指针
        right = len(numbers) - 1 # 尾指针
        while left < right:
            curr = numbers[left] + numbers[right] # 两数之和
            if curr == target:
                return[left+1,right+1]
            else:
                if curr < target:
                    left += 1
                else:
                    right -= 1
                    
if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))

# 方法2
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)): # 外循环
            for j in range(i+1,len(numbers)): # 内循环
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15],9))

# 方法3
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums_dict = {} # 空的字典
        for i in range(len(numbers)):
            temp = target - numbers[i]  # 计算差值
            if temp in nums_dict:  # 当差值存在字典中输出对应下标
                return [nums_dict[temp] + 1, i + 1]
            else: # 当差值不存在字典中,将数值作为 key ,下标作为 value 加入字典中,方便查找;
                nums_dict[numbers[i]] = i

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([3,2,4],6))