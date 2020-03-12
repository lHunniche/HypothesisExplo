import hypothesis.strategies as st
from hypothesis import given, example

'''def mean(xs):
    sum = 0
    for x in xs:
        sum += x
    return sum/len(xs)

@given(st.lists(st.floats(allow_nan=False, allow_infinity=False), min_size=1))
def test_mean(xs):
    assert min(xs) >= mean(xs) >= max(xs)

'''
def encode(input_string):
    if not input_string:
        return []
    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            #count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q

def my_reverse(some_list):
    if len(some_list) == 0 or len(some_list) == 1:
        return some_list
    reversed_list = []
    for index in range(len(some_list)-1, -1, -1):
        reversed_list.append(some_list[index])
    return reversed_list



@given(st.text())
@example("")
def test_decode_inverts_encode(s):
    assert decode(encode(s)) == s

@given(st.lists(st.integers(), min_size=1))
def test_builtin_reverse_function(some_list):
    #assert some_list.reverse() == my_reverse(some_list)

    placeholder1 = some_list.copy()
    placeholder2 = some_list.copy()
    placeholder1.reverse()
    placeholder2.reverse()
    assert placeholder1 == placeholder2

    placeholder3 = some_list.copy()
    placeholder3.reverse()
    placeholder3.reverse()
    assert placeholder3 == some_list

@given(st.lists(st.integers(), min_size=1), st.lists(st.integers(), min_size=1))
def test_builtin_reverse_function_again(list1, list2):
    # joins both lists and reverses the result
    # e.g. [1,2] and [3,4] becomes [1,2,3,4], and reversed to [4,3,2,1]
    placeholder1 = list1.copy() + list2.copy()
    placeholder1.reverse()

    # reverses each list and glues the first one to the back of the second one
    # [1,2] becomes [2,1], and [3,4] becomes [4,3]
    # this becomes [4,3] + [2,1] = [4,3,2,1]
    placeholder2 = list1.copy()
    placeholder3 = list2.copy()
    placeholder2.reverse()
    placeholder3.reverse()
    placeholder4 = placeholder3 + placeholder2


    assert placeholder4 == placeholder1




#test_decode_inverts_encode()
test_builtin_reverse_function()
test_builtin_reverse_function_again()


#test_list = [0,1]
