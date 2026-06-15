class Solution:
    def removeNthFromEnd(self, head, n):
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        if n == len(nodes):
            return head.next

        nodes[-n-1].next = nodes[-n].next

        return head
