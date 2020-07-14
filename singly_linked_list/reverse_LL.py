def reverse_ll(ll):
    #will receive linked list as input and returns reverse
    #order of that linked list

    """
    steps:
    1. Each node needs to point at the previous node
    2. Head and tail pointers need to be flipped

    cases:
    1. if linked list is empty return the original that is passed in
    
    """
    #if LL is empty, return LL
    if ll.head is None:
        return ll
    #if LL has one node,
    if ll.head is ll.tail:
        return ll
    #if LL has more than one node
    current = ll.head
    previous = None
    next_node = None
    while current is not None:
        #store a pointer to the current next value
        next_node = current.get_next()

        #switch current's next pointer to previous (None for head)
        current.set_next(previous)

        #increment logic:
        previous = current
        current = next_node

    ll.head, ll.tail = ll.tail, ll.head
        


