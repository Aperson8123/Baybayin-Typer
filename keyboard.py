import traceback
from collections import deque # TODO Use this when storing the keyboard inputs
from pynput import keyboard

KP3: deque[str] = deque(maxlen=3)
"Global variable storing last 3 alphanumeric keyboard inputs as a que"

def on_press(key: keyboard.KeyCode | keyboard.Key):
    try:
        if key == keyboard.Key.esc:
            print("No longer reading events")
            return False

        if isinstance(key, keyboard.KeyCode): # If last key pressed is an alphanumeric character:
            char = key.char.lower() # To make everything case insensitive
            KP3.append(char)
            print(KP3)

    except Exception:
        print(traceback.format_exc())
        print(f"{key} of type {type(key)} was last pressed\n")

def main():

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

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