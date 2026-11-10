"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict1 = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            dict1[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = dict1[curr]
            copy.next = dict1[curr.next]
            copy.random = dict1[curr.random]
            curr = curr.next
        
        return dict1[head]