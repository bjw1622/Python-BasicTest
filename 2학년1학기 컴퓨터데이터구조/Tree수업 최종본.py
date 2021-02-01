class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self): #데이터 뭐야
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_left(self,left):
        self.left = left

    def set_right(self,right):
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self,root):
        self.root = root

    def print_tree(self):
        self.print_node(self.root,0) #a라는 노드와 숫자 0 이 전달

    def print_node(self,node,depth): #노드와 뎁스가0부터 들어옴
        msg = ""
        if node is not None: #노드가 있으면
            for i in range(0,depth):#텅텅 비어있는 메세지에 공백을 몇번이나 추가하는가
                msg += " "
            msg += node.get_data() #노드의 데이터를 꺼내서 문장에 붙이기 처음엔 "A"이다.
            print(msg)
            #여기서부터 제귀함수 동작.
            #children = node.get_children() #자식 다가져와  b,c,d
            #for i in range(0,len(children)): # 자식 한명 한명 처리
                #self.print_node(children[i] , depth+1) # i가 0일때는 B 뎁스는 2가 된다
            self.print_node(node.get_left(),depth+1)
            self.print_node(node.get_right(),depth) 

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



tree.set_root(node_a)  #트리랑 노드 연결

node_a.set_left(node_b)

node_b.set_left(node_e)
node_b.set_right(node_c)

node_c.set_left(node_h)
node_c.set_right(node_d)

node_d.set_left(node_j)

node_e.set_left(node_k)
node_e.set_right(node_f)

node_f.set_right(node_g)

node_g.set_left(node_m)

node_h.set_left(node_n)
node_h.set_right(node_i)

node_j.set_left(node_o)

node_k.set_right(node_l)

node_o.set_right(node_p)


tree.print_tree()


