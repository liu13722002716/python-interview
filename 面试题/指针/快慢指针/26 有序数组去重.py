"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例 1:
给定数组 nums = [1,1,2],
函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
你不需要考虑数组中超出新长度后面的元素。
示例 2:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。

说明:
为什么返回数值是整数，但输出的答案是数组呢?
请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
你可以想象内部操作如下:
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);
// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array 数组
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 方案一
from typing import List
class Solution:
    def removeDuplicated(self,nums: List[int]) -> int:
        n = len(set(nums)) # 不重复nums的长度
        i = 0
        while i < n-1:
            if nums[i] == nums[i+1]:
                temp = nums[i+1] # 将重复的第二个值赋值给 temp
                nums[i+1:len(nums)-1] = nums[i+2:] # 将交换位置,取出重复值
                nums[-1] = temp # 将重复的值付给nums最后一项
                continue
            else:
                i += 1
        return i+1

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicated([0,0,1,1,1,2]))

# 方案二
class Solution:
    def removeDuplicated(self,nums: List[int]) -> int:
        slow = 0 # 慢指针
        fast = 1 # 快指针
        while fast < len(nums):
            # fast在slow的前面走
            # 如果两者值不同，则在slow + 1位置保存fast位置的数值
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow+1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicated([0,0,1,1,1,2]))