import json
from difflib import get_close_matches
data=json.load(open("data.json"))

def translate(w):
    w=w.lower()
    if w  in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn=input("Did you mean %s instead? enter Y if yes, or N if no? " % get_close_matches(w,data.keys())[0])
        if yn.lower()=="y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn.lower()=="n":
            return "the word doesn't exit. Please double check it"
        else:
            return "we didn't understand your entry"
    else:
        return "the word doesn't exit. Please double check it"

word=input("Enter word: ")
output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)