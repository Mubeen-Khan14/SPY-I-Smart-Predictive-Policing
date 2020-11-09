# Text Labels
from tkinter import *
from tkinter.ttk import Combobox
window=Tk()

# add widgets here
window.title('SPY I - Smart Predictive policing')

#Label
lbl=Label(window, text="Crowd Density Estimation", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)

#Button
btn=Button(window, text="Start people counting", fg='blue')
btn.place(x=80, y=100)
window.geometry("400x300+10+20")


#Input Dialog Box
txtfld=Entry(window, text="nbr of people are 100 approximate", bd=5)
txtfld.place(x=80, y=150)


#Textfield
var = StringVar()
var.set("one")
videos=("one", "two", "three", "four")
cb=Combobox(window, values=videos)
cb.place(x=100, y=150)

lb=Listbox(window, height=5, selectmode='multiple')
for num in videos:
    lb.insert(END,num)
lb.place(x=250, y=150)

v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="anamolay/normal activity", variable=v0,value=1)
r1.place(x=200,y=100)
                
v1 = IntVar()
C1 = Checkbutton(window, text = "activity recognization", variable = v1)
C1.place(x=200, y=100)
window.mainloop()