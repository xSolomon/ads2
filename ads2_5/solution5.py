''' Lesson 5 solution. '''

def FormBBSTArray(input_array : list, left_border : int, right_border : int,
    result_array_index, result_array : list) -> list:
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

def GenerateBBSTArray(a : list) -> list:
    ''' Recursively generates BBST array from input array. '''
    a.sort()
    return FormBBSTArray(a, 0, len(a) - 1, 0, [None] * len(a))







