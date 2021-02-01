class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        self.size += 1
        if self.top is None: #탑이 비어있으면
            self.top = new_node #뉴 노드를 탑으로 할당
        else:
            new_node.set_next(self.top) # 뉴 노드의 다음을 탑으로 한다
            self.top = new_node  # 뉴 노드가 탑

    def print_stack(self):
        print(">> current stack")
        node = self.top
        while node is not None:
            print(node.get_data())
            node = node.get_next()
        print(">>>>>>>>>>>>>>>>")

    def pop(self):
        node = self.top
        if node is not None:
            self.top = node.get_next()
            self.size -= 1
        return node

stack = Stack()
stack.push("Apple")
stack.push("Kiwi")
stack.push("Banana")
stack.print_stack()

while True:
    node = stack.pop()
    if node is None:
        break
    else:
        print("Pop:" + node.get_data())
stack.print_stack()