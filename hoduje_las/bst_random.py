from TreeNode import TreeNode

from functions_for_both import insert

def create_random_bst(arr):
    if len(arr) <1:
        return None
    root = TreeNode(arr[0])
    for i in range(1, len(arr)):
        insert(root, arr[i])
    
    return root





