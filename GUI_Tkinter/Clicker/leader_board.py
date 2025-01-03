import ttkbootstrap as ttkb
from ttkbootstrap import Toplevel


class LeaderBoard(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.title("Leader Board")
        self.window_width = self.winfo_screenwidth()
        self.window_height = self.winfo_screenheight()
        self.geometry(f"300x350+{int(self.window_width/2)-160}+{int(self.window_height/2)-180}")
        self.resizable(False, False)
        self.__load_widgets()
        self.mainloop()

    def __load_widgets(self):
        self.label_list = list()
        try:
            with open('record.txt', 'r',encoding='utf-8') as file:
                result = file.readlines()
                label_index = 0
                for line in result:
                    self.label_list.append(ttkb.Label(self, text=line, style="warning"))
                    self.label_list[label_index].pack(pady = 10)
                    label_index += 1
            close_button = ttkb.Button(self, text="Close", command=self.close_leader_board,style="warning")
            close_button.pack(pady = 10)
        except FileNotFoundError:
            print("There is no file which named 'record.txt'")
        except PermissionError:
            print("You don't have permission to write file")
        except IOError:
            print("File Process Error")

    def close_leader_board(self):
        self.withdraw()

