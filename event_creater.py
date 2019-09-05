from __future__ import print_function
import pickle
import os
import datetime

import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def send_event(msg, start_date, stop_date):
    def build_creds():
        SCOPES = ['https://www.googleapis.com/auth/calendar']
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
        return creds
    
    
    service = build('calendar', 'v3', credentials=build_creds())
    # events_result = service.events().list(calendarId='primary',
    #                                      singleEvents=True,
    #                                     orderBy='startTime').execute()
    # events = events_result.get('items', [])
    # print(events)
    if msg is not None:
        event = {
            'summary': msg,
            'start': {
                'dateTime': start_date,
                'timeZone': 'Asia/Yekaterinburg'
            },
            'end': {
                'dateTime': stop_date,
                'timeZone': 'Asia/Yekaterinburg'
            },
            #'attendees': [
            #    {'email': 'vinogradovnick32@gmail.com'}
            #],
            "reminders": {
                "useDefault": False,
                "overrides": [
                {
                    "method": "popup",
                    "minutes": 10
                }
                ]
            },
        }
    #event = service.events().insert(calendarId='primary', body=event).execute()


def main():
    send_event("ПЛАКСИН ЫЫЫ", '2019-09-04T11:30:00', '2019-09-04T12:50:00')


if __name__ == '__main__':
    main()
