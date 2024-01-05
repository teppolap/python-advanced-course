from pynput import keyboard
import threading

keys=[]
lock_keys=threading.Lock()

def on_press(key):
    global keys
    try:
        with lock_keys:
            keys.append(key.char)
    except:
        pass
    
def init_mainloop():
    global listener
    listener=keyboard.Listener(on_press=on_press)
    listener.start()

def clean_mainloop():
    global listener
    listener.stop()
    #listener.join()

def get_key():
    with lock_keys:
        if len(keys)>0:
            return keys.pop(0)
        else:
            return ''
