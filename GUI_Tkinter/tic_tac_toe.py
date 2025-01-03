import tkinter as tk
import random
from tkinter import Tk
from tkinter import messagebox


class TicTacToe(Tk):
    WINNING_LISTS = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    RANDOM_LIST = [1,2,3,4,6,7,8,9]
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.window_width = self.winfo_screenwidth()
        self.window_height = self.winfo_screenheight()
        self.geometry(f"410x420+{int(self.window_width/2)-205}+{int(self.window_height/2)-210}")
        self.resizable(width=False, height=False)
        self.button_group = list()
        self.user_clicked = list()
        self.computer_clicked = [5]
        self.user_clicked_count = 0
        self.computer_clicked_count = 0
        self.default_bg = self.cget('bg')
        self.__load_widgets()
        self.__game_start()
        self.mainloop()

    def __load_widgets(self):
        button_index = 0

        for i in range(0,3):
            for j in range(0,3):
                self.button_group.append(tk.Button(self,width=3, text="X",
                                                   foreground= self.default_bg,font=("Arial",50,"bold"),
                                                   activeforeground=self.default_bg,
                                                   command = lambda index = button_index: self.player_click(index)))
                self.button_group[button_index].grid(row=i,column=j,padx=(2,),pady=1)
                button_index += 1

    def __game_start(self):
        user_confirmation = messagebox.askyesno(title="Game start confirmation",message="Game is about to start, Are you ready?")
        if user_confirmation:
            self.button_group[4].config(disabledforeground='red',state=tk.DISABLED)
        else:
            self.destroy()

    def player_click(self,button_index):
        game_over = False
        if len(TicTacToe.RANDOM_LIST) > 0 and game_over == False :
            self.button_group[button_index].config(disabledforeground = "green",text="O",state=tk.DISABLED)
            TicTacToe.RANDOM_LIST.remove(button_index+1)
            self.user_clicked.append(button_index+1)
            self.user_clicked.sort()
            self.user_clicked_count += 1
            computer_random = random.choice(self.RANDOM_LIST)
            self.button_group[computer_random-1].config(disabledforeground='red',state=tk.DISABLED)
            TicTacToe.RANDOM_LIST.remove(computer_random)
            self.computer_clicked.append(computer_random)
            self.computer_clicked.sort()
            self.computer_clicked_count += 1
            if self.computer_clicked_count >= 3:
                win_check_result = self.check_winner()
                if win_check_result is not None:
                    if win_check_result[0]:
                        messagebox.showinfo(title="Congratulations!",message=f"{win_check_result[1]} Wins !")
                    else:
                        messagebox.showinfo(title="Sorry!", message=f"{win_check_result[1]} Wins !")
                    for each_remain_button in self.RANDOM_LIST:
                        self.button_group[each_remain_button-1].config(disabledforeground=self.default_bg,state=tk.DISABLED)

    def check_winner(self):
        for each_winning_list in self.WINNING_LISTS:
            if set(each_winning_list).issubset(set(self.user_clicked)) or each_winning_list == self.user_clicked:
                return [True, 'Player']
            elif set(each_winning_list).issubset(self.computer_clicked) or each_winning_list == self.computer_clicked:
                return [True, 'Computer']
        if self.user_clicked_count == 4 and self.computer_clicked_count == 4:
            return [False,'No One']





if __name__ == "__main__":
    TicTacToe()


