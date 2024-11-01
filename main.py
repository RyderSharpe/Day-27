# Import the necessary modules from tkinter
from tkinter import *

# Create the main window
window = Tk()
window.title("My First GUI")  # Set the window title
window.minsize(width=500, height=300)  # Set the minimum window size
window.config(padx=100, pady=100)


# Create a label widget
my_label = Label(
    text="I am a label",  # Initial text
    font=("Arial", 24, "bold")  # Font style and size
)
my_label.config(text="New Text")
# my_label.pack()# Add the label to the window
# my_label.pack(side="left") # To change location
# my_label.place(x=0,y=0) # For a precise location
my_label.grid(column=0, row=0)

# Update the label text (two ways to do it)
# my_label["text"] = "New Text"
# my_label.config(text="New Text")

# Create a button widget
def button_clicked():
    print("click me again!")
    text = entry.get()
    my_label.config(text=text)

button = Button(text="Click me baby", command=button_clicked)
button.grid(column=1, row=1)  # Add the button to the window

button_a = Button(text="New Button", command=button_clicked)
button_a.grid(column=2, row=0)  # Add the button to the window

entry = Entry(width=10)
entry.grid(column=3, row=2)


# # Using return/enter key
# def write(e):
#     text = e.widget.get()
#     # print(text)
#     my_label.config(text=text)
#
# # Entry
# e = Entry(width=10)
# e.pack()
# e.bind("<Return>", write)
# window.mainloop()




# Start the main event loop (like a 'while True:' loop)
window.mainloop()
