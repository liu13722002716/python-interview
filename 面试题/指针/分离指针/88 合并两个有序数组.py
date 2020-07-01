"""
:Author: Mr.Liu
:Create: 2020/6/25 10:17
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
说明:
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
"""

# 方法1
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m1 = 0  # nums1 指针
        n1 = 0  # nums2 指针
        if m == 0:  # 当 m = 0 时证明nums1中没有要输出的值,那么将nums2中的值都赋值给nums1
            nums1[:] = nums2[:]
        while n1 < n:
            if m1 >= m+n1:
                nums1[m1:m1+n-n1] = nums2[n1:n]
                break
            if nums1[m1] < nums2[n1]:
                m1 += 1
            else:
                nums1[m1],nums1[m1+1:] = nums2[n1],nums1[m1:len(nums1)-1]
                m1 += 1
                n1 += 1
        return nums1
if __name__ == '__main__':
    s = Solution()
    print(s.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5))

# 方法2
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1  # nums1 指针
        j = n - 1  # nums2 指针
        k = m + n - 1  # nums1 最后位置指针
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while i >= 0:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        return nums1

if __name__ == '__main__':
    s = Solution()
    print(s.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5))
