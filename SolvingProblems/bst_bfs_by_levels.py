from DataStructures.Implementation.bst import create_balanced_bst


def level_order(root: 'TreeNode') -> list[list[int]]:
    if root is None:
        return []
    return level_order_recursive([root], [])


def level_order_recursive(queue, node_list):
    if not queue:
        return node_list
    current_level = []
    new_queue = []
    for node in queue:
        current_level.append(node.value)
        if node.left is not None:
            new_queue.append(node.left)
        if node.right is not None:
            new_queue.append(node.right)
    node_list.append(current_level)
    return level_order_recursive(new_queue, node_list)


if __name__ == "__main__":
    my_bst = create_balanced_bst()
    print(level_order(my_bst.root))
