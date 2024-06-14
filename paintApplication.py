import tkinter as tk
from tkinter import ttk


# Create a window
root = tk.Tk()

root.geometry("1000x1000")  # Width x height of the window
root.resizable(False, False)  # Width, height of the window can't be changed
root.configure(bg="#D3D3D3")  # Background color of the window
root.title("Paint Application")

color_pick_value = tk.StringVar(value="black")  # Default color
size_pick_value = tk.IntVar(value=5)  # Default size

#Crate widgets
#crate label for the topic
topic_label = ttk.Label(root, text="Paint Application", font=("Helvetica", 50, "bold"), foreground="blue",background="#D3D3D3")
topic_label.pack(side=tk.TOP,pady=10)  

#create label for the color select
color_label = ttk.Label(root, text="Choose color:", font=(12),background="#D3D3D3")
color_label.pack()

#crate combobox for the color select
color_pick = ttk.Combobox(root, values=["red", "blue", "green", "yellow", "black"], font=(12),background="#D3D3D3")
color_pick.pack(pady=10)

#create label for the size select
size_label = ttk.Label(root, text="Choose size:", font=(12),background="#D3D3D3",foreground="black")
size_label.pack()

#crate entry for the size select
size_enter = ttk.Entry(root, font=(12), width=10,background="#D3D3D3")
size_enter.pack(pady=10)

#create frames for the button
button_frame = tk.Frame(root, bg="#D3D3D3")
button_frame.pack(pady=10)

def update_size_and_color():
    size_pick_value.set(int(size_enter.get()))
    color_pick_value.set(color_pick.get())

style = ttk.Style()
style.configure('Custom.TButton', background='#D3D3D3')

#crate button for the size select
enter_button = ttk.Button(button_frame, text="Enter", command=update_size_and_color,style='Custom.TButton')
enter_button.pack(side=tk.LEFT,padx=10)

#crate button for the clear
def clear():
    canvas.delete("all")

#crate button for the clear
clear_button = ttk.Button(button_frame, text="Clear", command=clear,style='Custom.TButton')
clear_button.pack(side=tk.RIGHT,padx=10)

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
