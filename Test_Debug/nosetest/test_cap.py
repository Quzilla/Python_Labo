# nosetests test_cap.py

import cap
from nose.tools import eq_

def test_one_word():
    text = 'duck'
    result = cap.just_do_it3(text)
    eq_(result, 'Duck')
    
def test_multiple_words():
    text = 'a veritable flock of ducks'
    resutl = cap.just_do_it3(text)
    eq_(resutl, 'A Veritable Flock Of Ducks')
    
def test_words_with_apostrophes():
    text = "I'm fresh out of ideas"
    result = cap.just_do_it3(text)
    eq_(result, "I'm Fresh Out Of Ideas")
    
def test_words_with_quotes():
    text = "\"You're despicable,\" said Daffy Duck"
    result = cap.just_do_it3(text)
    eq_(result, "\"You're Despicalbe,\" Said Daffy Duck")
    