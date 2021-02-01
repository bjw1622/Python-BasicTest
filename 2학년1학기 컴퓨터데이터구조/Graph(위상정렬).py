class   Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def set_visited(self, visited):
        self.visited = visited

    def get_data(self):
        return self.data

    def get_neighbors(self):
        return self.neighbors

    def get_visited(self):
        return self.visited


class Graph:
    def __init__(self):
        self.nodes = []
        self.x = []

    def add_node(self, node):
        self.nodes.append(node)

    def topological_sort(self):

        if len(self.nodes) > 0: #노드의 갯수가 0보다 크면
            for node in self.nodes:
                node.set_visited(False) #깃발 다 내리기

        for i in range(0,len(self.nodes)):
            if not self.nodes[i].get_visited():
             self.visit(self.nodes[i])  # 맨 처음 노드 방문하고

        self.x.reverse()
        for i in range (0,len(self.x)):
            print(self.x[i].data)

    def visit(self,node):
        node.set_visited(True) # 깃발 꽂고
        #print(node.get_data(), end ="")  #그 노드 출력하고 한칸띄고
        neighbors = node.get_neighbors() #그 노드의 이웃을 이웃이라고함.
        for neighbor in neighbors: #이웃이 있는동안
            if not neighbor.get_visited():#이웃이 깃발 x면
                self.visit(neighbor) #이웃으로 방문
        self.x.append(node) # 이웃이 없는거는 x리스트에 담기
        #print(self.x)


graph = Graph()

node_A = Node('A')
graph.add_node(node_A)
node_B = Node('B')
graph.add_node(node_B)
node_C = Node('C')
graph.add_node(node_C)
node_D = Node('D')
graph.add_node(node_D)
node_E = Node('E')
graph.add_node(node_E)
node_F = Node('F')
graph.add_node(node_F)
node_G = Node('G')
graph.add_node(node_G)
node_H = Node('H')
graph.add_node(node_H)
node_I = Node('I')
graph.add_node(node_I)
node_J = Node('J')
graph.add_node(node_J)

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_F)

node_B.add_neighbor(node_H)

node_D.add_neighbor(node_C)
node_D.add_neighbor(node_E)
node_D.add_neighbor(node_I)

node_E.add_neighbor(node_I)

node_G.add_neighbor(node_A)
node_G.add_neighbor(node_B)
node_G.add_neighbor(node_C)

node_I.add_neighbor(node_C)

node_J.add_neighbor(node_E)

graph.topological_sort()