import tkinter
from tkinter import *
from tkinter import messagebox, ttk

import ttkbootstrap
from ttkbootstrap import Style


class Calculator:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x210')
        self.root.title('Simple Calculator')
        self.root.resizable(False, False)
        self.style = Style('superhero')
        self.first_input_value = StringVar()
        self.first_input_value.set("")
        self.first_input_value.trace_add('write', self.__edit_text_one)
        self.second_input_value = StringVar()
        self.second_input_value.set("")
        self.second_input_value.trace_add('write', self.__edit_text_two)
        self.first_string = ""
        self.second_string = ""
        self.__load_widgets()
        self.root.mainloop()

    def __load_widgets(self):
        self.radio_group_observer = IntVar()
        self.radio_group_observer.set(1)
        plus_sign = ttkbootstrap.Radiobutton(self.root, text='+', value='1', variable=self.radio_group_observer, style='TRadiobutton,danger')
        plus_sign.grid(row=0,column=0,columnspan=2,pady=(20,0))
        minus_sign = ttkbootstrap.Radiobutton(self.root, text='- ', value='2', variable=self.radio_group_observer,
                                              style='TRadiobutton,warning')
        minus_sign.grid(row=1,column=0,columnspan=2,pady=(10,0))
        self.first_input = ttkbootstrap.Entry(self.root,width=20,textvariable=self.first_input_value)
        self.first_input.grid(row=2,column=0,padx=10)
        self.first_input.bind('<BackSpace>', self.backspace_handling_one)
        self.second_input = ttkbootstrap.Entry(self.root, width=20,textvariable=self.second_input_value)
        self.second_input.grid(row=2,column=1,padx=(0,10))
        self.second_input.bind('<BackSpace>', self.backspace_handling_two)
        multiply_sign = ttkbootstrap.Radiobutton(self.root, text='*', value='3', variable=self.radio_group_observer,
                                                 style='TRadiobutton,success')
        multiply_sign.grid(row=3,column=0,columnspan=2)
        self.style.configure('TRadiobutton', font=('Arial', 16, 'bold'),foreground='white')
        division_sign = ttkbootstrap.Radiobutton(self.root, text='/', value='4', variable=self.radio_group_observer,
                                                 style='TRadiobutton,primary')
        division_sign.grid(row=4, column=0, columnspan=2)
        evaluate = ttkbootstrap.Button(self.root,text="Evaluate",command=self.calculate)
        evaluate.grid(row=5,column=0,columnspan=2,pady=(10,0))

    def calculate(self):
        if self.first_input.get() == "" or self.second_input.get() == "":
            messagebox.showerror('Error', 'Please enter all values')
        else:
            if self.radio_group_observer.get() == 1:
                result = int(self.first_input.get())+int(self.second_input.get())
                messagebox.showinfo('Success', 'The result is: ' + str(result))
            elif self.radio_group_observer.get() == 2:
                result = int(self.first_input.get()) - int(self.second_input.get())
                messagebox.showinfo('Success', 'The result is: ' + str(result))
            elif self.radio_group_observer.get() == 3:
                result = int(self.first_input.get()) * int(self.second_input.get())
                messagebox.showinfo('Success', 'The result is: ' + str(result))
            else:
                try:
                    result = round(int(self.first_input.get()) / int(self.second_input.get()),2)
                    messagebox.showinfo('Success', 'The result is: ' + str(result))
                except ZeroDivisionError:
                    messagebox.showinfo('Error', 'You can\'t divide by zero')
                    self.second_input.delete(0, END)
                    self.second_input.focus()
        self.first_string = ""
        self.second_string = ""



    def __edit_text_one(self, *args):
        if not self.first_input.get().isdigit():
            self.first_input_value.set("")
        else:
            self.first_string = self.first_input.get()
        self.first_input_value.set(self.first_string)

    def __edit_text_two(self, *args):
        if not self.second_input.get().isdigit():
            self.second_input_value.set("")
        else:
            self.second_string = self.second_input.get()
        self.second_input_value.set(self.second_string)


    def backspace_handling_one(self, event):
        if len(self.first_string) == 1:
            self.first_string = ""

    def backspace_handling_two(self, event):
        if len(self.second_string) == 1:
            self.second_string = ""

if __name__ == '__main__':
    calculator = Calculator()







