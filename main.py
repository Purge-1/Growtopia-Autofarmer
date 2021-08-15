from tkinter import *
from tkinter import ttk, messagebox
import pyautogui
import time

window=Tk()
window.geometry("125x125")
window.title('Window')

def pos1():
    global pos1
    time.sleep(1)
    pos1 = pyautogui.position()
    messagebox.showinfo("POS 1", f"{pyautogui.position()}")

def pos2():
    global pos2
    time.sleep(1)
    pos2 = pyautogui.position()
    messagebox.showinfo("POS 2", f"{pyautogui.position()}")

def block():
    global block
    time.sleep(1)
    block = pyautogui.position()
    messagebox.showinfo("Block Pos", f"{pyautogui.position()}")

def fist():
    global fist
    time.sleep(1)
    fist = pyautogui.position()
    messagebox.showinfo("Fist Pos", f"{pyautogui.position()}")

def start():
    global block
    global fist
    global pos1
    global pos2

    if block == None:
        messagebox.showinfo("Error", f"Block not set")
    elif fist == None:
        messagebox.showinfo("Error", f"Fist not set")
    elif pos1 == None:
        messagebox.showinfo("Error", f"POS 1 not set")
    elif pos2 == None:
        messagebox.showinfo("Error", f"POS 2 not set")

    else:
        while True:
            #Select Block
            pyautogui.click(block)
            #Place POS 1
            pyautogui.click(pos1)
            #Place POS 2
            pyautogui.click(pos2)
            #Select Fist
            pyautogui.click(fist)
            #Break POS 1
            pyautogui.click(pos1, clicks=3)
            #Break POS 2
            pyautogui.click(pos2, clicks=3)

#Buttons
ttk.Button(text="POS 1", command=pos1).pack()        
ttk.Button(text="POS 2", command=pos2).pack()
ttk.Button(text="Block Pos", command=block).pack()
ttk.Button(text="Fist Pos", command=fist).pack()
ttk.Button(text="Start", command=start).pack()

window.mainloop()