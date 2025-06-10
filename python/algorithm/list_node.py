
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
def build_list(data: list[int]) -> ListNode:
  # head = ListNode()
  # return map(lambda x : ListNode(x) )
  
  head = None
  
  for x in range(data):
    if not head:
      head = ListNode(x)
    else:
      head.next = ListNode(x)
    
  return head