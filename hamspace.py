import keyboard
import pyautogui
import time
import threading
import pystray
from PIL import Image

running = False

def spam_spacebar():
    global running
    while running:
        pyautogui.press("space")
        time.sleep(0.05)

def toggle_spam(icon, item):
    global running
    running = not running
    if running:
        threading.Thread(target=spam_spacebar, daemon=True).start()

def exit_program(icon, item):
    icon.stop()

def load_icon():
    try:
        return Image.open("dist\ham.ico")
    except FileNotFoundError:
        print("Het icoonbestand werd niet gevonden!")
        raise


menu = (pystray.MenuItem("Start/Stop (F6)", toggle_spam), pystray.MenuItem("Exit", exit_program))
icon = pystray.Icon("hamspace", load_icon(), menu=menu)

keyboard.add_hotkey("F6", toggle_spam, args=(icon, None))

icon.run()
