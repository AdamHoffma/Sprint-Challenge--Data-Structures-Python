from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length >= 0 and self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail        
        elif self.current is self.storage.tail:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
        else:
            self.current.insert_after(item)
            self.storage.length += 1
            self.current = self.current.next
            self.storage.delete(self.current.next)
            
            
        
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next
        
        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
