import json_parser as jp
import excel_reader as excel
import event_creater as calendar
import downloader
import os
EXCEL_FILE = 'file.xlsx'


def main():
    if(downloader.download()):
        for x in (excel.get_all_lessons(EXCEL_FILE)):
            xEvent = x.__dict__()
            calendar.send_event(xEvent.get('name'), xEvent.get(
                'startTime'), xEvent.get('endTime'))
    else:
        print('error')


if __name__ == '__main__':
    main()
