from tkinter import *
import calendar
import locale
import threading
import time

from contextlib import contextmanager

LOCALE_LOCK = threading.Lock()

ui_locale = '' # e.g. 'fr_FR' fro French, '' as default



@contextmanager
def setlocale(name): #thread proof function to work with locale
    with LOCALE_LOCK:
        saved = locale.setlocale(locale.LC_ALL)
        try:
            yield locale.setlocale(locale.LC_ALL, name)
        finally:
            locale.setlocale(locale.LC_ALL, saved)

class Calendar(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.year = 1111
        self.month = 11
        self.cal_data = calendar.month(self.year, self.month )

        self.title = "Monthly Calendar"
        self.titleLbl = Label(self, text = self.title, font=('Helvetica', 30, 'bold'), fg="white", bg="black")
        self.titleLbl.pack(side=TOP, anchor=W)
        
        self.calLbl = Label(self, font=('Consolas', 20), fg="white", bg="black")
        self.calLbl.pack(side=TOP, anchor=W)
        self.updateCal()
    def updateCal(self):

        with setlocale(ui_locale):
            month=time.strftime('%m')
            year=time.strftime('%Y')
            month=int(month)
            year=int(year)
            if month != self.month or year != self.year:
                self.month = month
                self.year = year
                self.cal_data = calendar.month(self.year, self.month )
                self.calLbl.config(text=self.cal_data)
        self.calLbl.after(864000, self.updateCal)#updates every day

if __name__ == "__main__":
    tk = Tk()
    tk.configure(background="black")
    f = Frame(tk,background="black")
    f.pack()
    w = Calendar(f)
    w.pack()
    tk.mainloop()

        

        
   
