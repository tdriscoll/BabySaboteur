import unittest
from utility.string_utility import make_pretty


class StringUtilityTest(unittest.TestCase):


    def test_empty_string_made_pretty_is_empty_string(self):
        self.assertEqual('', make_pretty('', 5))
        
    def test_one_word_smaller_than_width(self):
        self.assertEqual('bob', make_pretty('bob', 5))
    
    def test_strip_trailing_spaces(self):
        self.assertEqual('bob', make_pretty('bob ', 5))
    
    def test_split_two_words(self):
        self.assertEqual('bob\nsue', make_pretty('bob sue ', 5))
        
    def test_do_not_split_word_small_than_width(self):
        self.assertEqual('bob sue', make_pretty('bob sue ', 10))
        
    def test_remove_extra_spaces_in_word(self):
        self.assertEqual('bob sue', make_pretty('bob  sue ', 10))
        
    def test_split_three_words(self):
        self.assertEqual('bob\nsue\ntim', make_pretty('bob sue tim ', 5))
        
    
    def test_some_words_but_not_all(self):
        self.assertEqual('a b c\nd e', make_pretty('a b c d e ', 5))
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()