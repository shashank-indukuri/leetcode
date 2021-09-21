# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = {}
        curnode = head
        i = 0
		
        while curnode != None:
            nodes[i] = curnode
            curnode = curnode.next
            i += 1
        index = i - n
        next_node = nodes[index].next
        
        try:
            prev_node = nodes[index-1]
            nodes.pop(index)
            prev_node.next = next_node
        except:
            head = next_node
			
        return head
