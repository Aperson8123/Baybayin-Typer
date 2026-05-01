import traceback
from collections import deque
from pynput import keyboard

KP: str = ""
"Global variable storing the last alphanumeric keyboard input"
UPDATE: bool = False
"Used so listener thread can communicate with main thread when a key is pressed"

def on_press(key: keyboard.KeyCode | keyboard.Key):
    global UPDATE
    global KP
    try:
        if key == keyboard.Key.esc:
            print("No longer reading events")
            return False

        if isinstance(key, keyboard.KeyCode): # If last key pressed is an alphanumeric character:
            char = key.char.lower() # To make everything case insensitive
            KP = char
            UPDATE = True
            #print(KP3)

    except Exception:
        print(traceback.format_exc())
        print(f"{key} of type {type(key)} was last pressed\n")

def main():

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    global UPDATE
    global KP

    key3: deque[str] = deque(maxlen=3)

    while listener.running:
        if UPDATE:
            key3.append(KP)
            print("updated")
            print(f"last 3 keys: {key3}")
        UPDATE = False

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