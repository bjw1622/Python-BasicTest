import sys


class Node:
    index = 0

    def __init__(self, data):
        self.index = Node.index
        Node.index += 1
        self.data = data
        self.neighbors = []

        self.key = sys.maxsize
        self.memo = None
        self.is_done = False  #방문 안한상태 깃발 x

    def get_index(self):
        return self.index

    def get_data(self):
        return self.data

    def get_neighbors(self):
        return self.neighbors

    def get_key(self):
        return self.key

    def get_memo(self):
        return self.memo

    def get_is_done(self):
        return self.is_done

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def set_key(self, key, memo): #memo는 weight
        if (self.key > key):
            self.key = key
            self.memo = memo

    def set_is_done(self):
        self.is_done = True


class Graph:

    def __init__(self, nodes, matrix):
        self.nodes = nodes
        self.matrix = matrix

    def execute_prim(self):
        num = 0
        current = self.nodes[0]
        while num< 9: #0~8까지 반복
            num = num+1
            current.set_is_done() #깃발 올리기
            if current == self.nodes[0]:
                current.set_key(0, None)

            for x in range(1, len(self.nodes)):
                y = current.get_index()
                if matrix[y][x] > 0:
                    if nodes[x].get_is_done() == False: #깃발 올리지 않은거
                        self.nodes[x].set_key(matrix[y][x], current)
            Low = sys.maxsize
            for z in range(0, len(self.nodes)):
                if self.nodes[z].get_is_done() is not True:
                    if Low > self.nodes[z].get_key():
                        Low = self.nodes[z].get_key()
                        current = self.nodes[z]
            if num == 9: # 0~8까지 방문하고 stop
                break

        self.print_result()

    def print_result(self):
        for node in self.nodes:
            if node.get_memo() is not None:
                print(node.get_data() + ' - ' + node.get_memo().get_data() +
                      ' (' + str(node.get_key()) + ')')


# create an array whose elements are alphabets from 'A' to 'I' using ascii code
dataset = []
for i in range(65, 74):
    dataset.append(chr(i))

# create nodes
nodes = []
for data in dataset:
    nodes.append(Node(data))

# create matrix for weights
matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],  # w.r.t node A
          [4, 0, 8, 0, 0, 0, 0, 11, 0],  # w.r.t node B
          [0, 8, 0, 7, 0, 4, 0, 0, 2],  # w.r.t node C
          [0, 0, 7, 0, 9, 14, 0, 0, 0],  # w.r.t node D
          [0, 0, 0, 9, 0, 10, 0, 0, 0],  # w.r.t node E
          [0, 0, 4, 14, 10, 0, 2, 0, 0],  # w.r.t node F
          [0, 0, 0, 0, 0, 2, 0, 1, 6],  # w.r.t node G
          [8, 11, 0, 0, 0, 0, 1, 0, 7],  # w.r.t node H
          [0, 0, 2, 0, 0, 0, 6, 7, 0]]  # w.r.t node I

# set neighbor relation
for i in range(0, len(nodes)):
    for j in range(i + 1, len(nodes)):
        if matrix[i][j] > 0:
            nodes[i].add_neighbor(nodes[j])
            nodes[j].add_neighbor(nodes[i])

# create a graph
graph = Graph(nodes, matrix)

# execute prim algorithm
graph.execute_prim()