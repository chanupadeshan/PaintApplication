import tkinter as tk
from tkinter import ttk


# Create a window
root = tk.Tk()

root.geometry("1000x1000")  # Width x height of the window
root.resizable(False, False)  # Width, height of the window can't be changed

root.title("Paint Application")

color_pick_value = tk.StringVar()

topic_label = ttk.Label(root, text="Paint Application", font=("Helvetica", 20, "bold"), foreground="blue")
topic_label.pack(pady=10)  

color_label = ttk.Label(root,text="Choose color:",font=(12))
color_label.pack()

color_pick = ttk.Combobox(root,values=["red","blue","green","yellow","black","white"],font=(12),textvariable=color_pick_value)
color_pick.pack()

size_label =ttk.Label(root,text="Choose size:",font=(12))
size_label.pack()

size_enter =ttk.Entry(root,font=(12),width=10,background="white")
size_enter.pack()

enter_button = ttk.Button(root,text="Enter")
enter_button.pack()

def clear():
    canvas.delete("all")


clear_button = ttk.Button(root,text="Clear",command=clear)
clear_button.pack()


canvas = tk.Canvas(root,bg="white",height=500,width=500)
canvas.pack()

def draw(event):
    x=event.x
    y=event.y
    canvas.create_oval(x,y,x,y,width=5,fill=color_pick_value.get())
canvas.bind("<Motion>", draw)



root.mainloop()