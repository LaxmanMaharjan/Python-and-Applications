from random import randint
count = 0
class BST:
    class __Node:
        def __init__(self, value, left = None, right = None):
            self.value = value
            self.left = left
            self.right = right

        def get_value(self):
            return self.value

        def set_value(self,newvalue):
            self.value = newvalue

        def get_left(self):
            return self.left

        def set_left(self,newvalue):
            self.left = newvalue

        def get_right(self):
            return self.right

        def set_right(self,newvalue):
            self.right = newvalue

        def __iter__(self):
            """
            It is for inorder traversal in Bst.So, the result is the values in ascending order
            :return:
            """
            if self.left != None:
                for elem in self.left:
                    yield elem

            yield self

            if self.right != None:
                for elem in self.right:
                    yield elem

    def __init__(self):
        self.root = None

    def insert(self,value):
        # The __insert function is recursive and is not a passed a self parameter. It is a
        # static function (not a method of the class) but is hidden inside the insert
        # function so users of the class will not know it exists.

        def __insert(root,value):
            if root == None:
                return BST.__Node(value)
            if value < root.get_value():
                root.set_left(__insert(root.get_left(),value))
            elif value > root.get_value():
                root.set_right(__insert(root.get_right(),value))
            return root

        self.root = __insert(self.root,value)

    def delete_node(self,value):
        parent,node = self.search(value)
        # print(parent.__dict__)
        # print(node.__dict__)

        # Node to be deleted is not found case
        if node == None or node.get_value() != value:
            return False

        # Node has no child ie left node
        elif node.get_left() == None and node.get_right() == None:
            if value < parent.get_value():
                parent.set_left(None)
            else:
                parent.set_right(None)
            return True

        # Node has a left child only
        elif node.get_left() != None and node.get_right() == None:
            if node.get_value() < parent.get_value():
                parent.set_left(node.get_left())
            else:
                parent.set_right(node.get_left())
            return True

        #Node has a right child only
        elif node.get_right() != None and node.get_left() == None:
            if node.get_value() < parent.get_value():
                parent.set_left(node.get_right())
            else:
                parent.set_right(node.get_right())
            return True

        #Node has both child
        else:
            max_node = self.find_max_node(node.get_left())
            self.delete_node(max_node.get_value())
            node.set_value(max_node.get_value())
            return True

    def search(self,value):
        parent = None
        node = self.root
        # This will find the required node and it's parent node
        while node and node.get_value() != value:
            parent = node
            if value < node.get_value():
                node = node.get_left()
            elif value > node.get_value():
                node = node.get_right()
        return parent,node

    def find_node(self,value):
        for i in self.root:
            if i.get_value() == value:
                return i

    def find_min_node(self,node = None):
        if node == None:
            node = self.root
        else:
            if node != None:
                while node.get_left() != None:
                    node = node.get_left()
        return node

    def find_max_node(self, node = None):
        if node == None:
            node = self.root
        else:
            if node != None:
                while node.get_right() != None:
                    node = node.get_right()
        return node
    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

def main():
    num_list = [55,45,65,40,50,60,70,80,35]
    tree = BST()
    for i in num_list:
        tree.insert(int(i))

    # for i in tree.root.left:
    #     print(i.get_value())
    #
    # node = tree.find_node(50)
    # print(node.get_right())
    #
    print(tree.delete_node(55))
    for i in tree.root:
        print(i.get_value())

    # tree1 = BST()
    # tree1.insert(45)
    # tree1.insert(40)
    # tree1.root.left = None
    # print(tree1.root.__dict__)

if __name__ == "__main__":
    main()