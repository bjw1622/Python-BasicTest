class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return sefl.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.get_right

    def set_left(self,left):
        self.set_left = set_left

    def set_right(self,right):
        self.set_right = set_right
    #def get_data(self): #데이터 뭐야
        #return self.data


    #def get_children(self): #너 자식 뭐야
        #return self.children

    #def add_child(self,child): # 자식 추가해
        #self.children.append(child)

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):   #루트 뭐야
        return self.root

    def set_root(self,root):     #루트 이걸로해
        self.root = root

    def print_tree(self):       #트리 출력
        self.print_node(self.root,0) #a라는 노드와 숫자 0 이 전달

    def print_node(self,node,depth): #노드와 뎁스가0부터 들어옴
        msg = ""
        if node is not None: #노드가 있으면
            for i in range(0,depth):#텅텅 비어있는 메세지에 공백을 몇번이나 추가하는가
                msg += " "
            msg += node.get_data() #노드의 데이터를 꺼내서 문장에 붙이기 처음엔 "A"이다.
            print(msg)
            #여기서부터 제귀함수 동작.
            children = node.get_children() #자식 다가져와  b,c,d
            for i in range(0,len(children)): # 자식 한명 한명 처리 len(children) 자식 갯수
                self.print_node(children[i] , depth+1) # i가 0일때는 B 뎁스는 2가 된다

tree = Tree()
node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")
node_h = Node("H")
node_i = Node("I")
node_j = Node("J")
node_k = Node("K")
node_l = Node("L")
node_m = Node("M")
node_n = Node("N")
node_o = Node("O")
node_p = Node("P")

tree.set_root(node_a) #트리랑 노드 연결
node_a.add_child(node_b)
node_a.add_child(node_c)
node_a.add_child(node_d)

node_b.add_child(node_e)
node_b.add_child(node_f)
node_b.add_child(node_g)

node_c.add_child(node_h)
node_c.add_child(node_i)

node_d.add_child(node_j)

node_e.add_child(node_k)
node_e.add_child(node_l)

node_g.add_child(node_m)

node_h.add_child(node_n)

node_j.add_child(node_o)
node_j.add_child(node_p)

tree.print_tree()

