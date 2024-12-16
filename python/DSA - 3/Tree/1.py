class BST:
    def __init__(self, key):
        self.key = key
        self.lchild = None                          # Implementation of Binary Search Tree
        self.rchild = None          

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        
        if self.key == data:                        # Don't mind if there's duplicate values
            return

        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)             # Inserting values to a Binary Search Tree
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

    def searchit(self, data):
        if self.key == data:
            print('The node is found')
            return
        
        if self.key > data:
        
            if self.lchild:
                self.lchild.searchit(data)
            else:
                print('Node is not present')
            
        else:
            if self.rchild:
                self.rchild.searchit(data)
            else:
                print('Node is not present')

    def pre_trav(self):
        print(self.key, end=' ')
        if self.lchild:
            self.lchild.pre_trav()
        if self.rchild:
            self.rchild.pre_trav()

    def in_trav(self):
        if self.lchild:
            self.lchild.in_trav()
        print(self.key, end=' ')
        if self.rchild:
            self.rchild.in_trav()

    def post_trav(self):
        if self.lchild:
            self.lchild.post_trav()
        if self.rchild:
            self.rchild.post_trav()
        print(self.key, end=' ')

    def deletion(self, data):
        if self.key is None:
            print('The tree is empty')
            return None

        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.deletion(data)
            else:
                print("The node is not present in the tree")
        
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.deletion(data)
            else:
                print('The node is not present in the tree')

        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            elif self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            temp = self.lchild
            while temp.rchild:  
                temp = temp.rchild

            self.key = temp.key

            self.lchild = self.lchild.deletion(temp.key)

        return self
    
    def find_closest(self, target):
        closest = self.key
        current_node = self
        while current_node:
            if abs(target - closest) > abs(target - current_node.key):
                closest = current_node.key
            if target < current_node.key:
                current_node = current_node.lchild
            elif target > current_node.key:
                current_node = current_node.rchild
            else:
                break
        return closest

    def is_valid_bst(self, min_val=float('-inf'), max_val=float('inf')):
        if not self:
            return True
        if not (min_val < self.key < max_val):
            return False
        is_left_valid = self.lchild.is_valid_bst(min_val, self.key) if self.lchild else True
        is_right_valid = self.rchild.is_valid_bst(self.key, max_val) if self.rchild else True
        return is_left_valid and is_right_valid

root = BST(10)
x = [1,21,43,41,65,4,13]
for i in x:
    root.insert(i)

# root.searchit(3)
print('this is preorder')
root.pre_trav()
# print()
# print('this is inorder')
# root.in_trav()
# print()
# print('this is postorder')
# root.post_trav()
root.deletion(4)
print('after deleting')
root.pre_trav()
print("\n\nClosest value to 10:", root.find_closest(19))
print("\nIs the tree a valid BST?", root.is_valid_bst()) 