"""
:Author: Mr.Liu
:Create: 2020/6/29 9:39
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。
注意：
    0 ≤ x, y < 231.
示例:
    输入: x = 1, y = 4
    输出: 2
解释:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑
    
    上面的箭头指出了对应二进制位不同的位置。

"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        count = 0
        while a != 0: # 汉明重量
            a = a & (a - 1)
            count += 1
        return count
if __name__ == '__main__':
    s = Solution()
    print(s.hammingDistance(1,4))