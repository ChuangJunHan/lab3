import lab3

print("Test_lab3")

def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = lab3.bubble_sort(input_arr, lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = lab3.bubble_sort(input_arr, lab3.SORT_DESCENDING)

    assert (result == test_arr)


def test_bubble_sort_exceeding():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 2, 15, 82, 37]
    test_arr = 1

    result = lab3.bubble_sort(input_arr, lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_zero():
    result = []
    input_arr = []
    test_arr = 0

    result = lab3.bubble_sort(input_arr, lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_noninteger():
    result = []
    input_arr = [64, 34, 25, 12, 'a']
    test_arr = 2

    result = lab3.bubble_sort(input_arr, lab3.SORT_ASCENDING)

    assert (result == test_arr)
