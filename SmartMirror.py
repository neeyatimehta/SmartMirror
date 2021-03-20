from tkinter import *
from _MirrorScreen import MirrorScreen
from _HomeScreen import HomeScreen
from _EntertainmentScreen import EntertainmentScreen
from _OfficeScreen import OfficeScreen



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
        self.tk.bind("<Key>", self.switch_screen)#switching screen
        self.onScreen='mirrorscreen'
        
    def switch_screen(self,event):
        choice = event.char #key value

        #Home Screen
        if choice == 'h':
            for widget in self.frm.winfo_children():
                widget.destroy()
            self.screen = HomeScreen(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.onScreen='homescreen'

        #Black screen
        elif choice == 'b':
            for widget in self.frm.winfo_children():
                widget.destroy()
            self.screen = MirrorScreen(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.onScreen='mirrorscreen'
        
        #Entertainment Screen
        elif choice == 'e':
            for widget in self.frm.winfo_children():
                widget.destroy()
            self.screen = EntertainmentScreen(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.onScreen='entertainmentscreen'
        
        #Office screen
        elif choice == 'o':
            for widget in self.frm.winfo_children():
                widget.destroy()
            self.screen = OfficeScreen(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.onScreen='officescreen'

    #Toggle fullscreen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"


#main function
if __name__ == "__main__":
    window = SmartMirror()
    window.tk.mainloop()


    

        
            

    


