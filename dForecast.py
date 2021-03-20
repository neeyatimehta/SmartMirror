from tkinter import *
import requests
import json
from datetime import datetime

from PIL import Image, ImageTk
from contextlib import contextmanager

class Forecasts(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.config(bg='black')
        self.title = 'Weekly Forecast'
        self.titleLbl = Label(self, text=self.title,font=('Helvetica', 30,'bold'),fg="white",bg="black")
        self.titleLbl.pack(side=TOP, anchor=W)
        self.forecastContainer = Frame(self,bg="black")
        self.forecastContainer.pack(side=LEFT)
        self.get_forecast()



    def get_forecast(self):

        #Requesting data from api
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/daily"

        querystring = {"lat":"23.022505","lon":"72.571365","units":"metric","lang":"en"}

        headers = {
            'x-rapidapi-key': "b9480bbd0dmsh8ce179da7a322e7p19cde9jsn65611d1d0648",
            'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        forecast_obj = json.loads(response.text)

        data = forecast_obj['data']

        i=0
        
        #setting values
        for day in data:
            if i>7:
                break
            high_temp = day['high_temp']
            low_temp =  day['low_temp']
            date = day['datetime']
            dateTimeObject = datetime.strptime(date, "%Y-%m-%d")
            
            #print(str(high_temp) + " " +str(low_temp)+ " "+ str(forecast_day) )
                    
           
            degree_sign = u'\N{DEGREE SIGN}'
            high_temperature = "%s%sC" % (str(int(high_temp)),degree_sign)
            low_temperature = "%s%sC" % (str(int(low_temp)),degree_sign)
            forecast_day = dateTimeObject.strftime("%a")


            forecastFrm = Forecast(self.forecastContainer, high_temperature, low_temperature, forecast_day)
            forecastFrm.pack(side=LEFT, anchor=N, padx=25)
            i += 1

        self.after(8640000, self.get_forecast)# called everyday

class Forecast(Frame):
    def __init__(self, parent, high_temperature, low_temperature, forecast_day):
        Frame.__init__(self, parent,bg="black")
        self.dayLbl = Label(self, text = forecast_day, font =('Helvetica', 20, 'bold'), fg='white', bg='black')
        self.dayLbl.pack(side=TOP, anchor=CENTER)
        self.tempLbl = Label(self, text = high_temperature + ' - ' + low_temperature, font =('Helvetica', 15, 'bold'), fg='white', bg='black')
        self.tempLbl.pack(side=TOP, anchor=CENTER)
        


if __name__ == "__main__":
    tk = Tk()
    tk.configure(background="black")
    f = Frame(tk,background="black")
    f.pack()
    w = Forecasts(f)
    w.pack()
    tk.mainloop()

