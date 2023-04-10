from TreeNode import TreeNode
import math

def print_preorder(node):
    if node == None:
        return
    
    print(node.value)
    print_preorder(node.left)
    print_preorder(node.right)

def print_inorder(node):
    if node == None:
        return
    print_inorder(node.left)
    print(node.value)
    print_inorder(node.right)

def search_for_min(node):
    while node is not None:
        mi = node.value
        print(mi)
        node = node.left
    return mi

def search_for_max(node):
    while node is not None:
        ma = node.value
        print(ma)
        node = node.right
    return ma

def insert(node, val):
    new_node = TreeNode(val)

    root:TreeNode =  node
    prev = None
    while root is not None:
        prev = root
        if (val < root.value):
            root = root.left
        else:
            root = root.right
    
    if prev is None:
        prev = new_node
    elif val < prev.value:
        prev.left = new_node
    else: 
        prev.right = new_node

    return prev

    # if val < node.value:
    #     node.left = insert(node.left, val)
    # else:
    #     node.right = insert(node.right, val)
    
    return node


def print_subtree_preorder(node, val):
    while node is not None and node.value != val:
        if node.value < val:
            node = node.right
        else:
            node = node.left
    
    print_preorder(node)

def delete_nodes_by_values(main_node:TreeNode, values:list):
    
    for value in values:
        main_node = delete_element_by_value(main_node, value)
    return main_node



def delete_element_by_value(node, val):
    if node is None:
        return node
    
    if val < node.value:
        node.left =  delete_element_by_value(node.left, val)
    elif val > node.value:
        node.right = delete_element_by_value(node.right, val)

    else:
        if node.left is None:
            temp =node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp
    
        temp = search_for_min(node.right)

        node.value = temp

        node.right = delete_element_by_value(node.right, temp)

    return node

    
def height(node:TreeNode):
    if node is None:
        return -1
    left_height = height(node.left)
    right_height = height(node.right)
    if left_height > right_height:
        return (left_height+1)
    else:
        return (right_height+1)


def get_balance(node:TreeNode):
    if node is None:
        return 
    return height(node.left) - height(node.right)


def vine(node:TreeNode)->int:
    count = 0
 
    # Make tmp pointer to traverse and right flatten the given BST
    tmp = node.right
 
    # while tmp is not null
    while tmp:
 
        # If left exist for node pointed by tmp then right rotate it
        if tmp.left:
            oldTmp = tmp
            tmp = tmp.left
            oldTmp.left = tmp.right
            tmp.right = oldTmp
            node.right = tmp
 
        # If left dont exists add 1 to count and traverse further right to flatten remaining BST
        else:
            count += 1
            node = tmp
            tmp = tmp.right
 
    return count 
    
    


def second_phase_of_balance(grand: TreeNode, m:int) -> None:
    tmp = grand.right
    for i in range(m):
        oldTmp = tmp
        tmp = tmp.right
        grand.right = tmp
        oldTmp.right = tmp.left
        tmp.left = oldTmp
        grand = tmp
        tmp = tmp.right


def balance(root:TreeNode)->TreeNode:
    # print_preorder(root)
    grand = TreeNode(0)
 
    # assign the right of dummy node as our input BST
    grand.right = root
 
    #  get the number of nodes in input BST and simultaneously convert it into right linked list.
    count = vine(grand)
    # get the height of tree in which all levels are completely filled
    h = int(math.log2(count + 1))
 
    # get number of nodes until second last level
    m = pow(2, h) - 1
 
    # left rotate for excess nodes at last level
    second_phase_of_balance(grand, count - m)
 
    # left rotate till m becomes 0
    # Steps is done as mentioned in algorithm to make BST balanced.
    for m in [m // 2**i for i in range(1, h + 1)]:
        second_phase_of_balance(grand, m)
 
    # return the root of the balanced binary search tree
    # print_preorder(grand.right)
    return grand.right
#zostaje root idk dlaczego
def delete_tree(node:TreeNode)->None:
    if node == None:
        return 
    print("Deleting node: ", node.value)
    node.left = delete_tree(node.left)
    node.right = delete_tree(node.right)
    node = None
    