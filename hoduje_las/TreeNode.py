class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


# class AvlTree:
#     def __init__(self, root=None):
#         self.root =None
    
#     def insert(self,val):
#         if self.root is None:
#             return TreeNode(val)
#         if val < self.root.value:
#             node.left = self.insert(self.root.left, val)
#         else:
#             node.right = self.insert(self.root.right, val)
        
#         return node
    
#     def create_avl_from_arr(self,arr):
#         if len(arr) > 0:
            
            
#             mid_idx = len(arr)//2
#             mid = arr[mid_idx]
            
#             root = self.insert(None, mid)
#             root.left = self.create_avl_from_arr(arr[:mid_idx])
#             root.right = self.create_avl_from_arr(arr[mid_idx+1:])
        
#             return root

#     def delete_tree(self, node):
#         if self.root is not None:
#             self.delete_tree(self.root.left)
#             self.delete_tree(node.right)
#             print(node.value)