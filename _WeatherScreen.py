from tkinter import *
from aWeather import Weather
from dForecast import Forecasts

class WeatherScreen(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, bg="black")
        self.topFrame = Frame(self, background = 'black')
        self.bottomFrame = Frame(self, background = 'black')
        self.topFrame.pack(side = TOP, fill=BOTH, expand = YES)
        self.bottomFrame.pack(side = TOP, fill=BOTH, expand = YES)
       
        # weather
        self.weather = Weather(self.topFrame)
        self.weather.pack(side=TOP, anchor=CENTER, padx=100, pady=60)
    
        # forecast
        self.forecast = Forecasts(self.bottomFrame)
        self.forecast.pack(side=TOP, anchor=N, padx=100, pady=60)


if __name__ == "__main__": 
    class MainScreen:
        def __init__(self):
            self.tk = Tk()
            self.tk.configure(background='black')
            self.frm = Frame(self.tk, background="black")
            self.frm.pack(side = TOP, fill=BOTH, expand = YES)
            self.screen = WeatherScreen(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.state = False
            self.tk.bind("<Return>", self.toggle_fullscreen)

        def toggle_fullscreen(self, event=None):
            self.state = not self.state  # Just toggling the boolean
            self.tk.attributes("-fullscreen", self.state)
            return "break"

    w = MainScreen()
    w.tk.mainloop()
