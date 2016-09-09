# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        temp=head.next
        head.next=self.swapPairs(temp.next)
        temp.next=head
        return temp



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur=head
        head=head.next
        left=None
        while(cur and cur.next):
            p1,p2=cur,cur.next
            p1.next,p2.next=p2.next,p1
            if left:
                left.next=p2
            cur,left=p1.next,p1
        return head


