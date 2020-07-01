"""
:Author: Mr.Liu
:Create: 2020/6/27 10:18
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
示例 1:
    输入: 123
    输出: 321
示例 2:
    输入: -123
    输出: -321
示例 3:
    输入: 120
    输出: 21
注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
"""


class Solution:
    def reverse(self, x: int) -> int:
        if '-' in str(x):
            y = str(x).replace('-','')
            y = int('-'+ y[::-1])
            if (-2)**31 < y < 2 **31 -1:
                y = y
            else:
                y = 0
        else:
            y = int(str(x)[::-1])
            if (-2)**31 < y < 2 **31 -1:
                y = y
            else:
                y = 0
        return y
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(120))
