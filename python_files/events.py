from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
from gtts import gTTS
import playsound
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess

SCOPES = ['https://www.googleapis.com/auth/calendar']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

class Calendar():

    def __init__(self,voice_assistant):
        self.voice_assistant = voice_assistant

    def find(self, text):
        SERVICE = authenticate_google()

        CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]
        for phrase in CALENDAR_STRS:
            if phrase in text:
                date = self.get_date(text)
                if date:
                    self.get_events(date, SERVICE)
                else:
                    self.voice_assistant.speak("I don't understand")

        CREATE_STRS = ["create a event"]
        for phrase in CREATE_STRS:
            if phrase in text:
            
                self.voice_assistant.speak("What is the name of the event?")

                name = self.voice_assistant.google_get_audiospeech()

                date = self.get_date(text)
                if len(name) == 0:
                    name = "New"
                if date:
                    self.create_event(date, name, SERVICE)
                else:
                    self.voice_assistant.speak("I don't understand")

        NOTE_STRS = ["make a note", "write this down", "remember this"]
        for phrase in NOTE_STRS:
            if phrase in text:
                self.voice_assistant.speak("What would you like me to write down?")
                note_text = self.voice_assistant.google_get_audiospeech()
                note(note_text)
                self.voice_assistant.speak("I've made a note of that.")
                
    def get_date(self,text):
        text = text.lower()
        today = datetime.date.today()

        if text.count("today") > 0:
            return today

        day = -1
        day_of_week = -1
        month = -1
        year = today.year

        for word in text.split():
            if word in MONTHS:
                month = MONTHS.index(word) + 1
            elif word in DAYS:
                day_of_week = DAYS.index(word)
            elif word.isdigit():
                day = int(word)
            else:
                for ext in DAY_EXTENTIONS:
                    found = word.find(ext)
                    if found > 0:
                        try:
                            day = int(word[:found])
                        except:
                            pass

        # THE NEW PART STARTS HERE
        if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
            year = year + 1

        # This is slighlty different from the video but the correct version
        if month == -1 and day != -1:  # if we didn't find a month, but we have a day
            if day < today.day:
                month = today.month + 1
            else:
                month = today.month

        # if we only found a dta of the week
        if month == -1 and day == -1 and day_of_week != -1:
            current_day_of_week = today.weekday()
            dif = day_of_week - current_day_of_week

            if dif < 0:
                dif += 7
                if text.count("next") >= 1:
                    dif += 7

            return today + datetime.timedelta(dif)

        if day != -1:  # FIXED FROM VIDEO
            return datetime.date(month=month, day=day, year=year)

    def create_event(self,day, name, service):
        date = datetime.datetime.combine(day, datetime.datetime.min.time())
        end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
        utc = pytz.UTC
        date = date.astimezone(utc)
        end_date = end_date.astimezone(utc)

        if len(name) != 0:
            event = {
                "summary": f"{name}",
                "location": "Online",
                "description": "Demo",
                "colorId": 5,
                "start": {
                    "dateTime": f"{date.isoformat()}",
                    "timeZone": "Asia/Kolkata"
                },
                "end": {
                    "dateTime": f"{end_date.isoformat()}",
                    "timeZone": "Asia/Kolkata"
                },
                "recurrence": [
                    "RRULE:FREQ=DAILY;COUNT=1"
                ],
            }

            event = service.events().insert(calendarId='primary', body=event).execute()

            self.voice_assistant.speak("Event created")
            
    def get_events(self,day, service):
        # Call the Calendar API
        date = datetime.datetime.combine(day, datetime.datetime.min.time())
        end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
        utc = pytz.UTC
        date = date.astimezone(utc)
        end_date = end_date.astimezone(utc)

        events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(),
                                              timeMax=end_date.isoformat(),
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            self.voice_assistant.speak('No upcoming events found.')
        else:
            self.voice_assistant.speak(f"You have {len(events)} events on this day.")

            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
                start_time = str(start.split("T")[1].split("-")[0])
                if int(start_time.split(":")[0]) < 12:
                    start_time = start_time + "am"
                else:
                    start_time = str(int(start_time.split(":")[0]) - 12) + start_time.split(":")[1]
                    start_time = start_time + "pm"

                self.voice_assistant.speak(event["summary"] + " at " + start_time)

