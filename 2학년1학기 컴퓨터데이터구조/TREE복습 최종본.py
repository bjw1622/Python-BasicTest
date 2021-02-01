"""class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

    def get_data(self): #너 데이터 뭐야
        return self.data


    def get_children(self): #너 자식 뭐야
        return self.children


    def add_child(self,child): #너 자식 이걸로 추가해
        self.children.append(child)

class Tree:

    def __init__(self):
        self.root = None


    def get_root(self):
        return self.root

    def set_root(self,root):
        self.root = root

    def print_tree(self):
        self.print_node(self.root,0)
        # root랑 뎊스를 0 으로 처음 출력
    def print_node(self,node,depth):
        msg = " "
        if node is not None: #노드가 존재한다면
            for i in range(0,depth):# i가 0부터 depth-1에 있을때
                msg += " " # 메세지에 공백을 더하라
            msg += node.get_data()
            print(msg)
        children = node.get_children()
        for i in range(0,len(children)):
            self.print_node(children[i],depth+1)



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
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

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
        # root랑 뎊스를 0 으로 처음 출력
    def print_node(self,node,depth):
        msg = " "
        if node is not None: #노드가 존재한다면
            for i in range(0,depth):# i가 0부터 depth-1에 있을때
                msg += " " # 메세지에 공백을 더하라
            msg += node.get_data()
            print(msg)

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

tree.set_root(node_a) #트리랑 노드 연결
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












