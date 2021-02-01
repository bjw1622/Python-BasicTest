class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.visited = False #처음 방문 x

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)  #이웃 추가

    def set_visited(self, visited):
        self.visited = visited # 방문 기록

    def get_data(self): #데이터 가져와
        return self.data

    def get_neighbors(self): #주변 이웃 가져와
        return self.neighbors

    def get_visited(self): # 이미 방문 했니
        return self.visited


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def bfs(self):
        if len(self.nodes) > 0:
            for node in self.nodes:
                node.set_visited(False)  #깃발 다 내리기

        queue = [] # 큐 준비
        self.nodes[0].set_visited(True) #0번째 노드 시작 깃발 올리기
        print(self.nodes[0].get_data(),end = "") # 적기
        queue.append(self.nodes[0]) #  큐로 추가하기(큐가0이면 끝)
        while len(queue) > 0: #큐에 뭔가가 들어있음 계속 해라
            current = queue.pop(0) # 가장 앞에있는거 pop(디큐 처럼 사용)
            neighbors = current.get_neighbors() # 팝 한거를 current노드
            for neighbor in neighbors: # neighbor의 이웃들
                if not neighbor.get_visited(): # 아직 방문 안된 애들
                    neighbor.set_visited(True) # 깃발올리고
                    print(" - " + neighbor.get_data(), end="") # 적어주고
                    queue.append(neighbor) # 큐에 추가해준다
        print("")

    def dfs(self):
        if len(self.nodes) > 0:
            for node in self.nodes:
                node.set_visited(False)

        self.visit(self.nodes[0])
        print("")

    def visit(self,node):
        node.set_visited(True)
        print(node.get_data(), end =" ")
        neighbors = node.get_neighbors()
        for neighbor in neighbors:
            if not neighbor.get_visited():
                self.visit(neighbor )



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
node_S = Node('S')
graph.add_node(node_S)

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_S)

node_B.add_neighbor(node_A)

node_C.add_neighbor(node_D)
node_C.add_neighbor(node_E)
node_C.add_neighbor(node_F)
node_C.add_neighbor(node_G)
node_C.add_neighbor(node_S)

node_D.add_neighbor(node_C)

node_E.add_neighbor(node_C)
node_E.add_neighbor(node_H)

node_F.add_neighbor(node_C)
node_F.add_neighbor(node_G)

node_G.add_neighbor(node_F)
node_G.add_neighbor(node_S)

node_H.add_neighbor(node_E)
node_H.add_neighbor(node_G)

node_S.add_neighbor(node_A)
node_S.add_neighbor(node_C)
node_S.add_neighbor(node_G)

print("[BFS result]")
graph.bfs()

print("[DFS result]")
graph.dfs()