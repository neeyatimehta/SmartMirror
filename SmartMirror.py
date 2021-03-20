from tkinter import *
from _MirrorScreen import MirrorScreen
from _HomeScreen import HomeScreen
from _EntertainmentScreen import EntertainmentScreen
from _OfficeScreen import OfficeScreen
from _WeatherScreen import WeatherScreen
from _AppDrawer import AppDrawer
from _VoiceCommandScreen import VoiceCommandScreen
import speech_recognition as sr
import random
import vlc  
import pafy 
import time
import keyboard
from youtubesearchpython import VideosSearch



commandsList = ['What is the time?', 'How is the weather', 'what movies are playing?', 'list tv shows', 'what is in the news', 'go to office screen']


class SmartMirror:
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='black')
        self.frm = Frame(self.tk, background="black") #screen container
        self.frm.pack(side = TOP, fill=BOTH, expand = YES)
        self.screen = AppDrawer(self.frm) #display screen variable
        self.screen.pack(side = TOP, fill=BOTH, expand = YES)
        self.state = False #fullscreen toggle variable
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Key>", self.switch_screen)#switching screen
        self.onScreen='appdrawer'
        self.tk.bind("<space>",self.voice_command)

    def voice_command(self, event=None):
        #print("voice command called")
        r = sr.Recognizer()

        with sr.Microphone() as source:
            #print ('Listneing...')
            
            audio = r.listen(source)
            
            try:
                text = r.recognize_google(audio)
                command = format(text)
                #print(command)
               
                    
                if ('office' in command) or ('calender' in command) or ('event' in command) or ('task' in command):
                    for widget in self.frm.winfo_children():
                        widget.destroy()
                    self.screen = OfficeScreen(self.frm)
                    self.screen.pack(side = TOP, fill=BOTH, expand = YES)
                    self.onScreen='officescreen'
                    
                if ('play' in command):
                    movieName = command.replace("play","")
                    searchQuery = movieName+" Trailer"
                    videosSearch = VideosSearch(searchQuery)
                    info_dict = videosSearch.result()["result"][0]   # This will provide info for whole video

                    # url of the video 
                    url = info_dict["link"]

                    # creating pafy object of the video 
                    video = pafy.new(url)

                    # getting stream at index 0 
                    best = video.streams[0] 

                    # creating vlc media player object 
                    media = vlc.MediaPlayer(best.url) 
                    media.toggle_fullscreen()

                    # start playing video 
                    media.play()
                    start = time.time()

                    while True:
                        if((time.time() - start) < video.length):
                            if keyboard.is_pressed('n'):
                                media.stop()
                                break
                            else:
                                time.sleep(1) 
                        else:
                            media.stop()
                            break
                    
                elif ('home' in command) or ('news' in command) or ('headline' in command):
                    for widget in self.frm.winfo_children():
                        widget.destroy()
                    self.screen = HomeScreen(self.frm)
                    self.screen.pack(side = TOP, fill=BOTH, expand = YES)
                    self.onScreen='homescreen'

                elif ('black' in command) or ('mirror' in command) or ('time' in command) or ('bye' in command):
                    for widget in self.frm.winfo_children():
                        widget.destroy()
                    self.screen = BlackScreen(self.frm)
                    self.screen.pack(side = TOP, fill=BOTH, expand = YES)
                    self.onScreen='blackscreen'
                    
                elif ('entertainment' in command) or ('movie' in command) or ('tv show' in command):
                    for widget in self.frm.winfo_children():
                        widget.destroy()
                    self.screen = EntertainmentScreen(self.frm)
                    self.screen.pack(side = TOP, fill=BOTH, expand = YES)
                    self.onScreen='entertainmentscreen' 
                    
                elif ('weather' in command) or ('temperature' in command) or ('forecast' in command):
                    for widget in self.frm.winfo_children():
                        widget.destroy()
                    self.screen = WeatherScreen(self.frm)
                    self.screen.pack(side = TOP, fill=BOTH, expand = YES)
                    self.onScreen='weatherscreen'

                elif ('app' in command):
                    for widget in self.frm.winfo_children():
                        widget.destroy()
                    self.screen = AppDrawer(self.frm)
                    self.screen.pack(side = TOP, fill=BOTH, expand = YES)
                    self.onScreen='appdrawer'

                else:
                    c = random.choice(commandsList)
                    for widget in self.frm.winfo_children():
                        widget.destroy()
                    c_string = 'Not a valid command! Try saying: ' + c
                    self.screen = VoiceCommandScreen(self.frm, c_string)
                    self.screen.pack(side = TOP, fill=BOTH, expand = YES)

            except Exception as e:
                #print(e)
                for widget in self.frm.winfo_children():
                        widget.destroy()
                self.screen = VoiceCommandScreen(self.frm,'Unable to hear you! Try again!')
                self.screen.pack(side = TOP, fill=BOTH, expand = YES)
        
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
        
        #Weather screen
        elif choice == 'w':
            for widget in self.frm.winfo_children():
                widget.destroy()
            self.screen = WeatherScreen(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.onScreen='weatherscreen'
        
        #App Drawer
        if choice == 'a':
            for widget in self.frm.winfo_children():
                widget.destroy()
            self.screen = AppDrawer(self.frm)
            self.screen.pack(side = TOP, fill=BOTH, expand = YES)
            self.onScreen='appdrawer'

    #Toggle fullscreen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"


#main function
if __name__ == "__main__":
    window = SmartMirror()
    window.tk.mainloop()


    
