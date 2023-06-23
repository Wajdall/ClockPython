from time import *
from tkinter import *
def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string= strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)


window = Tk()

canvas = Canvas(window, width=1000, height=600)
canvas.pack()

bg_image = PhotoImage(file=r"C:\Users\96653\Desktop\image\cat-boarding-24.png")


canvas.create_image(650, 300, image=bg_image)


time_label = Label(window,font=("Ink free",50),fg="black")
time_label.pack()
canvas.create_window(250,250,window=time_label)
day_label = Label(window,font=("Ink free",25))
day_label.pack()
canvas.create_window(250,300,window=day_label)
date_label = Label(window,font=("Ink free",25))
date_label.pack()
canvas.create_window(250,350,window=date_label)


update()

window.mainloop()