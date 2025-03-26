# Create hello world GUI window
import tkinter as tk
# Create the main window
root = tk.Tk()
root.title("My first GUI window")
# Create label
label = tk.Label(
    root,
    text = "Hello, MGS3001 W02"
)
# Lay out label
label.pack()
# Run the window forever
root.mainloop()
