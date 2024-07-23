import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def dct(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yesno=input("Did you mean %s ? Enter y if Yes or n if No\n" %get_close_matches(w,data.keys())[0])
        if yesno == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yesno =="n":
            return "Sorry the word doesn't exist"
        else:
            return "wrong input"
    else:
        return "Word not found in dictionary, please check the word"
word=input("Enter a word : ")
output = (dct(word.lower()))
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
print("Code Executed")