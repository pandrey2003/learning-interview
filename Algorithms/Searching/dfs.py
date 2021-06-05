from DataStructures.Implementation.bst import create_balanced_bst


def dfs_in_order(node, node_list: list):
    if node.left:
        dfs_in_order(node.left, node_list)
    node_list.append(node.value)
    if node.right:
        dfs_in_order(node.right, node_list)
    return node_list


def dfs_pre_order(node, node_list: list):
    node_list.append(node.value)
    if node.left:
        dfs_pre_order(node.left, node_list)
    if node.right:
        dfs_pre_order(node.right, node_list)
    return node_list


def dfs_post_order(node, node_list: list):
    if node.left:
        dfs_post_order(node.left, node_list)
    if node.right:
        dfs_post_order(node.right, node_list)
    node_list.append(node.value)
    return node_list


if __name__ == "__main__":
    my_bst = create_balanced_bst()
    print("DFS in order:", dfs_in_order(my_bst.root, []))
    print("DFS pre order:", dfs_pre_order(my_bst.root, []))
    print("DFS post order:", dfs_post_order(my_bst.root, []))
