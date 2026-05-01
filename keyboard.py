import traceback
import baybayin as by
from collections import deque
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

KP: str = ""
"Global variable storing the last alphanumeric keyboard input"
ALPH_UPDATE: bool = False
"Used so listener thread can communicate with main thread when an alphanumeric key is pressed"

def on_press(key: KeyCode | Key) -> bool:
    global ALPH_UPDATE
    global KP
    try:
        if key == Key.esc:
            print("No longer listening to keyboard")
            return False

        if isinstance(key, KeyCode): # If last key pressed is an alphanumeric character:
            char = key.char.lower() # To make everything case insensitive
            if char == 'o': char = 'u'
            if char == 'e': char = 'i'
            KP = char
            ALPH_UPDATE = True

    except:
        print(traceback.format_exc())
        print(f"{key} of type {type(key)} was last pressed\n")

def main():

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    controller = keyboard.Controller()

    global ALPH_UPDATE
    global KP

    key2: deque[str] = deque((None, None), maxlen=2) # Initially filled with None so all elems are always accesible
    while listener.running:
        if not ALPH_UPDATE:
            continue

        # Before doing anything, delete the english character that was pressed
        controller.tap(Key.backspace)

        kp = KP # making a local version to use cause thats probably better or smthn
        key2.append(kp)

        print(f"kp: {kp}")
        print(f"last 2 keys: {key2}")

        last_key = key2[0]
        # Definitely a better way to do this
        if (last_key in by.vowels_eng or (last_key is None)) and (kp in by.vowels_eng):
            controller.tap(by.baycons_dict[kp])
        elif last_key in by.baycons_eng and kp == 'a':
            controller.tap(Key.backspace) # delete the vowel terminator that we assume is there
        elif last_key in by.baycons_eng and kp in ('i', 'e'):
            controller.tap(Key.backspace)
            controller.tap(by.baymod_dict['i'])
        elif last_key in by.baycons_eng and kp in ('o', 'u'):
            controller.tap(Key.backspace)
            controller.tap(by.baymod_dict['u'])
        elif (kp in by.baycons_eng) and (kp not in by.vowels_eng):
            controller.tap(by.baycons_dict[kp])
            controller.tap(by.baymod_dict["vowel_terminator"])

        ALPH_UPDATE = False # Resetting update to wait for listener to make it true again

main()