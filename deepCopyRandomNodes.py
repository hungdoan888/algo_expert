# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:11:30 2021

@author: hungd
"""

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
        
        
def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None: return head
		
		# Clone eg. 1-2->3->None= 1->new_node(1)->2->new_node(2)->3->new_node(3)->None
        cur = head
        while cur:
            temp = cur.next
            cur.next = Node(cur.val)
            cur.next.next = temp
            cur = temp

        # Set up the random
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else cur.random
            cur = cur.next.next

        # detach
        cloned = head.next
        cur = head
        while cur.next:
            temp = cur.next
            cur.next = cur.next.next
            cur = temp
        return cloned
    
    
    
    
    
    
    
    
    
    
    