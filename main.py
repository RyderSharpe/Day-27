import tkinter

window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")
# my_label_a = tkinter.Label(text="I am another label", font=("Arial", 24, "bold"))
# my_label_a.pack(expand=True)








# Like a 'while True:'


window.mainloop()
