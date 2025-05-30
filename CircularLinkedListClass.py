from NodeClass import *

class CircularLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def append(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        new_node = Node(element)
        if self.size == 0:
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, element: str, index: int) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character")
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")
        if index == self.size:
            self.append(element)
            return
        new_node = Node(element)
        if index == 0:
            if self.size == 0:
                new_node.next = new_node
                self.tail = new_node
            else:
                new_node.next = self.tail.next
                self.tail.next = new_node
            self.size += 1
            return
        current = self.tail.next
        for _ in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        if self.size == 1:
            deleted_value = self.tail.data
            self.tail = None
            self.size = 0
            return deleted_value
        if index == 0:
            deleted_value = self.tail.next.data
            self.tail.next = self.tail.next.next
            self.size -= 1
            return deleted_value
        current = self.tail.next
        for _ in range(index - 1):
            current = current.next
        deleted_value = current.next.data
        if current.next == self.tail:
            self.tail = current
        current.next = current.next.next
        self.size -= 1
        return deleted_value

    def deleteAll(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1 or self.size == 0:
            return
        i = self.size - 1
        while i >= 0:
            if self.get(i) == element:
                self.delete(i)
            i -= 1

    def get(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        current = self.tail.next
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self):
        new_list = CircularLinkedList()
        if self.size == 0:
            return new_list
        current = self.tail.next
        for _ in range(self.size):
            new_list.append(current.data)
            current = current.next
        return new_list

    def reverse(self) -> None:
        if self.size <= 1:
            return

        prev = self.tail
        current = self.tail.next
        head = current

        for _ in range(self.size):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.tail = head

    def findFirst(self, element: str) -> int:
        if not isinstance(element, str) or len(element) != 1 or self.size == 0:
            return -1
        current = self.tail.next
        for i in range(self.size):
            if current.data == element:
                return i
            current = current.next
        return -1

    def findLast(self, element: str) -> int:
        if not isinstance(element, str) or len(element) != 1 or self.size == 0:
            return -1
        last_index = -1
        current = self.tail.next
        for i in range(self.size):
            if current.data == element:
                last_index = i
            current = current.next
        return last_index

    def clear(self) -> None:
        self.tail = None
        self.size = 0

    def extend(self, elements) -> None:
        if not isinstance(elements, CircularLinkedList):
            raise TypeError("Argument must be a CircularLinkedList")
        if elements.size == 0:
            return
        current = elements.tail.next
        for _ in range(elements.size):
            self.append(current.data)
            current = current.next

    def __str__(self) -> str:
        if self.size == 0:
            return "[]"
        result = []
        current = self.tail.next
        for _ in range(self.size):
            result.append(current.data)
            current = current.next
        return "[" + ", ".join(f"'{char}'" for char in result) + "]"
