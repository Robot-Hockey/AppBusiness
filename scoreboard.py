# apt install python3-tk
from tkinter import *
 
window = Tk()
 
window.title("AppBusiness")
window.attributes("-fullscreen", True)
 
lbl_player = Label(window, text="Player", font=("Helvetica", 64)) 
lbl_player.grid(column=0, row=0, padx= 200, pady=10, sticky="e")

lbl_point_player = Label(window, text="0",font=("Helvetica", 128))
lbl_point_player.grid(column=0, row=1, padx= 320, pady=10, sticky="ne")

lbl_robot = Label(window, text="Robot", font=("Helvetica", 64))
lbl_robot.grid(column=1, row=0, padx= 200, pady=10, sticky="w")

lbl_point_robot = Label(window, text="0", font=("Helvetica", 128))
lbl_point_robot.grid(column=1, row=1, padx= 320, pady=10, sticky="nw")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)

window.mainloop()