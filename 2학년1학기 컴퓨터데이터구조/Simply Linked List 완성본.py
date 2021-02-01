class Node:
    def __init__(self, fruit): #init은 초기화하다. self
        self.fruit = fruit
        self.next = None

    def get_fruit(self): #너가 가진 과일 이름이 뭐야?
        return  self.fruit

    def get_next(self): # 너 옆에 뭐야?
        return  self.next

    def set_next(self, next):# 너 옆에 값은 이거야
        self.next = next

class Simply_linked_list:

    def __init__(self):
        self.header = None
        self.size = 0

    def append(self, fruit):
        new_node = Node(fruit)
        self.size += 1
        if self.header is None:
            self.header = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node

    def print_list(self):
        print(">> current list")
        node = self.header
        while node is not None:
            print(node.get_fruit())
            node = node.get_next()
        print(">>>>>>>>>>>")

    def get_at(self,index):
        if index >= self.size:
            return None
        else:
            node = self.header
            for i in range(0, index):
                node = node.get_next()
            return node

    def search(self,fruit):
        node = self.header
        while node is not None:
            if node.get_fruit() == fruit:
                return node
            node = node.get_next()
        return None

    def delete_at(self, index):
        if index >= self.size:
            pass
        else:
            prev = None
            current = self.header
            for i in range(0, index):
                prev = current
                current = current.get_next()
            if current == self.header:
                self.header = current.get_next()
            else:
                prev.set_next(current.get_next())
            if current == self.tail:
                self.tail = prev


a = Simply_linked_list()
a.append("Apple")
a.append("Kiwi")
a.append("Banana")
a.print_list()

node = a.get_at(1)
if node is not None:
    print(node.get_fruit())
else :
    print("index error")
node = a.get_at(2)
if node is not None :
    print(node.get_fruit())
else:
    print("index error")

node = a.search("Banana")
if node is not None:
    print("We have it")
else:
    print("We don't have it")

