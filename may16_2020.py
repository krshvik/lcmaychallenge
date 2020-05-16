class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head 
        
        if head.next is None or head.next.next is None:
            return head
        
        earr = []
        oarr = []
        i = 1
        while head is not None:
            if i%2 == 1:
                oarr.append(head)
            else:
                earr.append(head)
            head = head.next 
            i = i + 1
        
        for e in earr:
            e.next = None
        for o in oarr:
            o.next = None
            
        leno =  len(oarr)
        i = 0 
        while i < leno:
            if i + 1 < leno:
                oarr[i].next = oarr[i+1]
            i = i + 1 
        
        lene = len(earr)
        i = 0 
        while i < lene:
            if i + 1 < lene:
                earr[i].next = earr[i+1]
            i = i + 1 
        
        oarr[leno-1].next = earr[0]
        
        return oarr[0]