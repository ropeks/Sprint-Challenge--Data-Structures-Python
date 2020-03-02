from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        else:
            if self.current == self.storage.tail:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head
            else:
                self.storage.overwrite(self.current, item)
                self.current = self.current.next
                self.storage.delete(self.current.next)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        cur_node = self.storage.head
        while cur_node:
            list_buffer_contents.append(cur_node.value)
            cur_node = cur_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
