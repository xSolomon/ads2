''' Lesson 5 solution. '''

from bisect import bisect_left

def binary_search(values : list[int], search_value : int) -> int:
    ''' Returns position of element if it's present, else "None". '''
    index : int = bisect_left(values, search_value)
    return index if index != len(values) and values[index] == search_value else -1

def FormBBSTArray(input_array : list[int], left_border : int, right_border : int,
    result_array_index, result_array : list[int]) -> list[int]:
    ''' From ascending sorted array forms BBST array. '''
    if right_border < left_border:
        return result_array
    middle_element_index : int = (left_border + right_border) // 2
    result_array[result_array_index] = input_array[middle_element_index]
    result_array_index *= 2
    FormBBSTArray(input_array, left_border, middle_element_index - 1,
        result_array_index + 1, result_array)
    FormBBSTArray(input_array, middle_element_index + 1, right_border,
        result_array_index + 2, result_array)
    return result_array

def GenerateBBSTArray(a : list[int]) -> list[int]:
    ''' Recursively generates BBST array from input array. '''
    a.sort()
    return FormBBSTArray(a, 0, len(a) - 1, 0, [None] * len(a))

def find_node_by_key(BBSTArray : list[int], key : int) -> int | None:
    ''' Returns index of node with key or None if no such node. '''
    current_index : int = 0
    while current_index < len(BBSTArray):
        if BBSTArray[current_index] is None:
            break
        if BBSTArray[current_index] == key:
            return current_index
        current_index = current_index * 2 + (1 if BBSTArray[current_index] > key else 2)
    return None

def nodes_except_one_inorder(BBSTArray : list[int], current_node_index : int, exclude_key : int) -> list[int]:
    ''' Returns all tree nodes excluding one key.
        Uses inorder traversal. '''
    result : list[int] = []
    if current_node_index >= len(BBSTArray):
        return result
    if BBSTArray[current_node_index] is None:
        return result
    result.extend(nodes_except_one_inorder(
        BBSTArray, current_node_index * 2 + 1, exclude_key)) # left subtree
    if BBSTArray[current_node_index] != exclude_key:
        result.append(BBSTArray[current_node_index])
    result.extend(nodes_except_one_inorder(
        BBSTArray, current_node_index * 2 + 2, exclude_key)) # right subtree
    return result


def delete_node_by_key(BBSTArray : list[int], key : int) -> list[int]:
    ''' Deletes node by key via excluding it from inorder traversal and then reforming BBST. '''
    nodes_without_key_inorder : list[int] = nodes_except_one_inorder(BBSTArray, 0, key)
    return FormBBSTArray(nodes_without_key_inorder, 0, len(nodes_without_key_inorder) - 1,
        0, [None] * len(BBSTArray))





