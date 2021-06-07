from DataStructures.Implementation.bst import create_balanced_bst


def is_valid_bst(root):
    return validate_bst(root, None, None)


def validate_bst(root_node, max_val, min_val):
    if root_node is None:
        return True
    if max_val and root_node.value >= max_val or min_val and root_node.value <= min_val:
        return False
    return validate_bst(root_node.left, root_node.value, min_val) and validate_bst(root_node.right, max_val, root_node.value)


if __name__ == "__main__":
    my_bst = create_balanced_bst()
    print(is_valid_bst(my_bst.root))
