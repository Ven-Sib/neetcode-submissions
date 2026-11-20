# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = collections.deque([root])
        res = []                      # outside the while loop

        while q:
            node = q.popleft()
            if node:
                res.append(node.val)  # collect every value
                q.append(node.left)
                q.append(node.right)

        heapq.heapify(res)            # O(n)

        for _ in range(k - 1):        # discard the k-1 smallest
            heapq.heappop(res)

        return heapq.heappop(res)     # the kth smallest