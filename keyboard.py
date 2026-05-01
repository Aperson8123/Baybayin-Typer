import traceback
import baybayin as by
from collections import deque
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

KP: str = ""
"Global variable storing the last alphanumeric keyboard input"
UPDATE: bool = False
"Used so listener thread can communicate with main thread when an alphanumeric key is pressed"

def on_press(key: KeyCode | Key) -> bool:
    global UPDATE
    global KP
    try:
        if key == Key.esc:
            print("No longer listening to keyboard")
            return False

        if isinstance(key, KeyCode): # If last key pressed is an alphanumeric character:
            char = key.char.lower() # To make everything case insensitive
            KP = char
            UPDATE = True

    except:
        print(traceback.format_exc())
        print(f"{key} of type {type(key)} was last pressed\n")

def main():

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    controller = keyboard.Controller()

    global UPDATE
    global KP

    key3: deque[str] = deque((None, None, None), maxlen=3) # Initially filled with None so all elems are always accesible

    while listener.running:
        if not UPDATE: # Do nothing if theres no update from listener. Updates only occur when an alphanumeric key is pressed
            continue

        kp = KP # making a local version to use cause thats probably better or smthn
        key3.append(kp)

        print(f"update: new kp {kp}")
        print(f"last 3 keys: {key3}")

        
        if kp in by.baycons_eng:
            controller.tap(Key.backspace)
            controller.tap(by.baycons_dict[kp])
            controller.tap(by.baymod_dict["vowel_terminator"])
        # controller.type(by.baycons_dict[kp])

        UPDATE = False # Resetting update to wait for listener to make it true again

main()