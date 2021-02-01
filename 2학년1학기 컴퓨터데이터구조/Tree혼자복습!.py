class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def get_data(self): #너 데이터 뭐야
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
        self.print_node(self.root,0)

    def print_node(self,node,depth):
        msg = ""
        if node is not None:
            for i in range(0,depth):
                msg += " "
            msg += node.get_data()
            print(msg)

            self.print_node(node.get_left() , depth+1)
            self.print_node(node.get_right() , depth)

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