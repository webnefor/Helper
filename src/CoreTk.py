
from tkinter import *

class Gpeg(Tk):

    def __init__(self,mode=1, path:None=None):

        super().__init__();
        self.path = path;
        self.setscreen_width = super().winfo_screenwidth()
        self.setscreen_height = super().winfo_screenheight()
        self.mode = mode;
        self.size_wind_x = int(self.setscreen_width / 4 - 25);
        self.size_wind_y = int(self.setscreen_height / 9);

        print("\033[032mDefault params: \ntime: 1 minute\npath=/list.conf\nU wanna change it? type to -h")

    def start(self) -> int:
        self.setup();
        self.mainloop();

        return 0;

    def setup(self) -> int:

        super().overrideredirect(self.mode)
        super().configure(background="black")
        super().attributes("-topmost",True)
        super().geometry(f"{self.size_wind_x+50}x{self.size_wind_y+50}")
        super().wm_geometry(f"+{int(0)}+{50}")


        return 0;


