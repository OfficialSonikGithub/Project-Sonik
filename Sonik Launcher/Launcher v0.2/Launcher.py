import tkinter
from tkinter import *
from tracemalloc import start
from turtle import color
import time
from time import sleep

print("""
          .'''''.        ..||..'''''''...
         / ##### \       : ||            ''.
        | ## # ## |      :.||...''''''....  '.
        | #  #  # |        ||             ''''
        | ####### |     .  ||
         \ ##### /     /| < _>
          \ ### /     / |/ < _>
        ..''   ''... /  |  < _>
      .'            /   | /||
      '                 |/ ||
      |   |     '..     |  ||
      |   |     |  '...''  ||
      |  |       |         ||
       \ |       |         ||
       |\|       |         ||
       \|         |        ||
        |         |        ||
        |         |        ||
       |           |       ||
     __|           |__     ||
    /   '.........'   \    ||
     ''''''     ''''''     ##

     https://github.com/OfficialSonikGithub/Project-Sonik
""")

input("     [>>>] Push Enter To Start Launcher")
print("     [>>>] Sonik Launcher")

root = Tk()
root.title("SONIK LAUNCHER")
root.geometry("500x300")

Label1 = Label(root, text="Sonik Launcher")
Label1.pack()

def inject():
    print("     [>>>] Using Safe Injection Method...")
    sleep(2.5)
    print("     [>>>] Injected")

Button1 = Button(root, text="Inject", width=25, height=2, background="#cc2114", command=inject)
Button1.pack()

def kill():
    print("     [>>>] Game Killed")

Button2 = Button(root, text="Kill Game", width=25, height=2, background="#cc2114", command=kill)
Button2.pack()

def start():
    print("     [>>>] Game Started")

Button3 = Button(root, text="Start Game", width=25, height=2, background="#cc2114", command=start)
Button3.pack()

Label2 = Label(root, text="SONIK - The safest free mod menu")
Label2.pack()
































while True:
    input("")
