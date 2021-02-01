class Node:
    def __init__(self,data):
        self.data= data
        self.tail = None
        self.next = None

    def set_prev(self,prev): #너 전에거 이거 해
        self.prev = prev

    def set_next(self,next): #너 다음거 이거해
        self.next = next

    def get_data(self): #너 데이터 뭐야?
        return self.data

    def get_prev(self): #너 전에거 뭐야?
        return self.prev

    def get_next(self): # 너 다음거 뭐야?
        return self.next

class Douby_linked_list:
    def __init__(self):
        self.header = None
        self.tail = None
        self.size = 0

    def print_list(self):
        print(">> current list")
        node = self.header
        while node is not None:
            print(node.get_data())
            node = node.get_next()
        print(">>>>>>>>>>>>>")

    def append(self,data):
        new_node = Node(data)
        self.size +=1
        if self.header is None: #헤더가 존재한다면
            self.header = new_node # 뉴노드를 헤더로 할당
        else: #헤더가 존재 안한다면
            self.tail.set_next(new_node) # 테일아 너 다음꺼를 뉴노드로 할게
            new_node.set_prev(self.tail)  # 뉴노드야 너 전에꺼를 테일로 할게.
        self.tail = new_node #뉴 노드를 테일로 할당

    def get_at(self,index):
        if index >= self.size:
            return None
        else:
            node = self.header
            for i in range(0,index):
                node = node.get_next()
            return node

    def search(self,fruit):
        node= self.header
        while node is not None:
            if node.get_data() ==fruit:
                return node
            node = node.get_next()
        return None

    def get_near_by(self,data,scope):
        lsit= []
    retrun list






dll = Douby_linked_list()
dll.append("Apple")
dll.append("Kiwi")
dll.append("Banana")
dll.append("Melon")
dll.append("Orange")
dll.append("Blackberry")

list = dll.get_near_by('Banana',2)
for node in list:
    print(node.get_data())
print("==================")
list = dll.get_near_by('Apple',3)
for node in list:
    print(node.get_data())
