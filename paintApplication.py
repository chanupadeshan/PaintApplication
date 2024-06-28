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

# Create widgets
# Create label for the topic
topic_label = ttk.Label(root, text="Paint Application", font=("Helvetica", 50, "bold"), foreground="blue", background="#D3D3D3")
topic_label.pack(side=tk.TOP, pady=10)

# Create label for the color select
color_label = ttk.Label(root, text="Choose color:", font=(12), background="#D3D3D3", foreground="#12205c")
color_label.pack()

# Create combobox for the color select
color_pick = ttk.Combobox(root, values=["red", "blue", "green", "yellow", "black"], font=(12), textvariable=color_pick_value)
color_pick.pack(pady=10)
color_pick.current(4)  # Set default selection to "black"

# Create label for the size select
size_label = ttk.Label(root, text="Choose size:", font=(12), background="#D3D3D3", foreground="#12205c")
size_label.pack()

# Create entry for the size select
size_enter = ttk.Entry(root, font=(12), width=10, textvariable=size_pick_value)
size_enter.pack(pady=10)

# Create frames for the button
button_frame = tk.Frame(root, bg="#D3D3D3")
button_frame.pack(pady=10)

def update_size_and_color():
    try:
        size = int(size_enter.get())
        size_pick_value.set(size)
        color_pick_value.set(color_pick.get())
    except ValueError:
        size_pick_value.set(5)  # Default size if invalid entry

style = ttk.Style()
style.configure('Custom.TButton', background='#D3D3D3', foreground='#12205c')

# Create button for the size select
enter_button = ttk.Button(button_frame, text="Enter", command=update_size_and_color, style='Custom.TButton')
enter_button.pack(side=tk.LEFT, padx=10)

# Create button for the clear
def clear():
    canvas.delete("all")

# Create button for the clear
clear_button = ttk.Button(button_frame, text="Clear", command=clear, style='Custom.TButton')
clear_button.pack(side=tk.RIGHT, padx=10)

# Create canvas 
canvas = tk.Canvas(root, bg="white", height=450, width=900)
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
