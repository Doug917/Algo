# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        if not head:
            return head

        if not head.next:
            return head
        
        #Determine length of linked list.
        length = 0
        head00 = head
        
        while head.next:
            head = head.next
            length += 1

        #switch the values of front and back.
        def switch_front_and_tail_values(head0, length, el):
            p1 = head0.val
            head = head0
            while el < length:
                head = head.next
                p2 = head.val
                el += 1
            head0.val = p2
            head.val = p1

        head0 = head00
        el = 0
        while el < length:
            switch_front_and_tail_values(head0, length, el)
            #repeat
            head0 = head0.next
            length -= 1
            el += 1
        

        return head00
        # #print new list to check.
        # head = head00
        # while head:
        #     print(head.val)
        #     head = head.next
                
