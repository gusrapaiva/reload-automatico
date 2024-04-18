from pyautogui import click
import threading;

def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
        func()

def clicker():
    click(85, 65)

setInterval(clicker, 5)