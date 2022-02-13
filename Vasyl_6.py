dummy = ListNode(-1)
p = dummy
p1 = list1
p2 = list2

while p1 is not None and p2 is not None: #2
    if p1.val > p2.val:
        p.next = p2
        p2 = p2.next
    else:
        p.next = p1
        p1 = p1.next
    p = p.next

if p1 is not None:
    p.next = p1
    
if p2 is not None:
    p.next = p2
    
return dummy.next    #2
  
