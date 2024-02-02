
from tkinter import *

class Gpeg(Tk):

    def __init__(self, path:None=None):

        super().__init__();
        self.path = path;
        print("\033[032mDefault params: \ntime: 1 minute\npath=/list.conf\nU wanna change it? type to -h")

    def start(self) -> int:
        self.setup();

        self.mainloop();

        return 0;

    def setup(self) -> int:

        super().overrideredirect(True)

        super().attributes("-topmost",True)

        screen_width = super().winfo_screenwidth()
        screen_height = super().winfo_screenheight()

        super().geometry(f"{int(screen_width / 4) + 50}x{int(screen_height / 4) - 60}")

        super().wm_geometry("+%d+%d" % ((int(screen_width)-411), \
                                    int(screen_height / screen_height) + 100))

        return 0;


