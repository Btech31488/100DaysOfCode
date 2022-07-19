from tkinter import *

#Button Function
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)



#Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#New Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)



#Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


#Entry(Input)

input = Entry(width=10)
input.get()
input.grid(column=3, row=2)


























window.mainloop()