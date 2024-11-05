import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def selection_sort_books(book_list : list[data.Book]):
    final_book_list = []
    book_dictionary = {}
    if len(book_list) == 0:
        return None
    for book in book_list:
        book_dictionary[book.title] = book
    sorted_list = sorted(book_dictionary)
    for item in sorted_list:
        for book in book_list:
            if item == book.title:
                final_book_list.append(book)
            else:
                continue
    return final_book_list


def swap_case(string : str) -> str:
    new_string_list = []
    string_list = list(string)
    for item in string_list:
        if ord(item) < 65 and ord(item) > 90 and ord(item) < 97 and ord(item) > 122:
            continue
        if item.islower() == True:
            item = item.upper()
            new_string_list.append(item)
        else:
            item = item.lower()
            new_string_list.append(item)
    new_string = "".join(new_string_list)
    return new_string
strings = '#sigMA1'
print(swap_case(strings))

def str_translate(string : str, old : str, new : str):
    new_string_list = []
    string_list = list(string)
    for item in string_list:
        if item == old:
            new_string_list.append(new)
        else:
            new_string_list.append(item)
    new_string = "".join(new_string_list)
    return new_string
print(str_translate('sigmas', 's', 'o'))

def histogram(paragraph : str):
    paragraph_list = paragraph.split()
    word_dictionary = {}
    for i in paragraph_list:
        if i not in word_dictionary:
            word_dictionary[i] = 1
        else:
            word_dictionary[i] += 1
    return word_dictionary



str = "The people who are crazy enough to think they can change the world are the ones who do"
print(histogram(str))




# Part 2


# Part 3


# Part 4
