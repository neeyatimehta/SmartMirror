from tkinter import *
from bMovies import Movies
from bShows import Shows

class EntertainmentScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")
        #self.config(bg='black')
        self.leftFrame = Frame(self, background = 'black')
        self.rightFrame = Frame(self, background = 'black')
        self.leftFrame.pack(side = LEFT, fill=BOTH, expand = YES)
        self.rightFrame.pack(side = RIGHT, fill=BOTH, expand = YES)
        # movies
        self.movies = Movies(self.leftFrame)
        self.movies.pack(side=LEFT, anchor=N, padx=100, pady=60)
        # shows
        self.shows = Shows(self.rightFrame)
        self.shows.pack(side=LEFT, anchor=N, padx=100, pady=60)
       

if __name__ == "__main__": 
    class MainScreen:
        def __init__(self):
            self.tk = Tk()
            self.tk.configure(background='black')
            self.frm = Frame(self.tk, background="black")
            self.frm.pack(side = TOP, fill=BOTH, expand = YES)
            self.screen = EntertainmentScreen(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.state = False
            self.tk.bind("<Return>", self.toggle_fullscreen)

        def toggle_fullscreen(self, event=None):
            self.state = not self.state  # Just toggling the boolean
            self.tk.attributes("-fullscreen", self.state)
            return "break"

    w = MainScreen()
    w.tk.mainloop()
