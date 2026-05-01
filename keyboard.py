import traceback
import baybayin as by
from collections import deque
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

KP: str = ""
"Global variable storing the last alphanumeric keyboard input"
UPDATE: bool = False
"Used so listener thread can communicate with main thread when a key is pressed"

def on_press(key: KeyCode | Key):
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
            #print(KP3)

    except:
        print(traceback.format_exc())
        print(f"{key} of type {type(key)} was last pressed\n")

def main():

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    controller = keyboard.Controller()

    global UPDATE
    global KP

    key3: deque[str] = deque(maxlen=3)

    while listener.running:
        if not UPDATE: # Do nothing if theres no update from listener
            continue

        kp = KP # making a local version to use cause thats probably better or smthn
        key3.append(kp)
        print(f"update: new kp {kp}")
        print(f"last 3 keys: {key3}")

        if kp == 'b':
            controller.tap(Key.backspace)
            controller.tap(by.baychar_dict[kp])

        UPDATE = False # Resetting update to wait for listener to make it true again

main()

# with keyboard.Events() as events:

#         controller = keyboard.Controller()

#         for event in events:
#             if event.key == keyboard.Key.esc:
#                 print("No longer reading events")
#                 break
#             if isinstance(event, keyboard.Events.Press):
#                 if isinstance(event.key, keyboard.KeyCode): # If last key pressed is an alphanumeric character:
#                     kp3.append(event.key.char) # Storing last 3 keyboard presses alphanumeric characters
#                     print(kp3)