"""
:Author: Mr.Liu
:Create: 2020/6/28 18:02
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""

"""
给你两个二进制字符串，返回它们的和（用二进制表示）。
输入为 非空 字符串且只包含数字 1 和 0。
示例 1:
    输入: a = "11", b = "1"
    输出: "100"
示例 2:
    输入: a = "1010", b = "1011"
    输出: "10101"
提示：
    每个字符串仅由字符 '0' 或 '1' 组成。
    1 <= a.length, b.length <= 10^4
    字符串如果不是 "0" ，就都不含前导零。
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = 0
        num2 = 0
        sum = 0
        if b == '0':
            return a
        if a == '0':
            return b
        for i in range(len(a)):
            if a[i] == '1':
                num1 += pow(2, len(a) - (i + 1))
        for i in range(len(b)):
            if b[i] == '1':
                num2 += pow(2, len(b) - (i + 1))
        sum = num1 + num2
        y = ''
        while sum > 0:
            sum, z = divmod(sum, 2)
            y = str(z) + y
        return y

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('1111','1111'))