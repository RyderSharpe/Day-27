# Import the necessary modules from tkinter
from tkinter import *

# Create main window
window = Tk()
window.title("Celsius to Kelvin")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10, bg="light cyan")

# Celsius label
celsius_label = Label(
    text = "Enter temperature in celsius",
    font=("Arial", 10, "bold"),
    fg = "blue",
)
celsius_label.grid(column=0, row=0)

# Celsius entry
entry = Entry(width=10)
entry.grid(column=0, row=1)



# Conversion
def convert_to_kelvin():
    global kelvin
    celsius = float(entry.get())
    kelvin = celsius + 273.15
    kelvin_converted.config(text=kelvin)


# Button widget
def button_clicked():
    convert_to_kelvin()
    print("clicked")

# Convert Button
button = Button(text="Convert",command=button_clicked)
button.grid(column=1, row=1)  # Add the button to the window


# Calculated temperature in kelvin label
kelvin_label = Label(
    text = "Calculated temperature in kelvin",
    font=("Arial", 10, "bold"),
    fg = "blue",
)
kelvin_label.grid(column=2, row=0)

# Kelvin_converted
kelvin_converted = Label(
    text = "???",
    font=("Arial", 10, "bold"),
    fg = "blue",
)
kelvin_converted.grid(column=2, row=1)



# Keep the main window open
window.mainloop()
