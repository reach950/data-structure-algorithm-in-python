#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""链表算法题"""

from queue import PriorityQueue


# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 206. Reverse Linked List 反转链表
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        prev = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

    # 反转链表递归实现
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return p

    # 24. Swap Nodes in Pairs 两两交换链表中的节点
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = start = ListNode(0)
        prev.next = head
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            a.next, b.next, prev.next = b.next, a, b
            prev = b.next
        return start.next

    # 141. Linked List Cycle 判断链表是否有环(用set实现，空间复杂度O(n))
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        hash_set = set()
        while curr:
            if curr in hash_set:
                return True
            hash_set.add(curr)
            curr = curr.next
        return False

    # 141. Linked List Cycle 判断链表是否有环(用快慢指针实现，空间复杂度O(1))
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    # 25. Reverse Nodes in k-Group k个一组翻转链表
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head or head.next or k < 2:
            return head
        start = prev_sub_tail = ListNode(0)
        start.next = head
        sub_head = sub_tail = head
        while sub_head:
            for _ in range(k - 1):
                if sub_tail is None:
                    return start.next
                sub_tail = sub_tail.next
            next_sub_head = sub_tail.next
            # 将子链表的tail的next指针设为null,反转链表
            sub_tail.next = None
            Solution().reverseList(sub_head)
            # 把子链表接起来,此时的subHead为反转后的tail,subTail为反转后的head
            prev_sub_tail.next = sub_tail
            sub_head.next = next_sub_head
            # 将prevSubTail更新子链表的tail,subHead,subTail更新到下一个子链表的head
            prev_sub_tail, sub_head, sub_tail = sub_head, next_sub_head, next_sub_head
        return start.next

    # 142. Linked List Cycle II 环形链表的起始位置
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        if fast is None or fast.next is None:
            return None
        slow = head
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return slow

    # 21. Merge Two Sorted Lists 两个有序的链表合并(递归实现)
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists1(l1, l2.next)
            return l2

    # 21. Merge Two Sorted Lists 两个有序的链表合并(循环实现)
    def mergeTwoLists2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start = curr = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        curr.next = l1 or l2
        return start.next

    # 19. Remove Nth Node From End of List 删除链表倒数第 n 个结点(空间复杂度O(n))
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        curr, temp_list = head, [head]
        while curr.next:
            curr = curr.next
            temp_list.append(curr)
        length = len(temp_list)
        if n == length:
            temp_list.pop(0)
        elif n == 1:
            temp_list[length - 1 - n].next = None
        else:
            temp_list[length - 1 - n].next = temp_list[length + 1 - n]
        if temp_list:
            return temp_list[0]
        else:
            return None

    # 19. Remove Nth Node From End of List 删除链表倒数第 n 个结点(快慢指针实现 空间复杂度O(1))
    def removeNthFromEnd2(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return None
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head

    # 876. Middle of the Linked List 求链表的中间结点
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 23. Merge k Sorted Lists合并K个排序链表
    def mergeKLists(self, lists):
        if not lists:
            return None
        queue = PriorityQueue()
        start = curr = ListNode(0)
        for l in lists:
            queue.put((l.val, l))
        while queue:
            curr.next = queue.get()[1]
            curr = curr.next
            node = curr.next
            if node:
                queue.put(node.val, node)
        return start.next
