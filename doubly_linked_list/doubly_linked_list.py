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
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass