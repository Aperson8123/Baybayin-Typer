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

baychar_uni: list[int] = list(range(baychar_start, baychar_end))
"List of all baybayin characters in decimal unicode in ascending order"
baychar: list[chr] = [chr(x) for x in baychar_uni]
"List of all baybayin characters in ascending order of their unicode number"
bayeng: list[str] = ["a", "i", "u", "ka", "ga", "nga", "ta", "da", "na", "pa", "b", "ma", "ya", "ra", "la", "wa", "sa", "ha"]
"What baychar list corresponds to in english characters in order"

baymod_int: list[int] = list(range(baymod_start, baymod_end))
baymod: list[chr] = [chr(x) for x in baymod_int] 
baymodeng: list[str] = ["i", "u", "vowel_terminator"]

baychar_dict: dict[str, str] = {}
for i, char in enumerate(bayeng): baychar_dict.update({char: baychar[i]})