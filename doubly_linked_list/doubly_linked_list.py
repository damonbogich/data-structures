"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        #if linked list is empty- set new node to head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current_head = self.head
            current_head.prev = new_node
            self.head = new_node
            new_node.next = current_head

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        #empty list
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else: 
            self.length -= 1
            current_head = self.head
            self.head = current_head.next
            self.head.prev = None
        return value


    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        new_tail = ListNode(value)
        #empty List:
        if self.head is None:
            self.head = new_tail
            self.tail = new_tail
        else:
            current_tail = self.tail
            current_tail.next = new_tail
            self.tail = new_tail
            self.tail.prev = current_tail

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        current_tail = self.tail
        #empty DLL:
        if self.head is None:
            return None
        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current_tail.prev = self.tail
            self.tail.next = None 
            self.length -= 1
        return current_tail.value
            
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        input_node = node
        current_head = self.head
        current_tail = self.tail
        #empty DLL:
        if self.head is None:
            return None
        #input node value = head value
        elif self.head.value == input_node.value:
            self.head = self.head
        #input node value = tail value

        
        elif self.tail.value == input_node.value:
            #set tail to tail.prev
            self.tail = current_tail.prev
            #set new tail.next to None
            self.tail.next = None
            #set old head.prev to new head
            current_head.prev = current_tail
            #sets head to old tail
            self.head = current_tail
            #sets new head's prev to None
            self.head.prev = None
            self.head.next = current_head


        else:
            search = self.head
            while search.value != input_node.value:
                search = search.next
            #now I'm assuming search.val = input.val
            
            #remove search from current spot:
            search.prev.next = search.next
            search.next.prev = search.prev

            #move search to head:
            current_head.prev = search
            self.head = search
            self.head.prev = None
            self.head.next = current_head

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        input_node = node
        current_head = self.head
        current_tail = self.tail
        #empty DLL:
        if self.head is None:
            return None
        #input node value = tail value
        elif self.tail.value == input_node.value:
            self.tail = self.tail


        elif self.head.value == input_node.value:
            #set head to head.next
            self.head = self.head.next
            self.head.prev = None

            #set current head to tail
            current_tail.next = current_head
            self.tail = current_head
            self.tail.next = None
            self.tail.prev = current_tail
        else:
            search = self.tail
            while search.value != input_node.value:
                search = search.prev
            
            #assuming value's in there in there
            search.prev.next = search.next
            search.next.prev = search.prev

            #make search new tail:
            current_tail.next = search
            self.tail = search
            self.tail.prev = current_tail
            self.tail.next = None

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        input_node = node
        current_head = self.head
        current_tail = self.tail
        
        #empty DLL
        if self.head is None:
            return None
        # 1 node in DLL
        elif self.head is self.tail:
            self.length -= 1
            self.head = None
            self.tail = None
        #node = self.head
        elif self.head.value == input_node.value:
            self.length -= 1
            self.head = current_head.next
            self.head.prev = None
        #node = self.tail
        elif self.tail.value == input_node.value:
            self.length -= 1
            self.tail = current_tail.prev
            self.tail.next = None
        #node isn't head or tail
        else: 
            self.length -= 1
            search = self.head
            while search.value != input_node.value:
                search = search.next
            #assuming it's there
            search.prev.next = search.next
            search.next.prev = search.prev


        


        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        
        if not self.head and self.tail:
            return None

        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
        return max_value