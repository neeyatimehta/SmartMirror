from tkinter import *
import requests
import json

from PIL import Image, ImageTk
from contextlib import contextmanager

class Weather(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.temperature = ''
        self.forecast = ''
        self.location = ''
        self.currently = ''
        self.icon = ''
        self.icon_lookup = {
            '200': "assets/Storm.png",
            '201': "assets/Storm.png",
            '202': "assets/Rain.png",
            '230': "assets/Storm.png",
            '231': "assets/Storm.png",
            '232': "assets/Storm.png",
            '233': "assets/Hail.png",
            '300': "assets/Rain.png",
            '301': "assets/Rain.png",
            '302': "assets/Rain.png",
            '500': "assets/Rain.png",
            '501': "assets/Rain.png",
            '502': "assets/Rain.png",
            '511': "assets/Rain.png",
            '520': "assets/Rain.png",
            '521': "assets/Rain.png",
            '522': "assets/Rain.png",
            '600': "assets/Snow.png",
            '601': "assets/Snow.png",
            '602': "assets/Snow.png",
            '610': "assets/Snow.png",
            '611': "assets/Snow.png",
            '612': "assets/Snow.png",
            '621': "assets/Snow.png",
            '622': "assets/Snow.png",
            '623': "assets/Snow.png",
            '700': "assets/Haze.png",
            '711': "assets/Haze.png",
            '721': "assets/Haze.png",
            '731': "assets/Haze.png",
            '741': "assets/Haze.png",
            '751': "assets/Haze.png",
            '800': "assets/Sun.png",
            '800d': "assets/Sun.png",
            '800n': "assets/Moon.png",
            '801': "assets/Cloud.png",
            '802': "assets/PartlySunny.png",
            '803': "assets/PartlySunny.png",
            '802d': "assets/PartlySunny.png",
            '803d': "assets/PartlySunny.png",
            '802n': "assets/PartlyMoon.png",
            '803n': "assets/PartlyMoon.png",
            '804': "assets/Cloud.png",
            '900': "assets/Rain.png"
        }
        
        self.degreeFrm = Frame(self, bg='black')
        self.degreeFrm.pack(side=TOP, anchor=W)
        self.iconLbl = Label(self.degreeFrm, bg ="black")
        self.iconLbl.pack(side=LEFT, anchor=E, padx=20)
        
        self.temperatureLbl = Label(self.degreeFrm, font =('Helvetica',70), fg="white", bg="black")
        self.temperatureLbl.pack(side=TOP, anchor=W)
        
        self.currentlyLbl = Label(self.degreeFrm, font=('Helvetica',14), fg="white", bg="black")
        self.currentlyLbl.pack(side=RIGHT, anchor=N)
        self.get_weather()



    def get_weather(self):

        #Requesting data from api
        url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

        querystring = {"lon":"72.571365","lat":"23.022505","units":"M","lang":"en"}

        headers = {
            'x-rapidapi-key': "b9480bbd0dmsh8ce179da7a322e7p19cde9jsn65611d1d0648",
            'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        weather_obj = json.loads(response.text)
        data=weather_obj['data'][0]

        #setting values
        degree_sign = u'\N{DEGREE SIGN}'
        temperature = "%s%sC" % (str(int(data['temp'])),degree_sign)
        currently = "Feels like %s%sC\n%s\nHumidity: %s%%\nWind: %skm/h %s" % (str(int(data['app_temp'])), degree_sign,str(data['weather']['description']), str(int(data['rh'])), str(int(data['wind_spd'])),str(data['wind_cdir']))

        icon_id = str(data['weather']['code'])
        pod = str(data['pod'])

        icon = None

        if(icon_id=='800' or icon_id=='802' or icon_id=='803'):
            icon_id = str(icon_id + pod)

        if icon_id in self.icon_lookup:
            icon = self.icon_lookup[icon_id]

        if icon is not None:
                if self.icon != icon:
                    self.icon = icon
                    image = Image.open(icon)
                    image = image.resize((150, 150), Image.ANTIALIAS)
                    image = image.convert('RGB')
                    photo = ImageTk.PhotoImage(image)

                    self.iconLbl.config(image=photo)
                    self.iconLbl.image = photo
        else:
            # remove image
            self.iconLbl.config(image='')



        if self.currently != currently:
            self.currently = currently
            self.currentlyLbl.config(text=currently, justify="right")

        if self.temperature != temperature:
            self.temperature = temperature
            self.temperatureLbl.config(text=temperature)

        self.after(600000, self.get_weather)# called every 10 min




if __name__ == "__main__":
    tk = Tk()
    tk.configure(background="black")
    f = Frame(tk,background="black")
    f.pack()
    w = Weather(f)
    w.pack()
    tk.mainloop()

