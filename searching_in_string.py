
text = "this is a text, type in whatever you wish, we'll find a given string in this, the variable of given string is named 'given'"
given = "given"

for i in range(len(text)):
    if text[i:i+len(given)] == given:
        if len(given) == 1:
            print("character", i+1)
        else:
            print("from character", i+1, "to", i+len(given))
