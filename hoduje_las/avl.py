import numpy as np
from functions_for_both import insert
from TreeNode import TreeNode

def create_avl_from_arr(arr):
    if len(arr) > 0:
        
        mid_idx = len(arr)//2
        mid = arr[mid_idx]
        
        root = insert(TreeNode(mid), mid)
        root.left = create_avl_from_arr(arr[:mid_idx])
        root.right = create_avl_from_arr(arr[mid_idx+1:])
    
        return root