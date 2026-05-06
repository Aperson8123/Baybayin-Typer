import unicodedata as un

def filter_unicode(l: list[chr]) -> list:
    return [char for char in l if un.category(char) not in ('Cc', 'Cn', 'Co')] 

vowels_eng = ("a", "e", "i", "o", "u")

# Where the baybayin characters start and end in unicode
baychar_start: int = int("1700", 16)
baychar_end: int = int("1712", 16)

# Where the baybayin modifiers start and end in unicode
baymod_start: int = int("1712", 16)
baymod_end: int = int("1716", 16) 

#Used so apps that use graphme clustering dont combine characters with modifiers as one character 
zero_width_space_code: int = int("200B", 16)
zero_width_space: str = chr(zero_width_space_code)

baychar_uni: list[int] = list(range(baychar_start, baychar_end))
"List of all baybayin consonant characters in decimal unicode in ascending order"
baychar: list[chr] = [chr(x) for x in baychar_uni]
"List of all baybayin consonant characters in ascending order of their unicode number"
baychar_eng: list[str] = ["a", "i", "u", "k", "g", "ng", "t", "d", "n", "p", "b", "m", "y", "r", "l", "w", "s", "h"]
"What baychar list corresponds to in english characters in order"
baychar_dict: dict[str, str] = {k:v for (k,v) in zip(baychar_eng, baychar)}
"Using english characters, access the corresponding character in baybayin"

baymod_int: list[int] = list(range(baymod_start, baymod_end))
"List of all baybayin characters modifiers in decimal unicode in ascending order"
baymod: list[chr] = [chr(x) for x in baymod_int] 
"List of all baybayin character modifiers in ascending order of their unicode number"
baymod_eng: list[str] = ["i", "u", "vowel_terminator"]
"What baymod list corresponds to in english characters in order"
baymod_dict: dict[str, str] = {k:v for (k,v) in zip(baymod_eng, baymod)}
"Using english characters, access the corresponding modifier in baybayin"