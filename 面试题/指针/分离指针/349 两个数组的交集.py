"""
:Author: Mr.Liu
:Create: 2020/6/25 10:00
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""给定两个数组，编写一个函数来计算它们的交集。
示例 1：
    输入：nums1 = [1,2,2,1], nums2 = [2,2]
    输出：[2]
示例 2：
    输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    输出：[9,4]
说明：
    输出结果中的每个元素一定是唯一的。
    我们可以不考虑输出结果的顺序。
"""

# 方法2
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list = []
        for i in range(len(nums1)): # 遍历第一个列表
            for j in range(len(nums2)): # 遍历第二个列表
                if nums1[i] == nums2[j] and nums1[i] not in list:  # 相等时就是交集 , 去重
                    list.append(nums1[i])
        return list

if __name__ == '__main__':
    s = Solution()
    print(s.intersection([4,9,5],[9,4,9,8,4]))

# 方法2
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    s = Solution()
    print(s.intersection([4,9,5],[9,4,9,8,4]))

# 方法3
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()  # 排序
        nums2.sort()  # 排序
        n1 = 0   # nums1 指针
        n2 = 0    # nums2 指针
        list = [] # 返回值的新列表
        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] > nums2[n2]:
                n2 += 1
            elif nums1[n1] < nums2[n2]:
                n1 += 1
            else:
                if nums1[n1] not in list:
                    list.append(nums1[n1])
                n1 += 1
                n2 += 1
        return list

if __name__ == '__main__':
    s = Solution()
    print(s.intersection([4,9,5],[9,4,9,8,4]))