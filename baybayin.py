import unicodedata as un
import pynput as pyn
from collections import deque #TODO Use this when storing the keyboard inputs
from pynput import keyboard

#TODO q, p, f, j, z, x, v ykwtd 

def filter_unicode(l: list[chr]) -> list:
    return [char for char in l if un.category(char) not in ('Cc', 'Cn', 'Co')] 

# Where the baybayin characters start and end in unicode
baychar_start: int = int("1700", 16)
baychar_end: int = int("1712", 16)

# Where the baybayin modifiers start and end in unicode
baymod_start: int = int("1712", 16)
baymod_end: int = int("1716", 16) 

baycons_uni: list[int] = list(range(baychar_start, baychar_end))
"List of all baybayin consonant characters in decimal unicode in ascending order"
baycons: list[chr] = [chr(x) for x in baycons_uni]
"List of all baybayin consonant characters in ascending order of their unicode number"
baycons_eng: list[str] = ["a", "i", "u", "k", "g", "ng", "t", "d", "n", "p", "b", "m", "y", "r", "l", "w", "s", "h"]
"What baycons list corresponds to in english characters in order"

baymod_int: list[int] = list(range(baymod_start, baymod_end))
"List of all baybayin characters modifiers in decimal unicode in ascending order"
baymod: list[chr] = [chr(x) for x in baymod_int] 
"List of all baybayin character modifiers in ascending order of their unicode number"
baymod_eng: list[str] = ["i", "u", "vowel_terminator"]
"What baymod list corresponds to in english characters in order"

baycons_dict: dict[str, str] = {}
for i, char in enumerate(baycons_eng): baycons_dict.update({char: baycons[i]})

baymod_dict: dict[str, str] = {}
for i, char in enumerate(baymod_eng): baymod_dict.update({char: baymod[i]})