import unittest
import cap

class TestCap(unittest.TestCase):
    
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        pass
    
    def test_one_word(self):
        text = 'duck'
        result = cap.just_do_it(text=text)
        self.assertEqual(result, 'Duck')
        
    # false
    # def test_multiple_words(self):
    #     text = 'a veritable flock of ducks'
    #     result = cap.just_do_it(text=text)
    #     self.assertEqual(result, 'A Veritalbe Flock Of Ducks')
        
    def test_multiple_words_2(self):
        text = 'a veritable flock of ducks'
        result = cap.just_do_it2(text=text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')
        
    def test_words_with_apstorophes(self):
        text = "I'm  fresh out of ideas"
        result = cap.just_do_it3(text=text)
        self.assertEqual(result, "I'm Fresh Out Of Ideas")
        
    def text_words_with_quotes(self):
        text = "\"You're despicable,\" said Daffy Duck"
        result = cap.just_do_it3(text)
        self.assertEqual(result, "\"You're Despicable,\" Said Daffy Duck")
        
if __name__ == '__main__':
    unittest.main()