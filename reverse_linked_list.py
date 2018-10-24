#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""反转链表"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_node = head
        prev_node = None
        while curr_node:
            curr_node.next, prev_node, curr_node = prev_node, curr_node, curr_node.next
        return prev_node
