"""
:Author: Mr.Liu
:Create: 2020/6/27 16:46
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
示例 1:
    输入: 121
    输出: true
示例 2:
    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:
    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        list = []
        for i in y:
            list.append(i)
        left = 0
        right = len(y) - 1
        while left < right:
            if list[left] == list[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(10))




"""
进阶:
    你能不将整数转为字符串来解决这个问题吗？
"""