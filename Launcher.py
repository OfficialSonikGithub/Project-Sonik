import tkinter
from tkinter import *
from turtle import color
import time
from time import sleep

print("     [>>>] SONIK LAUNCHER")

root = Tk()
root.title("SONIK LAUNCHER")
root.geometry("500x300")

Label1 = Label(root, text="SONIK LAUNCHER")
Label1.pack()

def inject():
    print("     [>>>] Using Safe Injection Method...")
    sleep(3)
    print("     [>>>] Injected")

Button1 = Button(root, text="Inject", width=25, height=2, background="#2478ff", command=inject)
Button1.pack()

def kill():
    print("     [>>>] Game Killed")

Button2 = Button(root, text="Kill Game", width=25, height=2, background="#2478ff", command=kill)
Button2.pack()

Label2 = Label(root, text="SONIK - The safest free mod menu")
Label2.pack()
































while True:
    input("")

