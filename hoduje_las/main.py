from bst_random import create_random_bst
from functions_for_both import search_for_max, search_for_min, print_inorder, delete_tree, print_subtree_preorder, delete_element_by_value, print_preorder, balance, get_balance, delete_nodes_by_values, vine
from avl import create_avl_from_arr



l1 = [9,2,15,1,4,8,11,5,7,10,13,12,14]


root_bts = create_random_bst(l1)
# root_bts = balance(root_bts)
print_inorder(root_bts)