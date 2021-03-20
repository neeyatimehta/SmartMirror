from tkinter import *
from PIL import Image, ImageTk
from contextlib import contextmanager

class AppDrawer(Frame):
    def __init__(self, parent, bg ='black'):
        Frame.__init__(self,parent,bg='black')
        self.topFrame = Frame(self, background = 'black')
        self.topFrame.pack(side = TOP, fill = BOTH, expand =YES)
        self.title = "App Drawer"
        self.title=Label(self.topFrame, text=self.title, font =('Helvetica', 40, 'bold'), fg='white', bg='black')
        self.title.pack(side=TOP, anchor=CENTER, pady=50)
        
        self.bottomFrame = Frame(self, background = 'black')
        self.bottomFrame.pack(side = TOP, fill = BOTH, expand = YES)

        #HomeScreen Widget
        self.homeScreen = Frame(self.bottomFrame, background = 'black')
        self.homeScreen.pack(side = LEFT, fill = BOTH, expand = YES, padx=25)
        #HomeScreen Icon
        homeScreenImg = Image.open("assets/Home.png")
        homeScreenImg = homeScreenImg.resize((100,100), Image.ANTIALIAS)
        homeScreenImg = homeScreenImg.convert('RGB')
        homeScreenPhoto = ImageTk.PhotoImage(homeScreenImg)
        self.homeScreenIconLabel = Label(self.homeScreen, bg='black',image=homeScreenPhoto)
        self.homeScreenIconLabel.image = homeScreenPhoto
        self.homeScreenIconLabel.pack(side=TOP,anchor=CENTER)
        #HomeScreen Title
        self.homeScreenLbl = Label(self.homeScreen, text = 'Home Screen', font =('Helvetica', 20, 'bold'), fg='white', bg='black')
        self.homeScreenLbl.pack(side=TOP, anchor=CENTER, pady=50)

        #entertainmentScreen Widget
        self.entertainmentScreen = Frame(self.bottomFrame, background = 'black')
        self.entertainmentScreen.pack(side = LEFT, fill = BOTH, expand = YES, padx=25)
        #entertainmentScreen Icon
        entertainmentScreenImg = Image.open("assets/Entertainment.png")
        entertainmentScreenImg = entertainmentScreenImg.resize((100,100), Image.ANTIALIAS)
        entertainmentScreenImg = entertainmentScreenImg.convert('RGB')
        entertainmentScreenPhoto = ImageTk.PhotoImage(entertainmentScreenImg)
        self.entertainmentScreenIconLabel = Label(self.entertainmentScreen, bg='black',image=entertainmentScreenPhoto)
        self.entertainmentScreenIconLabel.image = entertainmentScreenPhoto
        self.entertainmentScreenIconLabel.pack(side=TOP,anchor=CENTER)
        #entertainmentScreen Title
        self.entertainmentScreenLbl = Label(self.entertainmentScreen, text = 'Entertainment Screen', font =('Helvetica', 20, 'bold'), fg='white', bg='black')
        self.entertainmentScreenLbl.pack(side=TOP, anchor=CENTER, pady=50)

        #officeScreen Widget
        self.officeScreen = Frame(self.bottomFrame, background = 'black')
        self.officeScreen.pack(side = LEFT, fill = BOTH, expand = YES, padx=25)
        #officeScreen Icon
        officeScreenImg = Image.open("assets/Office.png")
        officeScreenImg = officeScreenImg.resize((100,100), Image.ANTIALIAS)
        officeScreenImg = officeScreenImg.convert('RGB')
        officeScreenPhoto = ImageTk.PhotoImage(officeScreenImg)
        self.officeScreenIconLabel = Label(self.officeScreen, bg='black',image=officeScreenPhoto)
        self.officeScreenIconLabel.image = officeScreenPhoto
        self.officeScreenIconLabel.pack(side=TOP,anchor=CENTER)
        #officeScreen Title
        self.officeScreenLbl = Label(self.officeScreen, text = 'Office Screen', font =('Helvetica', 20, 'bold'), fg='white', bg='black')
        self.officeScreenLbl.pack(side=TOP, anchor=CENTER, pady=50)

        #weatherForecast Widget
        self.weatherForecast = Frame(self.bottomFrame, background = 'black')
        self.weatherForecast.pack(side = LEFT, fill = BOTH, expand = YES, padx=25)
        #weatherForecast Icon
        weatherForecastImg = Image.open("assets/PartlySunny.png")
        weatherForecastImg = weatherForecastImg.resize((100,100), Image.ANTIALIAS)
        weatherForecastImg = weatherForecastImg.convert('RGB')
        weatherForecastPhoto = ImageTk.PhotoImage(weatherForecastImg)
        self.weatherForecastIconLabel = Label(self.weatherForecast, bg='black',image=weatherForecastPhoto)
        self.weatherForecastIconLabel.image = weatherForecastPhoto
        self.weatherForecastIconLabel.pack(side=TOP,anchor=CENTER)
        #weatherForecast Title
        self.weatherForecastLbl = Label(self.weatherForecast, text = 'Weather Forecast', font =('Helvetica', 20, 'bold'), fg='white', bg='black')
        self.weatherForecastLbl.pack(side=TOP, anchor=CENTER, pady=50)
        

if __name__ == "__main__": 
    class MainScreen:
        def __init__(self):
            self.tk = Tk()
            self.tk.configure(background='black')
            self.frm = Frame(self.tk, background="black")
            self.frm.pack(side = TOP, fill=BOTH, expand = YES)
            self.screen = AppDrawer(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.state = False
            self.tk.bind("<Return>", self.toggle_fullscreen)

        def toggle_fullscreen(self, event=None):
            self.state = not self.state  # Just toggling the boolean
            self.tk.attributes("-fullscreen", self.state)
            return "break"

    w = MainScreen()
    w.tk.mainloop()

