def just_do_it(text: str):
    "<text>に含まれるすべての単語をタイトルケースに"
    return text.capitalize()

def just_do_it2(text: str):
    "Capitalize all words in <text>"
    return text.title()

def just_do_it3(text: str):
    "Capitalize all words in <text>"
    from string import capwords
    return capwords(text)
