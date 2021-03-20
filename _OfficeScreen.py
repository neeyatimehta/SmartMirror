from tkinter import *
from cCalendarEvents import CalendarEvents
from cCalendar import Calendar
from cTasks import Tasks



class OfficeScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")
        self.leftFrame = Frame(self, background = 'black')
        self.rightFrame = Frame(self, background = 'black')
        self.leftFrame.pack(side = LEFT, fill=BOTH, expand = YES)
        self.rightFrame.pack(side = RIGHT, fill=BOTH, expand = YES)
        # calEvents
        self.calEvents = CalendarEvents(self.rightFrame)
        self.calEvents.pack(side=TOP, anchor=W, padx=50, pady=60)
        # Cal
        self.cal = Calendar(self.leftFrame)
        self.cal.pack(side=TOP, anchor=W, padx=100, pady=60)
        # Tasks
        self.tasks = Tasks(self.leftFrame)
        self.tasks.pack(side=TOP, anchor=W, padx=100, pady=(0,60))


if __name__ == "__main__": 
    class MainScreen:
        def __init__(self):
            self.tk = Tk()
            self.tk.configure(background='black')
            self.frm = Frame(self.tk, background="black")
            self.frm.pack(side = TOP, fill=BOTH, expand = YES)
            self.screen = OfficeScreen(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.state = False
            self.tk.bind("<Return>", self.toggle_fullscreen)

        def toggle_fullscreen(self, event=None):
            self.state = not self.state  # Just toggling the boolean
            self.tk.attributes("-fullscreen", self.state)
            return "break"

    w = MainScreen()
    w.tk.mainloop()
        
            

    


