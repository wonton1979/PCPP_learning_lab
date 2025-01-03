from tkinter import Tk
import ttkbootstrap as ttkb

class TrafficLight(Tk):
    __PHASES = (('red', 'grey', 'grey'),
              ('red', 'yellow', 'grey'),
              ('grey', 'grey', 'green'),
              ('grey', 'yellow', 'grey'))

    def __init__(self):
        super().__init__()
        self.title("Traffic Light")
        self.window_width = self.winfo_screenwidth()
        self.window_height = self.winfo_screenheight()
        self.geometry(f"200x430+{int(self.window_width/2)-100}+{int(self.window_height/2)-200}")
        self.__load_widgets()
        self.phases_index = 1
        self.mainloop()


    def __load_widgets(self):
        self.lights_canvas = ttkb.Canvas(self, width=210, height=340)
        self.lights_canvas.pack()
        self.lights_canvas.create_oval(50, 10, 150, 110, fill="red", outline="black",width=2)
        self.lights_canvas.create_oval(50, 120, 150, 220, fill="grey", outline="black", width=2)
        self.lights_canvas.create_oval(50, 230, 150, 330, fill="grey", outline="black", width=2)
        next_button = ttkb.Button(self, text="Next", command=self.next_change)
        next_button.pack(pady=10)
        quit_button = ttkb.Button(self, text="Quit", command=self.destroy)
        quit_button.pack()
        self.lights_canvas.config(bg="dimgray")

    def next_change(self):
        self.phases_index %= len(self.__PHASES)
        self.lights_canvas.create_oval(50, 10, 150, 110, fill=f"{TrafficLight.__PHASES[self.phases_index][0]}", outline="black", width=2)
        self.lights_canvas.create_oval(50, 120, 150, 220, fill=f"{TrafficLight.__PHASES[self.phases_index][1]}", outline="black", width=2)
        self.lights_canvas.create_oval(50, 230, 150, 330, fill=f"{TrafficLight.__PHASES[self.phases_index][2]}", outline="black", width=2)
        self.phases_index += 1
if __name__ == "__main__":
    TrafficLight()