#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        # First node
        self.head = None  
        # Last node
        self.tail = None  
        self.size = 0
        # Append items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        # temp = self.head # Initialise temp           
        # count = 0 # Initialise count
        #Loop while end of linked list is not reached
        # while (temp):
        #     count += 1
        #     temp = temp.next
        #     return count
        count = 0
        node = self.head

        while node is not None:
            count += 1
            node = node.next
        return count
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        # This function counts number of nodes in a list
        
            
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Append node after tail, if it exists
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
            
    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.tail is None:
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        current = self.head

        while current != None:
            if quality(current.data) == True:
                return current.data
            
            current = current.next
        return None 

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))
            return
        currentNode = self.head
        if currentNode.data == item: #if head has the item
            self.head = currentNode.next #if head has next... assign next as new head
            if currentNode.next == None: #head is the last item... set self.tail to none
                self.tail = None
            return
        prev = None
        while currentNode != None: #loop until we reach tail
            print("Current node =", currentNode)
            if currentNode.data == item: #if node's data is the item... found!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
                if currentNode.next == None: #if currentNode is the tail because it has no next...
                    self.tail = prev #prev node will now be the new tail
                prev.next = currentNode.next #DELETE currentNode by removing prev's next (reference) to currentNode's next
                return
            # TODO: Update previous node to skip around node with matching data
            prev = currentNode #if currentNode's data is not item, 
            currentNode = currentNode.next #keep going til it reach the tail
            print("Current.next = ", currentNode)
        # TODO: Otherwise raise error to tell user that delete has failed
        raise ValueError('Item not found: {}'.format(item))
        # if self.length() == 0:
        #     raise ValueError('Item not found: {}'.format(item))

        # #see if node that we want deleted is the head
        # if self.head.data == item:
        #     self.head = self.head.next
        #     self.size -= 1
        #     if self.length() == 0:
        #         self.tail = None
        #     return
        # #see if node that we want deleted is the tail
        # if self.tail.data == item:
        #     temp = self.tail.prev
        #     temp.next = None
        #     self.tail = temp
        #     self.size -= 1
        #     if self.length() == 0:
        #         self.head = None
        #     return

        # prev_node = self.head
        # curr_node = prev_node.next

        # found = False
        # #while node is not found look at the next node
        # while curr_node is not None:
        #     if curr_node.data == item:
        #         #node is found, route around node
        #         prev_node.next = curr_node.next
        #         temp = curr_node.next
        #         temp.prev = prev_node
        #         found = True
        #         self.size -= 1
        #     prev_node = curr_node
        #     curr_node = curr_node.next
        #     if found == True:
        #         return

        # #if node is not found, raise error
        # if found == False:
        #     raise ValueError('Item not found: {}'.format(item))



if __name__ == '__main__':
    test_linked_list()
