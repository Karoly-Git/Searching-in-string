import time
import os

a = "tetszőleges szöveg, amiben keresünk egy szövegrészt és tudni akarjuk a keresett szövegrész helyét a szövegben"
b = "szöveg"

for i in range(len(a)):
    if a[i:i+len(b)] == b:
        if len(b) == 1:
            print("character", i+1)
        else:
            print("from character", i+1, "to", i+len(b))
