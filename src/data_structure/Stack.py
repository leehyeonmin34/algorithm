# 배열
# class stack:
#     def __init__(self, size):
#         self.s = [None] * size
#         self.next = 0
#
#     def push(self, val):
#         self.s[self.next] = val
#         self.next += 1
#
#     def pull(self):
#         self.next -= 1
#         return self.s[self.next]

# 링크드 리스트

class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class Stack:
    def __init__(self):
        self.last = self.head = Node(None)

    def push(self, val):
        node = Node(val)
        node.prev = self.last
        self.last.next = node
        self.last = self.last.next

    def pull(self):
        if self.last != self.head:
            to_pop_node = self.last
            to_pop_node.prev.next = None
            self.last = to_pop_node.prev
            return to_pop_node.val


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pull())
print(s.pull())
print(s.pull())
