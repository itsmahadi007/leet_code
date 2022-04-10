# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def get_list (head):
            linked_list = []
            while head is not None:
                linked_list.append(head.val)
                head = head.next
            return linked_list
        
        
        def get_linked_list(linked_list):
            head = ListNode()
            try:
                head.val = linked_list[-1]
            except:
                return None
            
            for item in linked_list[-2::-1]:
                t_h = ListNode()
                t_h.val = item
                t_h.next = head
                head = t_h
            return head
        
                
        
        linked_list = get_list(head)
        del linked_list[-n]
        return get_linked_list(linked_list)
