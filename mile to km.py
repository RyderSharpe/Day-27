from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to KM")

miles_input = Entry(width=30) # Widget
miles_input.grid(column=1, row=0) # Location on grid
window.config(padx=20, pady=20)

miles_label = Label(text = "miles") # Widget
miles_label.grid(column=2, row=0) # Location on grid

is_equal_label = Label(text="Equal to") # Widget
is_equal_label.grid(column=0, row=1) # Location on grid

km_result_label = Label(text = "0") # Widget
km_result_label.grid(column=1, row=1) # Location on grid

km_label = Label(text="km") # Widget
km_label.grid(column=2, row=1) # Location on grid

calculate_button = Button(text="Calculate", command = miles_to_km) # Widget
calculate_button.grid(column=1, row=2) # Location on grid


window.mainloop()