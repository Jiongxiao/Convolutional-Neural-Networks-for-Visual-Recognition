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


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        count=self.countNodes(root.left)
        if k<=count:
            return self.kthSmallest(root.left,k)
        if k==count+1:
            return root.val
        else:
            return self.kthSmallest(root.right,k-count-1)

    def countNodes(self,node):
        if not node:
            return 0
        return self.countNodes(node.left)+self.countNodes(node.right)+1

