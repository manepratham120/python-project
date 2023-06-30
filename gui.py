from tkinter import *


top = Tk()
top.geometry("450x300")


linked_list1_label = Label(top, text="LongInteger1",padx=20,pady=10)
linked_list1_label.grid(row=0, column=0)

linked_list2_label = Label(top, text="LongInteger2",padx=20,pady=10)
linked_list2_label.grid(row=1, column=0)

operator_label = Label(top, text="Operator", padx=10, pady=10)
operator_label.grid(row=2, column=0)

operator_var = StringVar(top)
operator_var.set("+")
operator_options = OptionMenu(top, operator_var, "+", "-", "*", "/")
operator_options.grid(row=2, column=1)

result_button = Button(top, text="Result", fg="black", activebackground = "white")
result_button.grid(row=4, column=1,padx=40,pady=20)

area_of_list1 = Entry(top, width=30)
area_of_list1.grid(row=0, column=1)

area_of_list2 = Entry(top, width=30)
area_of_list2.grid(row=1, column=1)

top.mainloop()