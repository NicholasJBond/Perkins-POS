
lineInput = "0"
x1 = lineInput
keybind = "<Return>"
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()


entry1 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)

def getSquareRoot (self):  
    x1 = entry1.get()
    print(x1)
    lineInput = x1
    keybind = lineInput
    label1 = tk.Label(root, text=lineInput)
    canvas1.create_window(200, 230, window=label1)

    


root.bind(keybind,getSquareRoot)
entry1.delete(0)




root.mainloop()