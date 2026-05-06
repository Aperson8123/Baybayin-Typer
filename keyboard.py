import traceback
import baybayin as by
from collections import deque
from queue import Queue
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

def on_press(key: KeyCode | Key, last_kp: Queue) -> bool:
    try:
        if key == Key.esc:
            last_kp.put('STOP')
            print("No longer listening to keyboard")
            return False

        if key == Key.space:
            last_kp.put('space')

        if isinstance(key, KeyCode): 
            if (key.char in by.baychar_eng) or key.char in ('o', 'e'):
                char = key.char.lower() # To make everything case insensitive
                if char == 'o': char = 'u'
                if char == 'e': char = 'i'
                last_kp.put(char)

    except:
        print(traceback.format_exc())
        print(f"{key} of type {type(key)} was last pressed\n")

def main():

    last_kp: Queue[str] = Queue(1) # Used to communicate last kp with listener thread
    key2: deque[str] = deque((None, None), maxlen=2) # Initially filled with None so all elems are always accesible

    listener = keyboard.Listener(on_press = lambda key: on_press(key, last_kp))
    listener.start()

    controller = keyboard.Controller()

    while listener.running:
        kp = last_kp.get() # Will block the thread, waiting for an input
        if kp == "STOP": break
        if kp == "space":
            key2.append(None)
            continue
        key2.append(kp)
        last_key = key2[0]

        # print(f"kp: {kp}")
        # print(f"last 2 keys: {key2}")

        # Before doing anything, delete the english character that was pressed
        controller.tap(Key.backspace)

        # Definitely a better way to do this
        if last_key == 'n' and (kp == 'g'):
            for i in range(2): controller.tap(Key.backspace)
            controller.tap(by.baychar_dict['ng'])
            controller.tap(by.zero_width_space)
            controller.tap(by.baymod_dict['vowel_terminator'])
        elif (last_key in by.vowels_eng or (last_key is None)) and (kp in by.vowels_eng):
            controller.tap(by.baychar_dict[kp])
        elif last_key in by.baychar_eng and kp == 'a':
            controller.tap(Key.backspace)
        elif last_key in by.baychar_eng and kp == 'i':
            controller.tap(Key.backspace)
            controller.tap(by.baymod_dict['i'])
        elif last_key in by.baychar_eng and kp == 'u':
            controller.tap(Key.backspace)
            controller.tap(by.baymod_dict['u'])
        elif (kp in by.baychar_eng) and (kp not in by.vowels_eng):
            controller.tap(by.baychar_dict[kp])
            controller.tap(by.zero_width_space)
            controller.tap(by.baymod_dict["vowel_terminator"])

if __name__ == "__main__":
    main()