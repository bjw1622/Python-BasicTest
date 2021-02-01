#0

class Node:

    def __init__(self, data):  # 객체 생성
        self.data = data
        self.prev = None

    def get_data(self):  # 너 데이터 뭐냐
        return self.data

    def get_prev(self):  # 너 뒤에 누구니
        return self.prev

    def set_prev(self, prev):  # 너 뒤에 이거야
        self.prev = prev


class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0

    def enqueue(self, data):  # front는 처음만,rear는 게속 바뀜
        new_node = Node(data)
        self.size += 1
        if self.front is None:  # 프론트와 레어가 모두 뉴 노드를 가르킨다!!!
            self.front = new_node
            self.rear = new_node

        else:
            self.rear.set_prev(new_node)  # 레어의 그 뒤의 값을 뉴 노드로 할당
            self.rear = new_node  # 뉴 노드를 레어로 할당!!!!

    def print_queue(self):
        print(">>current queue")
        node = self.front  # 프론트를 노드로 할당
        while node is not None:  # 프론드가 존재한다면
            print(node.get_data())  # 그 프론트 값을 출력해줘
            node = node.get_prev()  # 프론트의 그 뒤의 값을 노드라고 한다.
        print(">>>>>>>>>>>>")

    def dequeue(self):  # 리턴 값 존재  #front값이 바뀜
        node = self.front
        self.size -= 1
        if node is not None:
            self.front = node.get_prev()
        return node


queue = Queue()
queue.enqueue("Apple")
queue.enqueue("Kiwi")
queue.enqueue("Banana")
queue.print_queue()

node = queue.dequeue()
print("Dequeue:" + node.get_data())
node = queue.dequeue()
print("Dequeue:" + node.get_data())

queue.enqueue("Melon")
queue.print_queue()
