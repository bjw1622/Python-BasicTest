class Node:

    def __init__(self, key):
        self.key = key #데이터를 속성 int
        self.left = None #child
        self.right = None

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_key(self):
        return self.key


class Binary_search_tree:

    def __init__(self):
        self.root = None

    #def set_root(self, root):
    #    self.root = root

    def get_root(self):
        return self.root

    def search(self,key):
        return self.check(self.root,key)

    def check(self,node,key): #현재의 노드 사용자가 찾고싶어하는거 key
        if node is None:
            return None

        if node.get_key() == key:
            return node
        elif node.get_key() > key:
            return self.check(node.get_left(),key)
        else:
            return self.check(node.get_right(),key)

    def insert(self,node):
        if self.root is None:
            self.root = node
        else:
            self.insert_node(self.root , node)

    def insert_node(self,parent,node):
        if parent.get_key() == node.get_key():#새로 들어온 키랑 부모랑 같으면(있는 데이터일때)
            pass
        else:
            if parent.get_key() > node.get_key(): #부모가 더크다면
                left = parent.get_left()
                if left is None:
                    parent.set_left(node)
                else:
                    self.insert_node(left,node) #왼쪽이 있다면 또 다른 부모의 후보가 된다.
            else:
                right = parent.get_right()
                if right is None:
                    parent.set_right(node)
                else:
                    self.insert_node(right,node)

    def print_tree(self):
        self.print_node(self.root,0)

    def print_node(self,node,depth):
        if node is not None:
            msg = ""
            for i in range(0,depth):
                msg += " "
            msg += str(node.get_key())
            print(msg)
            self.print_node(node.get_left() , depth+1)
            self.print_node(node.get_right(), depth + 1)

    def delete(self,key):
        self.root.deleted = self._delete(self.root,key)
        return deleted

    def _delete(self,node,key):
        if node is None:
            return node




bst = Binary_search_tree()

node_40 = Node(40)
bst.insert(node_40)
node_15 = Node(15)
bst.insert(node_15)
node_69 = Node(69)
bst.insert(node_69)
node_8 = Node(8)
bst.insert(node_8)
node_25 = Node(25)
bst.insert(node_25)
node_54 = Node(54)
bst.insert(node_54)
node_86 = Node(86)
bst.insert(node_86)
node_5 = Node(5)
bst.insert(node_5)
node_10 = Node(10)
bst.insert(node_10)
node_20 = Node(20)
bst.insert(node_20)
node_30 = Node(30)
bst.insert(node_30)
node_50 = Node(50)
bst.insert(node_50)
node_66 = Node(66)
bst.insert(node_66)
node_83 = Node(83)
bst.insert(node_83)
node_90 = Node(90)
bst.insert(node_90)



result = bst.search(66)
if result is None:
    print("fail")
else:
    print("success")

result = bst.search(67)
if result is None:
    print("fail")
else:
    print("success")

print(print_tree)
