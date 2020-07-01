"""
:Author: Mr.Liu
:Create: 2020/6/25 22:35
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""

"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

提示：
3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # 排序
        min = abs(nums[0] + nums[1] + nums[2] - target) # 相差的值
        res = nums[0] + nums[1] + nums[2]  # 三数之和
        for i in range(len(nums) - 2):
            left = i + 1 # 首指针
            right = len(nums) - 1 # 尾指针
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                # 因为比较的是距离而 sum 可能是负值，所以这里需要取绝对值来比较并更新当前数的距离
                # 如果3个数的和比 target 大，因为数组排序，所以尾指针向前移动可减小3个数的和
                # 反之则向后移动首指针
                if abs(sum - target) < min:
                    min = abs(sum - target)
                    res = sum
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else: #  如果3个数的和等于target，即为3个数的和
                    return sum
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4],1))