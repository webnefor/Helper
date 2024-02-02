from tkinter import *
from threading import Timer
#
# class LabelFrame(Label):
#     # , word=word, pronc=prnce,example=exmpl,
#     #  translte=trnslte, padx=50, pady=25, font=("Arial", 45)
#     def __init__(self, master, \
#                  word=None, pronc=None, \
#                  example=None, translte=None,\
#                  *args, **kwargs):
#         self.master = master;
#
#         self.random = random.randrange(len(GetArray));
#
#         super().__init__(master,text=word[self.random],
#                          padx=50, pady=25, font=("Arial", 45), *args, **kwargs)
#
#         self.viewPronunc = Label(  # pronunction
#         master=self.master, text=prnce[self.random],
#         padx=0, pady=10, font=("Helvetica", 25, "bold"), bg="red",
#         )
#
#         self.viewExample = Label(  # pronunction
#             master=self.master, text=exmpl[self.random],
#             padx=0, pady=10, font=("Helvetica", 20, "bold"),
#         )
#         self.viewTranslate = Label(  # pronunction
#             master=self.master, text=trnslte[self.random],
#             padx=0, pady=10, font=("Arial", 45), fg="white",
#         )
#     def view(self):
#         self.viewPronunc.pack();
#         super().pack(side="top", fill="both", expand=True);
#
#         exec_d = Timer(5, self.translate);
#         exec_d.start()
#
#     def translate(self):
#         stats:bool = True;
#         while 1:
#             if stats:
#                 super().pack_forget();
#
#                 self.viewTranslate.pack();
#                 self.viewExample.pack();
#
#                 time.sleep(3);
#
#                 self.master.withdraw()
#
#                 time.sleep(1);
#
#                 self.master.deiconify()
#                 self.random = 1;
#                 self.view()
#             else:


def disapper(self):
    self.viewPronunciation.place_forget()
    super().place_forget();

    self.viewTranslate.pack(padx=5, pady=10);
    self.viewExample.place(x=75, y=75, width=250, height=95);

    time.sleep(2)

    self.master.withdraw()

    time.sleep(1)

    return self.appear()


def appear(self):
    self.setrndm = random.randrange(len(src.sortlist.GetArray))

    if self.turnstatus == 0:
        super().place(x=100, y=-20)

        self.viewPronunciation.place(x=155, y=100)
        self.setrndm = 0;

        laterfnc = threading.Timer(3, self.disapper);
        laterfnc.start();
        self.turnstatus = 1;


    else:
        self.master.deiconify()
        self.setrndm = 1;
        self.viewTranslate.pack_forget()
        self.viewExample.place_forget()

        super().update()
        super().place(x=100, y=-20)

        self.viewPronunciation.place(x=155, y=100)
        self.turnstatus = 0
        self.master.update()

        time.sleep(3)

        return self.appear()

    # self.setrndm       = random.randrange(len(src.sortlist.GetArray));

    #
    # self.viewTranslate.place_forget()
    # self.viewExample.place_forget()
