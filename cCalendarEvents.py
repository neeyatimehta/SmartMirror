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



xlarge_text_size = 94
large_text_size = 48
medium_text_size = 28
small_text_size = 18

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


class CalendarEvents(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, bg='black')
        self.title = 'Calendar Events'
        self.calendarLbl = Label(self, text=self.title, font=('Helvetica', 30, 'bold'), fg="white", bg="black")
        self.calendarLbl.pack(side=TOP, anchor=W)
        self.calendarEventContainer = Frame(self, bg='black')
        self.calendarEventContainer.pack(side=LEFT, anchor = N)
        self.get_events()

    def get_events(self):
        for widget in self.calendarEventContainer.winfo_children():
            widget.destroy()
        creds = None
        # The file token_cal.pickle stores the user's access and refresh token_cals, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        maxTime = datetime.utcnow() + timedelta(days=30)
        maxTimeS = maxTime.isoformat() + 'Z'
        calList_result = service.calendarList().list().execute()
        calList = calList_result.get('items', [])

        i=0

        
        for cal in calList:
            
            calID = cal['id']
            
            events_result = service.events().list(calendarId=calID, timeMin=now,
                                                timeMax=maxTimeS, singleEvents=True,
                                                orderBy='startTime').execute()
            events = events_result.get('items', [])

            
            for event in events:
                if i>=5:
                    break
                i += 1
                event_name = event['summary']
                dateTime = event['start'].get('dateTime')
                if dateTime == None:
                    dateTime = event['start'].get('date')
                    dateTimeObject = datetime.strptime(dateTime, "%Y-%m-%d")
                    event_date = dateTimeObject.strftime("%d")
                    event_month = dateTimeObject.strftime("%b")
                    event_duration = dateTimeObject.strftime("%a")
                else:
                    dateTimeObject = datetime.strptime(dateTime, "%Y-%m-%dT%H:%M:%S%z")
                    
                    endDateTime = event['end'].get('dateTime')
                    endDateTimeObject = datetime.strptime(endDateTime, "%Y-%m-%dT%H:%M:%S%z")
                    
                    startTime = dateTimeObject.strftime("%I:%M %p")
                    endTime = endDateTimeObject.strftime("%I:%M %p")
                    event_date = dateTimeObject.strftime("%d")
                    event_month = dateTimeObject.strftime("%b")
                    event_duration = dateTimeObject.strftime("%a") + ", "+ startTime + " - " + endTime
                calendar_event = CalendarEvent(self.calendarEventContainer, event_name, event_date, event_month, event_duration)
                calendar_event.pack(side=TOP, anchor=W,pady=10)
        
        self.after(60000, self.get_events)            



class CalendarEvent(Frame):
    def __init__(self, parent, event_name="Event 1", event_date = "00", event_month = "MON", event_duration = "All Day"):
        Frame.__init__(self, parent, bg='black')
        self.dateFrm = Frame(self, bg='black')
        self.dateFrm.pack(side=LEFT, anchor=W)

        self.eventDate = event_date
        self.eventDateLbl = Label(self.dateFrm, text=self.eventDate, font=('Helvetica', small_text_size), fg = "white" , bg = "black")
        self.eventDateLbl.pack(side=TOP, anchor=W)

        self.eventMonth = event_month
        self.eventMonthLbl = Label(self.dateFrm, text=self.eventMonth, font=('Helvetica', small_text_size), fg = "white" , bg = "black")
        self.eventMonthLbl.pack(side=TOP, anchor=W)
    

        self.evtFrm = Frame(self, bg='black', padx=10)
        self.evtFrm.pack(side=RIGHT, anchor=CENTER)

        self.eventName = event_name
        self.eventNameLbl = Label(self.evtFrm, text=self.eventName, font=('Helvetica', small_text_size), fg="white", bg="black")
        self.eventNameLbl.pack(side=TOP, anchor=W)
        
        self.eventDuration = event_duration
        self.eventDurationLbl = Label(self.evtFrm, text=self.eventDuration, font=('Helvetica', 15), fg="white", bg="black")
        self.eventDurationLbl.pack(side=TOP, anchor=W)
    
if __name__ == "__main__":
    tk = Tk()
    tk.configure(background="black")
    f = Frame(tk,background="black")
    f.pack()
    w = CalendarEvents(f)
    w.pack()
    tk.mainloop()
        
