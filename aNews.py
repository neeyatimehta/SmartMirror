from tkinter import *
import requests
import feedparser

from PIL import Image, ImageTk

class News(Frame):
    def __init__(self, parent, *args, **kwargs):

        #Displays Title for News
        Frame.__init__(self, parent, *args, **kwargs)
        self.config(bg='black')
        self.title = 'News'
        self.newsLabel1 = Label(self, text=self.title,font=('Helvetica',30),fg="white",bg="black")
        self.newsLabel1.pack(side=TOP, anchor=W)

        #Frame for display News Headlines
        self.headlineContainer = Frame(self,bg="black")
        self.headlineContainer.pack(side=TOP)
        self.getHeadlines()

    
    def getHeadlines(self):

        #destroys all children in Frame
        for widget in self.headlineContainer.winfo_children():
            widget.destroy()

        #Fetches headlines from google news
        headlines_url = "https://news.google.com/news?ned=in&output=rss"
        feed = feedparser.parse(headlines_url)

        for post in feed.entries[0:5]:
            headline = NewsHeadline(self.headlineContainer, post.title)
            headline.pack(side=TOP, anchor=W)
        self.after(600000, self.getHeadlines)#refreshes every 10min

        
#Template for display News Headlines
class NewsHeadline(Frame):
    def __init__(self, parent, event_name):
        Frame.__init__(self, parent,bg="black")
        img = Image.open("assets/Newspaper.png")
        img = img.resize((25,25), Image.ANTIALIAS)
        img = img.convert('RGB')

        photo = ImageTk.PhotoImage(img)

        self.iconLabel = Label(self, bg='black',image=photo)
        self.iconLabel.image = photo
        self.iconLabel.pack(side=LEFT,anchor=N)

        self.eventName = event_name
        self.eventNameLabel = Label(self, bg='black',text=self.eventName, wraplength=1000, justify="left",font=('Helvetica', 18),fg="white")
        self.eventNameLabel.pack(side=LEFT, anchor=N)


if __name__ == "__main__":
    tk = Tk()
    tk.configure(background="black")
    f = Frame(tk,background="black")
    f.pack()
    w = News(f)
    w.pack()
    tk.mainloop()


