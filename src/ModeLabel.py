import random
import threading
import tkinter
import time

import src.sortlist

class ModeLabel(tkinter.Label):
    def __init__(self,master, msec, *args, **kwargs):
        self.msec          = msec;
        self.turnstatus    = 0;
        self.master        = master

        self.x = int(self.master.winfo_screenmmwidth() / 4 - 25)
        self.y = int(self.master.winfo_screenmmheight() /  9   )

    def create(self):
        self.setrndm       = random.randrange(len(src.sortlist.GetArray));

        super().__init__(self.master,
            text=src.sortlist.word[self.setrndm],bg="black",
            font=("Arial", 45), fg="white");
        self.viewPronunciation = tkinter.Label(self.master,
            text=src.sortlist.prnce[self.setrndm], fg="red", font=("Helvetica", 20),bg="black",);
        self.viewExample = tkinter.Label(self.master,
            text="Example: " + src.sortlist.exmpl[self.setrndm] , fg="red",bg="black",font=("Helvetica", 20));
        self.viewTranslate = tkinter.Label(self.master,
            text=src.sortlist.trnslte[self.setrndm]
                                           ,font=("Arial",28 ), fg="white",bg="black",);

    def update(self):

        super().place_forget()
        self.viewPronunciation.place_forget()

        self.viewExample.place(x=22, y=80);
        
        self.viewTranslate.place(x=self.x-10, y=self.y / 2)
        self.turnstatus = 1;
        time.sleep(10)

        self.master.withdraw()
        time.sleep(self.msec)

        return self.appear();

    def appear(self):

        self.master.deiconify()

        if (self.turnstatus == 0):
            self.create()

            super().place(x=self.x - 10, y=self.y / 2);
            self.viewPronunciation.place(x=155, y=85);

            timein = threading.Timer(10, self.update);
            timein.start();

        else:

            self.viewTranslate.place_forget();
            self.viewExample.place_forget()
            self.setrndm = random.randrange(len(src.sortlist.GetArray));
            self.turnstatus = 0;

            return self.appear()

