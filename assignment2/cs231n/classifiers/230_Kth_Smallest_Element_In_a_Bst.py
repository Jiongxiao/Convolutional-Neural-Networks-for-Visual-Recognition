# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        from collections import deque
        stack=deque()
        p=root
        while(True):
            while(p):
                stack.append(p)
                p=p.left
            if not stack:
                break
            p=stack.pop()
            k-=1
            if k==0:
                return p.val
            p=p.right
        return -1
