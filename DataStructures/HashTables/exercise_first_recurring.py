def first_recurring_item(lst: list):
    # Check for input
    if not isinstance(lst, list):
        raise RuntimeError("Wrong input!")
    # The code itself
    values = {}
    for item in lst:
        if values.get(item) is not None:
            return item
        values[item] = True
    return None


if __name__ == "__main__":
    # Testing - casual cases
    print(first_recurring_item([2,5,1,2,3,5,1,2,4]))
    print(first_recurring_item([2,1,1,2,3,5,1,2,4]))
    print(first_recurring_item([2, 3, 4, 5]))
    # Testing - extreme cases
    print(first_recurring_item([]))
    bad_parameters = [{}, None, False, True, "abc", 32]
    for parameter in bad_parameters:
        try:
            print(first_recurring_item(parameter))
        except RuntimeError:
            print(f"Test for {parameter} passed")
