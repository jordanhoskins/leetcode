"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def list_node_to_num(list_node, cur_value=None):
    if not cur_value:
        cur_value = []
    cur_value.insert(0, list_node.val)
    if list_node.next is not None:
        list_node_to_num(list_node.next, cur_value=cur_value)
    return int("".join(str(i) for i in cur_value))        

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        solution = list_node_to_num(l1) + list_node_to_num(l2)
        solution_list = [i for i in str(solution)]
        final_node = None
        for i, digit in enumerate(solution_list):
            cur_node = ListNode(val=digit, next=final_node)
            final_node=cur_node
        return final_node
