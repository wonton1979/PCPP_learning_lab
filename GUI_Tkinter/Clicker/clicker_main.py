import datetime
from tkinter import Tk, Menu
from tkinter import messagebox
import ttkbootstrap as ttkb
from ttkbootstrap import Style
from player_select import PlayerSelect
import random
from leader_board import LeaderBoard

class Clicker:
    def __init__(self):
        self.player_name = None
        self.time_counter_id = None
        self.root = Tk()
        self.root.title("Clicker")
        self.window_width = self.root.winfo_screenwidth()
        self.window_height = self.root.winfo_screenheight()
        self.root.resizable(False, False)
        self.style = Style("superhero")
        self.button_list = list()
        self.root.geometry(f"430x190+{int(self.window_width/2)-215}+{int(self.window_height/2)-100}")
        self.timer_second = 0
        self.first_click = False
        self.click_correct_count = 0
        self.__load_widgets()
        self.root.withdraw()
        self.user_name = PlayerSelect(self.root,self.get_player_name)
        self.root.mainloop()


    def __load_widgets(self):
        main_menu = Menu(self.root)
        self.root.config(menu=main_menu)
        sub_menu_game = Menu(main_menu, tearoff=False,font="Helvetica 8 bold")
        main_menu.add_cascade(label="Game", menu=sub_menu_game)
        main_menu.add_command(label="Exit Game", command=self.root.destroy)
        sub_menu_game.add_command(label='New Game',command = self.start_new_game)
        sub_menu_game.add_command(label='Leader Board',command = self.show_leader_board)
        self.list_of_numbers = list()
        button_index = 0
        grid_x:int = 0
        for i in range(0,5):
            for j in range(0,5):
                button_text = random.randint(0,999)
                self.list_of_numbers.append(button_text)
                grid_x = i
                grid_y = j
                self.button_list.append(ttkb.Button(self.root,text=str(button_text),style='TButton,groove',width=10,
                                                    command=lambda text=button_text,index=button_index:self.game_start(text,index)))
                self.button_list[button_index].grid(row=grid_x, column=grid_y,padx=1,pady=1)
                button_index += 1
        self.time_counter = ttkb.Label(self.root,text=f"Time : {self.timer_second}",style='TLabel')
        self.time_counter.grid(row=grid_x+1, column=0,columnspan = 5,pady=8)
        self.style.configure("TLabel",font=("Arial",10,"bold"),foreground="white")
        self.style.configure("TButton", foreground="black")


    def timer(self):
        self.timer_second += 1
        self.time_counter.config(text=f"Time : {self.timer_second}")
        if self.timer_second <= 100:
           self.time_counter_id = self.time_counter.after(1000, self.timer)

    def game_start(self,text,button_index):
        if not self.first_click:
            self.time_counter.after(1000, self.timer)
            self.first_click = True
        self.list_of_numbers.sort()
        if text == self.list_of_numbers[0]:
            self.button_list[button_index].config(state='disabled')
            self.list_of_numbers.remove(self.list_of_numbers[0])
            self.click_correct_count += 1
        if self.click_correct_count == 25:
            self.time_counter.after_cancel(self.time_counter_id)
            messagebox.showinfo("Success", f"Congratulations! You finished this challenge in {self.timer_second}, You won!")
            self.record_file_process()

    def record_file_process(self):
        high_record_list = list()
        try:
            with open("record.txt","r",encoding='utf-8') as file:
                record = file.readlines()
            if len(record) < 5 :
                with open("record.txt","a",encoding='utf-8') as file:
                    file.write(f"{len(record)+1}. {self.player_name} {self.timer_second} Seconds "
                               f"{datetime.datetime.today().strftime('%d/%m/%Y')} {datetime.datetime.now().strftime('%H:%M:%S')}\n ")
            elif len(record) == 5:
                for each_record in record:
                    each_record_split = each_record.split(" ")
                    print(each_record_split)
                    if self.timer_second < int(each_record_split[2]):
                        each_record_split[1] = self.player_name
                        each_record_split[2] = str(self.timer_second)
                        each_record_split[3] = datetime.datetime.today().strftime('%d/%m/%Y')
                        each_record_split[4] = datetime.datetime.now().strftime('%H:%M:%S')+"\n"
                        self.timer_second = 10000
                    high_record_list.append(" ".join(each_record_split))
                high_record_list.sort()
                with open("record.txt","w",encoding='utf-8') as file:
                    for each_record in high_record_list:
                        file.writelines(f"{each_record}")
        except FileNotFoundError:
            print("There is no file which named 'record.txt'")
        except PermissionError:
            print("You don't have permission to write file")
        except IOError:
            print("File Process Error")

    def start_new_game(self):
        self.timer_second = 0
        print(self.time_counter["text"])
        self.button_list = []
        self.root.geometry(f"430x210+{int(self.window_width/2)-215}+{int(self.window_height/2)-100}")
        self.__load_widgets()

    def show_leader_board(self):
        LeaderBoard(self)

    def get_player_name(self,player_name):
        self.player_name = player_name



if __name__ == '__main__':
    Clicker()