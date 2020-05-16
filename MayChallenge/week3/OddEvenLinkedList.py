
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        i = 1
        even = ListNode()
        odd = ListNode()
        start = odd
        starte = even
        last = ListNode()
        while(head != None):
            if(i % 2 == 1):
                odd.val = head.val
                odd.next = ListNode()
                odd = odd.next
            else:
                last = even
                even.val = head.val
                even.next = ListNode()
                even = even.next
            head = head.next
            i += 1
        last.next = None
        odd.val = starte.val
        odd.next = starte.next
        return start
