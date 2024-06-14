import tkinter as tk
from tkinter import ttk


# Create a window
root = tk.Tk()

root.geometry("1000x1000")  # Width x height of the window
root.resizable(False, False)  # Width, height of the window can't be changed

root.title("Paint Application")

color_pick_value = tk.StringVar(value="black")  # Default color
size_pick_value = tk.IntVar(value=5)  # Default size

#Crate widgets
#crate label for the topic
topic_label = ttk.Label(root, text="Paint Application", font=("Helvetica", 50, "bold"), foreground="blue")
topic_label.pack(pady=10)  

#create label for the color select
color_label = ttk.Label(root, text="Choose color:", font=(12))
color_label.pack()

#crate combobox for the color select
color_pick = ttk.Combobox(root, values=["red", "blue", "green", "yellow", "black"], font=(12), textvariable=color_pick_value)
color_pick.pack(pady=10)

#create label for the size select
size_label = ttk.Label(root, text="Choose size:", font=(12))
size_label.pack()

#crate entry for the size select
size_enter = ttk.Entry(root, font=(12), width=10)
size_enter.pack(pady=10)

#create frames for the button
button_frame = ttk.Frame(root)
button_frame.pack()

def update_size():
    size_pick_value.set(int(size_enter.get()))

#crate button for the size select
enter_button = ttk.Button(button_frame, text="Enter", command=update_size)
enter_button.pack(side=tk.LEFT,padx=10)

#crate button for the clear
def clear():
    canvas.delete("all")

#crate button for the clear
clear_button = ttk.Button(button_frame, text="Clear", command=clear)
clear_button.pack(side=tk.LEFT,padx=10)

#crate canvas 
canvas = tk.Canvas(root, bg="white", height=500, width=900)
canvas.pack(pady=10)

# Function to draw on the canvas
def draw(event):
    x = event.x
    y = event.y
    size = size_pick_value.get()
    color = color_pick_value.get()
    canvas.create_oval(x - size/2, y - size/2, x + size/2, y + size/2, fill=color, outline=color)

# Bind the draw function to the canvas
canvas.bind("<B1-Motion>", draw)

root.mainloop()
