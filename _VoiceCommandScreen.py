from tkinter import *
class VoiceCommandScreen(Frame):
    
    def __init__(self, parent, command_response='Listening...'):
        Frame.__init__(self, parent, bg="black")
        self.topFrame = Frame(self, background = 'black')
        self.topFrame.pack(side = TOP, fill=BOTH, expand = YES)
        self.commandResponse=command_response
        self.commandResponseLbl=Label(self.topFrame, text=self.commandResponse,wraplength=1000, font =('Helvetica', 48, 'bold'), fg='white', bg='black')
        self.commandResponseLbl.pack(side=TOP, anchor=CENTER, pady=100)
                                      
if __name__ == "__main__": 
    class MainScreen:
        def __init__(self):
            self.tk = Tk()
            self.tk.configure(background='black')
            self.frm = Frame(self.tk, background="black")
            self.frm.pack(side = TOP, fill=BOTH, expand = YES)
            self.screen = VoiceCommandScreen(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.state = False
            self.tk.bind("<Return>", self.toggle_fullscreen)

        def toggle_fullscreen(self, event=None):
            self.state = not self.state  # Just toggling the boolean
            self.tk.attributes("-fullscreen", self.state)
            return "break"

    w = MainScreen()
    w.tk.mainloop()
