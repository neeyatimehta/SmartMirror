from tkinter import *
import requests
import json
from datetime import datetime

from PIL import Image, ImageTk
from contextlib import contextmanager

class Shows(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.config(bg='black')
        self.title = 'Trending Shows'
        self.titleLbl = Label(self, text=self.title,font=('Helvetica', 30,'bold'),fg="white",bg="black")
        self.titleLbl.pack(side=TOP, anchor=W)

        self.showContainer = Frame(self,bg="black")
        self.showContainer.pack(side=TOP)
        self.getShows()

    def getShows(self):
        #destroys all children in Frame
        for widget in self.showContainer.winfo_children():
            widget.destroy()
        #Calling genre and movie api
        response = requests.get("https://api.themoviedb.org/3/trending/tv/week?api_key=3eb0a780a2bb4ae20df35401d72271d2")
        response_genres=requests.get("https://api.themoviedb.org/3/genre/tv/list?api_key=3eb0a780a2bb4ae20df35401d72271d2&language=en-US")

        genre_obj = json.loads(response_genres.text)
        genre_lookup = genre_obj['genres']

        show_obj = json.loads(response.text)
        shows = show_obj['results']
        show_count=0
        for show in shows:
            if show_count >= 4:
                break
            #Show Details
            show_title = show['name']
            show_ratings = show['vote_average']
            show_id = show['id']

            #Formating Air Date
            show_air_date = show['first_air_date']
            dateTimeObject = datetime.strptime(show_air_date, "%Y-%m-%d")
            air_date = dateTimeObject.strftime("%d %b, %Y")

            #Getting Genre names
            show_genre_ids =show['genre_ids']
            show_genres="|"
            for genre_id in show_genre_ids:
                for genre in genre_lookup:
                    if genre['id']==genre_id:
                        show_genres += " " + str(genre['name']) + " |"

            #Getting Watch Providers
            watch_provider_request_string = "https://api.themoviedb.org/3/tv/"+str(show_id)+"/watch/providers?api_key=3eb0a780a2bb4ae20df35401d72271d2"
            response_watch_providers = requests.get(watch_provider_request_string)
            watch_provider_obj = json.loads(response_watch_providers.text)
            watch_provider_result = watch_provider_obj['results']
            watch_provider_list='Available on |'
            if("IN" in watch_provider_result):
                show_count += 1
                #print(str(i) + ". "+ str(movie_id) +" Title: " + movie_title + " Rating: " + str(movie_ratings)+ " Release Date: "+release_date+"\n")
                #print("movie genres: "+ str(movie_genres))
                if("flatrate" in watch_provider_result["IN"]):
                    watch_providers = watch_provider_result["IN"]["flatrate"]
                    for provider in watch_providers:
                        watch_provider_list += " " + provider['provider_name'] + " |"
                        #print(provider['provider_name'])
                        
                if("ads" in watch_provider_result["IN"]):
                    watch_providers = watch_provider_result["IN"]["ads"]
                    for provider in watch_providers:
                        watch_provider_list += " " + provider['provider_name'] + " |"
                        #print(provider['provider_name'])

                elif("buy" in watch_provider_result["IN"] or "rent" in watch_provider_result["IN"]):
                    watch_provider_list = "Available for rent or purchase online"
                    #print("Available for rent or purchase online")
                showFrm = Show(self.showContainer, show_title, show_ratings, air_date, show_genres, watch_provider_list)
                showFrm.pack(side=TOP, anchor=W, pady=10)
        self.after(864000, self.getShows)


class Show(Frame):
    def __init__(self, parent, show_title, show_ratings, air_date, show_genres, watch_provider_list):
        Frame.__init__(self, parent,bg="black")
        img = Image.open("assets/show.png")
        img = img.resize((100,100), Image.ANTIALIAS)
        img = img.convert('RGB')

        photo = ImageTk.PhotoImage(img)

        self.iconLabel = Label(self, bg='black',image=photo)
        self.iconLabel.image = photo
        self.iconLabel.pack(side=LEFT,anchor=CENTER)

        self.showDetailContainer = Frame(self, bg='black')
        self.showDetailContainer.pack(side=LEFT, anchor=N)


        self.showTitle = show_title
        self.showTitleLbl = Label(self.showDetailContainer,text=self.showTitle,font=('Helvetica', 15),fg="white",bg="black")
        self.showTitleLbl.pack(side=TOP, anchor=W)

        self.showRatings = str(show_ratings)
        self.showRatingsLbl = Label(self.showDetailContainer,text=("Rating: "+self.showRatings),font=('Helvetica', 10),fg="white",bg="black")
        self.showRatingsLbl.pack(side=TOP, anchor=W)
        
        self.airDate = air_date
        self.airDateLbl = Label(self.showDetailContainer,text=("Aired on: "+self.airDate),font=('Helvetica', 10),fg="white",bg="black")
        self.airDateLbl.pack(side=TOP, anchor=W)

        self.showGenres = show_genres
        self.showGenresLbl = Label(self.showDetailContainer,text=self.showGenres,font=('Helvetica', 10),fg="white",bg="black")
        self.showGenresLbl.pack(side=TOP, anchor=W)

        self.watchProviderList = watch_provider_list
        self.watchProviderListLbl = Label(self.showDetailContainer,text=self.watchProviderList,font=('Helvetica', 10),fg="white",bg="black")
        self.watchProviderListLbl.pack(side=TOP, anchor=W)

if __name__ == "__main__": 
    tk = Tk()
    tk.configure(background="black")
    f = Frame(tk,background="black")
    f.pack()
    news = Shows(f)
    news.pack()
    tk.mainloop()        
