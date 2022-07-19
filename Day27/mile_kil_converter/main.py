from tkinter import *
FONT = ("Arial", 20)

def convert():
    km_convert = float(input.get())
    convert_label.config(text=round(km_convert*1.609))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=20)


input = Entry(width=7)
input.grid(column=1, row=0)

mile_label = Label(text="Miles", font=FONT)
mile_label.grid(column=2, row=0)

equal_label = Label(text=" is equal to", font=FONT)
equal_label.grid(column=0, row=1)

convert_label = Label(text=0, font=FONT)
convert_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)




















window.mainloop()