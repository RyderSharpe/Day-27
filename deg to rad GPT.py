from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Constants
pi = 3.141592653589793

# Function to convert based on selected mode
def convert():
    value = entry.get()
    if value:  # Check if the input field is not empty
        try:
            value_float = float(value)
            if conversion_mode.get() == "DegToRad":
                result = value_float * pi / 180
                output_label.config(text=f"{result:.4f} radians")
            else:
                result = value_float * 180 / pi
                output_label.config(text=f"{result:.4f} degrees")
            entry.config(foreground="black")
            add_to_history(value, result)
        except ValueError:
            entry.config(foreground="red")
            messagebox.showerror("Invalid Input", "Please enter a valid number")

# Function to add a conversion to history
def add_to_history(input_value, output_value):
    conversion_type = "Degrees to Radians" if conversion_mode.get() == "DegToRad" else "Radians to Degrees"
    history_list.insert(END, f"{input_value} -> {output_value:.4f} ({conversion_type})")

# Function to reset the input field, output label, and history
def reset_fields():
    entry.delete(0, END)
    output_label.config(text="Result will be displayed here")
    history_list.delete(0, END)

# Function to copy the result to the clipboard
def copy_to_clipboard():
    result_text = output_label.cget("text")
    window.clipboard_clear()
    window.clipboard_append(result_text)
    messagebox.showinfo("Copied", "Result copied to clipboard!")

# Function to toggle between light and dark themes
def toggle_theme():
    current_theme = theme.get()
    if current_theme == "Light":
        window.config(bg="#333333")
        frame.config(style="Dark.TFrame")
        theme.set("Dark")
        theme_button.config(text="Switch to Light Theme")
    else:
        window.config(bg="white")
        frame.config(style="Light.TFrame")
        theme.set("Light")
        theme_button.config(text="Switch to Dark Theme")

# Create the main window
window = Tk()
window.title("Degrees to Radians Converter")
window.geometry("500x600")
window.config(bg="white")
window.resizable(False, False)

# Theme variable
theme = StringVar(value="Light")

# Frame for Input and Output
frame = ttk.Frame(window, padding="20 20 20 20", style="Light.TFrame")
frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=20, pady=20)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# Conversion Mode Selection
conversion_mode = StringVar(value="DegToRad")
deg_to_rad_radio = ttk.Radiobutton(
    frame, text="Degrees to Radians", variable=conversion_mode, value="DegToRad"
)
deg_to_rad_radio.grid(column=0, row=0, sticky=W)
rad_to_deg_radio = ttk.Radiobutton(
    frame, text="Radians to Degrees", variable=conversion_mode, value="RadToDeg"
)
rad_to_deg_radio.grid(column=1, row=0, sticky=W)

# Input Label
input_label = ttk.Label(frame, text="Enter Value:")
input_label.grid(column=0, row=1, sticky=W)

# Entry widget for user input
entry = ttk.Entry(frame, width=10)
entry.grid(column=1, row=1, sticky=(W, E))
entry.bind("<KeyRelease>", lambda event: convert())

# Output Label
output_label = ttk.Label(frame, text="Result will be displayed here", foreground="blue")
output_label.grid(column=1, row=2, sticky=(W, E))

# Convert Button
convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.grid(column=0, row=3, sticky=W)

# Reset Button
reset_button = ttk.Button(frame, text="Reset", command=reset_fields)
reset_button.grid(column=1, row=3, sticky=E)

# Copy to Clipboard Button
copy_button = ttk.Button(frame, text="Copy Result", command=copy_to_clipboard)
copy_button.grid(column=1, row=4, sticky=E)

# History Label and Listbox
history_label = ttk.Label(frame, text="Conversion History:")
history_label.grid(column=0, row=5, sticky=W)
history_list = Listbox(frame, height=10, width=50)
history_list.grid(column=0, row=6, columnspan=2, sticky=(W, E))

# Theme Toggle Button
theme_button = ttk.Button(frame, text="Switch to Dark Theme", command=toggle_theme)
theme_button.grid(column=0, row=8, columnspan=2, pady=10)

# Menu Bar for Help/About
menu_bar = Menu(window)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Degrees to Radians Converter v1.0\nDeveloped by Sharpe Electrical Engineering Services"))
menu_bar.add_cascade(label="Help", menu=help_menu)
window.config(menu=menu_bar)

# Instructions Label
instructions_label = ttk.Label(
    window,
    text="Select a conversion type, enter a value, and see the result in real-time.",
    font=("Helvetica", 10, "italic"),
    background="white",
    foreground="grey",
    wraplength=500,
)
instructions_label.grid(column=0, row=6, padx=20, pady=10)

# Make sure widgets are centered and have enough space
for widget in frame.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# Run the application
window.mainloop()