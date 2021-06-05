from DataStructures.Implementation.bst import create_balanced_bst


def breadth_first_search(bst):
    queue = [bst.root]
    node_list = []
    while queue:
        current_node = queue.pop(0)
        node_list.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return node_list


def breadth_first_search_recursive(queue, node_list):
    if not queue:
        return node_list
    current_node = queue.pop(0)
    node_list.append(current_node.value)
    if current_node.left:
        queue.append(current_node.left)
    if current_node.right:
        queue.append(current_node.right)
    return breadth_first_search_recursive(queue, node_list)


if __name__ == "__main__":
    my_bst = create_balanced_bst()
    print("BFS iterative:", breadth_first_search(my_bst))
    print("BFS recursive:", breadth_first_search_recursive([my_bst.root], []))
