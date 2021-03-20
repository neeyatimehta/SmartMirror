from tkinter import *
import requests
import json
from datetime import datetime

from PIL import Image, ImageTk
from contextlib import contextmanager

class Movies(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.config(bg='black')
        self.title = 'Trending Movies'
        self.titleLbl = Label(self, text=self.title,font=('Helvetica', 30,'bold'),fg="white",bg="black")
        self.titleLbl.pack(side=TOP, anchor=W)

        self.movieContainer = Frame(self,bg="black")
        self.movieContainer.pack(side=TOP)
        self.getMovies()

    def getMovies(self):
        #destroys all children in Frame
        for widget in self.movieContainer.winfo_children():
            widget.destroy()
        #Calling genre and movie api
        response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=3eb0a780a2bb4ae20df35401d72271d2&language=en-US&page=1")
        response_genres=requests.get("https://api.themoviedb.org/3/genre/movie/list?api_key=3eb0a780a2bb4ae20df35401d72271d2&language=en-US")

        genre_obj = json.loads(response_genres.text)
        genre_lookup = genre_obj['genres']

        movie_obj = json.loads(response.text)
        movies = movie_obj['results']
        movie_count=0
        for movie in movies:
            if movie_count >= 4:
                break
            #Movie Details
            movie_title = movie['original_title']
            movie_ratings = movie['vote_average']
            movie_id = movie['id']

            #Formating Release Date
            movie_realease_date = movie['release_date']
            dateTimeObject = datetime.strptime(movie_realease_date, "%Y-%m-%d")
            release_date = dateTimeObject.strftime("%d %b, %Y")

            #Getting Genre names
            movie_genre_ids =movie['genre_ids']
            movie_genres="|"
            for genre_id in movie_genre_ids:
                for genre in genre_lookup:
                    if genre['id']==genre_id:
                        movie_genres += " " + str(genre['name']) + " |"

            #Getting Watch Providers
            watch_provider_request_string = "https://api.themoviedb.org/3/movie/"+str(movie_id)+"/watch/providers?api_key=3eb0a780a2bb4ae20df35401d72271d2"
            response_watch_providers = requests.get(watch_provider_request_string)
            watch_provider_obj = json.loads(response_watch_providers.text)
            watch_provider_result = watch_provider_obj['results']
            watch_provider_list='Available on |'
            if("IN" in watch_provider_result):
                movie_count += 1
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
                movieFrm = Movie(self.movieContainer, movie_title, movie_ratings, release_date, movie_genres, watch_provider_list)
                movieFrm.pack(side=TOP, anchor=W, pady=10)
        self.after(864000, self.getMovies)


class Movie(Frame):
    def __init__(self, parent,  movie_title, movie_ratings, release_date, movie_genres, watch_provider_list):
        Frame.__init__(self, parent,bg="black")
        img = Image.open("assets/movie.png")
        img = img.resize((100,100), Image.ANTIALIAS)
        img = img.convert('RGB')

        photo = ImageTk.PhotoImage(img)

        self.iconLabel = Label(self, bg='black',image=photo)
        self.iconLabel.image = photo
        self.iconLabel.pack(side=LEFT,anchor=CENTER)

        self.movieDetailContainer = Frame(self, bg='black')
        self.movieDetailContainer.pack(side=LEFT, anchor=N)


        self.movieTitle = movie_title
        self.movieTitleLbl = Label(self.movieDetailContainer,text=self.movieTitle,font=('Helvetica', 15),fg="white",bg="black")
        self.movieTitleLbl.pack(side=TOP, anchor=W)

        self.movieRatings = str(movie_ratings)
        self.movieRatingsLbl = Label(self.movieDetailContainer,text=("Rating: "+self.movieRatings),font=('Helvetica', 10),fg="white",bg="black")
        self.movieRatingsLbl.pack(side=TOP, anchor=W)
        
        self.releaseDate = release_date
        self.releaseDateLbl = Label(self.movieDetailContainer,text=("Released on: "+self.releaseDate),font=('Helvetica', 10),fg="white",bg="black")
        self.releaseDateLbl.pack(side=TOP, anchor=W)

        self.movieGenres = movie_genres
        self.movieGenresLbl = Label(self.movieDetailContainer,text=self.movieGenres,font=('Helvetica', 10),fg="white",bg="black")
        self.movieGenresLbl.pack(side=TOP, anchor=W)

        self.watchProviderList = watch_provider_list
        self.watchProviderListLbl = Label(self.movieDetailContainer,text=self.watchProviderList,font=('Helvetica', 10),fg="white",bg="black")
        self.watchProviderListLbl.pack(side=TOP, anchor=W)

if __name__ == "__main__": 
    tk = Tk()
    tk.configure(background="black")
    f = Frame(tk,background="black")
    f.pack()
    w = Movies(f)
    w.pack()
    tk.mainloop()

