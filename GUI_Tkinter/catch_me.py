from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap import style
import random


class CatchMe():
    def __init__(self):
        self.root = Tk()
        self.root.title("Catch Me")
        self.root.geometry("500x500")
        self.root.resizable(width=False, height=False)
        self.style = ttkb.Style("superhero")
        self.__load_widgets()
        self.root.mainloop()

    def __load_widgets(self):
        self.running_button = ttkb.Button(self.root,width=10,text="Catch Me",style='warning')
        self.running_button.place(x=10,y=10)
        self.running_button.bind("<Enter>",self.catch_me)

    def catch_me(self,event):
        random_x = random.randint(0,460)
        random_y = random.randint(0,470)
        self.running_button.place(x=random_x,y=random_y)


if __name__ == "__main__":
    CatchMe()



