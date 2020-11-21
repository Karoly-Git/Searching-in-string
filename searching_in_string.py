#  with this code I'd like to show (especially to beginners) how easy to search in a string
#  what this code does: will find string named 'given' in string named 'text' then shows it's location
#  of course you can change any of them and apply on any strings
#  figure out what line-11 and line-12 are used for

text = "this is a text, type in whatever you wish, then you can find a given string in this, the variable of given string is below named 'given'"
given = "given"

for i in range(len(text)):
    if text[i:i+len(given)] == given:
        if len(given) == 1:
            print("character", i+1)
        else:
            print("from character", i+1, "to", i+len(given))
