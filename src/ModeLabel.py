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

    def create(self):
        self.setrndm       = random.randrange(len(src.sortlist.GetArray));

        super().__init__(self.master,
                                         text=src.sortlist.word[self.setrndm],
                                                        pady=55,font=("Arial", 45), fg="white");
        self.viewPronunciation = tkinter.Label(self.master,
                                         text=src.sortlist.prnce[self.setrndm], fg="red", font=("Helvetica", 20));
        self.viewExample = tkinter.Label(self.master,
                                         text="Example: " + src.sortlist.exmpl[self.setrndm] , fg="red", pady=250);
        self.viewTranslate = tkinter.Label(self.master,
                                         text=src.sortlist.trnslte[self.setrndm], pady=25,font=("Arial", 45), fg="red");

    def update(self):

        super().place_forget()
        self.viewPronunciation.place_forget()

        self.viewTranslate.pack(padx=5, pady=10);
        self.viewExample.place(x=75, y=75, width=250, height=95);

        self.turnstatus = 1;
        time.sleep(6)

        self.master.withdraw()
        time.sleep(self.msec)

        return self.appear();

    def appear(self):

        self.master.deiconify()

        if (self.turnstatus == 0):
            self.create()

            super().place(x=100, y=-20);
            self.viewPronunciation.place(x=155, y=100);

            timein = threading.Timer(10, self.update);
            timein.start();

        else:

            self.viewTranslate.pack_forget();
            self.viewExample.place_forget()
            self.setrndm = random.randrange(len(src.sortlist.GetArray));
            self.turnstatus = 0;

            return self.appear()

