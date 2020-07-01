"""
:Author: Mr.Liu
:Create: 2020/6/26 14:41
:Github: https://XXXXXXXX
Copyright (c) 2020,Mr.Liu Group All Rights Reserved.
"""
"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:
     输入：[1, 2, 3, 3, 2, 1]
     输出：[1, 2, 3]
示例2:
     输入：[1, 1, 1, 1, 2]
     输出：[1, 2]
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        s1 = ListNode(0)
        s1.next = head
        list = []
        prev = s1
        curr = head
        while curr:
            if curr.val not in list:
                list.append(curr.val)
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        return head
