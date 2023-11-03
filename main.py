"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
        return x + 1
    

def longest_run(mylist, key):
    ### TODO
    
    longest_size = 0
    left_size = 0
    right_size = 0
    is_entire_range = False
    current_size = 0

    for item in mylist:
        if item == key:
            current_size += 1
            if current_size > longest_size:
                longest_size = current_size
        else:
            current_size = 0

    if longest_size == len(mylist):
        is_entire_range = True

    return Result(left_size, right_size, longest_size, is_entire_range)


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    if start == end:
            return Result(0, 0, 0, False)

        mid = (start + end) // 2

        left_result = find_longest_run(start, mid)
        right_result = find_longest_run(mid + 1, end)

        left_size = left_result.left_size
        right_size = right_result.right_size

        if mylist[mid] == key:
            left_size += 1
            right_size += 1
        else:
            left_size = 0
            right_size = 0

        longest_size = max(left_size, right_size, left_result.longest_size, right_result.longest_size)
        is_entire_range = (left_size + right_size == end - start + 1)

        return Result(left_size, right_size, longest_size, is_entire_range)


## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


