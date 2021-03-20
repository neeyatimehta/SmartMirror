from __future__ import print_function
from tkinter import *
import requests
import json
from datetime import datetime
from datetime import timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


from PIL import Image, ImageTk
from contextlib import contextmanager

xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18

SCOPES = ['https://www.googleapis.com/auth/tasks.readonly']


class Tasks(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.title = 'Tasks'
        self.titleLbl = Label(self, text=self.title, font=('Helvetica', medium_text_size, 'bold'), fg="white", bg="black")
        self.titleLbl.pack(side=TOP, anchor=W)

        self.taskToDoContainer = Frame(self, bg='black')
        self.taskToDoContainer.pack(side=LEFT, anchor = N)
        self.get_todo_tasks()

    def get_todo_tasks(self):
        for widget in self.taskToDoContainer.winfo_children():
            widget.destroy()
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token_task.pickle'):
            with open('token_task.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials_task.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token_task.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('tasks', 'v1', credentials=creds)

        # Call the Tasks API
        results = service.tasks().list(tasklist='MDM5MzY1OTQyMTY4NDUwMTk3ODY6MDow', maxResults=10).execute()
        items = results.get('items', [])
        if not items:
            task_todo = ToDo(self.taskToDoContainer,'No task lists found.')
            task_todo.pack(side=TOP, anchor=W,pady=10)

        
        for item in items:
            task_todo = ToDo(self.taskToDoContainer,item['title'])
            task_todo.pack(side=TOP, anchor=W)
        
        self.after(60000, self.get_todo_tasks)


class ToDo(Frame):
    def __init__(self, parent, todo="Event 1"):
        Frame.__init__(self, parent, bg='black')
        img = Image.open("assets/task.jpg")
        img = img.resize((25,25), Image.ANTIALIAS)
        img = img.convert('RGB')

        photo = ImageTk.PhotoImage(img)

        self.iconLabel = Label(self, bg='black',image=photo)
        self.iconLabel.image = photo
        self.iconLabel.pack(side=LEFT,anchor=N)
        
        self.toDo = todo
        self.toDoLabel = Label(self, bg='black',text=self.toDo,font=('Helvetica', 18),fg="white")
        self.toDoLabel.pack(side=LEFT, anchor=N)

    
        
if __name__ == "__main__":
    tk = Tk()
    tk.configure(background="black")
    f = Frame(tk,background="black")
    f.pack()
    w = Tasks(f)
    w.pack()
    tk.mainloop()

        
