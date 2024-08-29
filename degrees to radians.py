# Import the necessary modules from tkinter
from tkinter import *

# Constants
pi = 3.141592653589793
MY_FONT = ("Book Antiqua", 18, "bold")

# Create the main window
window = Tk()
window.title("Degrees to Radians Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


# Degrees label widget (INPUT)
degrees_input = Label(
    text="Enter Degrees",
    font=("Arial", 10, "bold"),
    fg="red",
    bg="white"
)
degrees_input.config(text="Enter Degrees")
degrees_input.grid(column=0, row=0)


# Radians label widget
calc_rads = Label(
    font=("Arial", 10, "bold")
)
calc_rads.config(text="Calculated Radians")
calc_rads.grid(column=2, row=0)


# Radians label widget (OUTPUT)
output_label = Label(
    font=("Arial", 10, "italic")
)
output_label.config(text="Calculated Radians")
output_label.grid(column=2, row=1)


# Button widget
entry = Entry(width=10)
entry.grid(column=0, row=1)

def deg_to_red_button():
    text = float(entry.get())
    result = text * pi/180
    output_label.config(text=result)


# button = Button(text="Convert", command=button_clicked)
button = Button(
    text="Convert",
    command=deg_to_red_button,
    fg="black",
    bg="white",
    font=("Arial", 10, "bold"),
    width=10,
    height=2,
    padx=10,
    pady=5,
    bd=2,
    relief="groove",
    activeforeground="red",
    activebackground="blue"
)
button.grid(column=1, row=1)  # Add the button to the window


window.mainloop()


##############################################

# # Shorter way
# from tkinter import *
# # Create the main window
# window = Tk()
# window.title("Degrees to Radians Converter")
# window.minsize(width=500, height=300)
# window.config(padx=100, pady=100)
#
# m = Entry(width=7)
# m.grid(padx=20, pady=20)
#
# window.mainloop()

