import data
import lab6
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 0
    def test_index_smallest_from_1(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 3
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_2(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = 4
        actual = lab6.index_smallest_from(input, 4)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_3(self):
        input = [2, 1, 9, 0, 4, 5]
        expected = None
        actual = lab6.index_smallest_from(input, 6)
        self.assertEqual(expected, actual)


    def test_index_smallest_from_4(self):
        input = []
        expected = None
        actual = lab6.index_smallest_from(input, 0)
        self.assertEqual(expected, actual)


    def test_selection_sort_1(self):
        input = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_2(self):
        input = []
        expected = []
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_3(self):
        input = [9, 7, 5, 3, 1]
        expected = [1, 3, 5, 7, 9]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    def test_selection_sort_4(self):
        input = [5, 0, 19, 21, 4, 6]
        expected = [0, 4, 5, 6, 19, 21]
        lab6.selection_sort(input)
        self.assertEqual(expected, input)


    # Part 1
    def test_selection_sort_books1(self):
        book_lists = [data.Book(['David'], 'alpha'), data.Book(['Daniel'], 'charlie'),
                      data.Book(['demitrious'], 'beta')]
        expected = [data.Book(['David'], 'alpha'), data.Book(['demitrious'], 'beta'), data.Book(['Daniel'], 'charlie')]
        result = lab6.selection_sort_books(book_lists)
        self.assertEqual(result, expected)

    def test_selection_sort_books2(self):
        book_lists = []
        expected = None
        result = lab6.selection_sort_books(book_lists)
        self.assertEqual(result, expected)

    # Part 2
    def test_swap_case1(self):
        string = 'StRiNG123#$'
        expected = 'sTrIng123#$'
        result = lab6.swap_case(string)
        self.assertEqual(result, expected)

    def test_swap_case2(self):
        string = 'AlpHaBeT1C0L_0Rd3r'
        expected = 'aLPhAbEt1c0l_0rD3R'
        result = lab6.swap_case(string)
        self.assertEqual(result, expected)

    # Part 3
    def test_str_translate1(self):
        string = 'Pythagoras'
        old = 'a'
        new = 'G'
        expected = 'PythGgorGs'
        result = lab6.str_translate(string, old, new)
        self.assertEqual(result, expected)

    def test_str_translate2(self):
        string = 'Pepperonis'
        old = 'e'
        new = 'h'
        expected = 'Phpphronis'
        result = lab6.str_translate(string, old, new)
        self.assertEqual(result, expected)

    # Part 4
    def test_histogram1(self):
        paragraph = 'We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America.'
        expected = {'We': 1, 'the': 6, 'People': 1, 'of': 3, 'United': 2, 'States,': 1, 'in': 1, 'Order': 1, 'to': 2, 'form': 1, 'a': 1, 'more': 1, 'perfect': 1, 'Union,': 1, 'establish': 2, 'Justice,': 1, 'insure': 1, 'domestic': 1, 'Tranquility,': 1, 'provide': 1, 'for': 2, 'common': 1, 'defence,': 1, 'promote': 1, 'general': 1, 'Welfare,': 1, 'and': 3, 'secure': 1, 'Blessings': 1, 'Liberty': 1, 'ourselves': 1, 'our': 1, 'Posterity,': 1, 'do': 1, 'ordain': 1, 'this': 1, 'Constitution': 1, 'States': 1, 'America.': 1}
        result = lab6.histogram(paragraph)
        self.assertEqual(result, expected)

    def test_histogram2(self):
        paragraph = "The people who are crazy enough to think they can change the world are the ones who do"
        expected = {'The': 1, 'people': 1, 'who': 2, 'are': 2, 'crazy': 1, 'enough': 1, 'to': 1, 'think': 1, 'they': 1, 'can': 1, 'change': 1, 'the': 2, 'world': 1, 'ones': 1, 'do': 1}
        result = lab6.histogram(paragraph)
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
