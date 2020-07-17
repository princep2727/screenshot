import time
import pyautogui
import tkinter as tk

def ss():
    name = int(round(time.time() * 1000))
    name = "C:/Users/princ/PycharmProjects/amazing projects/screenshots/ss_files/{}.png".format(name)
    #time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text="Take ScreenShot",
    command = ss)
button.pack(side=tk.LEFT)
close = tk.Button(
    frame,
    text="Quit",
    command = quit)
close.pack(side=tk.LEFT)

root.mainloop()

