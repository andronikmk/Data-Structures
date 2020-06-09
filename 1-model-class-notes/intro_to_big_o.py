count = 0
def my_print_counter(thing_to_print):
    global count
    count += 1
    print(thing_to_print)

my_items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


"""
O(1) - Constant Time
"""
def print_first_time(item):
    my_print_counter(item[0])

print_first_time(my_items)


"""
O(n) - Linear Time
"""
def print_all_items(items):
    for item in items:
        my_print_counter(item)

print_all_items(my_items)


"""
O(n^2) - Quadratic Time
"""
def print_all_possible_ordered__pairs(items):
    for first_item in items:
        for second_item in items:
            my_print_counter((first_item, second_item))

print_all_possible_ordered__pairs(my_items)


"""
N could be the actual input, or the size of the input
"""
def say_hi_n_times(n):
    for time in range(n):
        my_print_counter("hi")
    
say_hi_n_times(10)

"""
Drop the constants
"""
# O(2n) is simplified to what?
def print_all_items_twice(items):
    for item in items:
        my_print_counter(item)

    # Once more, with feeling
    for item in items:
        my_print_counter(item)

print_all_items_twice(my_items)

def print_first_item_then_first_half_then_say_hi_100_times(items):
    my_print_counter(items[0]) # O(1)

    middle_index = len(items) / 2
    index = 0
    while index < middle_index: # O(n/2)
        my_print_counter(items[index])
        index += 1
    
    for time in range(100):
        my_print_counter("hi")

print_first_item_then_first_half_then_say_hi_100_times(my_items)


"""
Drop the less significant terms
"""

# def print_all_numbers_then_all_pair_sums(number):
#     print("these are the numbers")
#     for number in numbers: # O(n)
#         my_print_counter(number)

#     print()


my_haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def contains(haystack, needle):

    for item in haystack:
        if item == needle:
            return True
    return False

contains(my_haystack, 10)

# https://www.desmos.com/calculator