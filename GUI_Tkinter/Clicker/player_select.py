import tkinter
from tkinter import ttk

import ttkbootstrap as ttkb
from ttkbootstrap import style, Toplevel


class PlayerSelect(ttkb.Toplevel):
    __player_name:str = "test"
    def __init__(self, parent,get_player_name):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.title("Player Selection")
        self.window_width = self.winfo_screenwidth()
        self.window_height = self.winfo_screenheight()
        self.resizable(False, False)
        self.geometry(f"300x150+{int(self.window_width/2)-215+50}+{int(self.window_height/2)-100+30}")
        self.topmost = True
        self.__load_widgets()
        self.get_player_name = get_player_name
        self.attributes('-topmost', 'true')
        self.mainloop()

    def __load_widgets(self):
        label_title = ttkb.Label(self, text="Player Selection",style="success",anchor="center")
        label_title.grid(row=0, column=0, columnspan=2,padx=100, pady=10)
        label_users = ttkb.Label(self, text="Users List :",style="success",anchor="center")
        label_users.grid(row=1, column=0,padx=(30,10), pady=10)
        self.players_combo = ttkb.Combobox(self, style="success",values=['胖德','熊二','噜啦'],justify='center',state="readonly")
        self.players_combo.grid(row=1, column=1, pady=10,padx=(0,30))
        self.players_combo.current(0)
        start_game = ttkb.Button(self, text="Start Game",style="success",command = self.start_game)
        start_game.grid(row=2, column=0,columnspan=2,padx=(15,10), pady=10)


    def start_game(self):
        PlayerSelect.__player_name = self.players_combo.get()
        self.parent.deiconify()
        self.get_player_name(PlayerSelect.__player_name)
        self.destroy()

    @property
    def player_name(self):
        return self.__player_name