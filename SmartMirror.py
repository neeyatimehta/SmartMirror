from tkinter import *
from _MirrorScreen import MirrorScreen



class SmartMirror:
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='black')
        self.frm = Frame(self.tk, background="black") #screen container
        self.frm.pack(side = TOP, fill=BOTH, expand = YES)
        self.screen = MirrorScreen(self.frm) #display screen variable
        self.screen.pack(side = TOP, fill=BOTH, expand = YES)
        self.state = False #fullscreen toggle variable
        self.tk.bind("<Return>", self.toggle_fullscreen)

    #Toggle fullscreen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"


#main function
if __name__ == "__main__":
    window = SmartMirror()
    window.tk.mainloop()


    

        
            

    


