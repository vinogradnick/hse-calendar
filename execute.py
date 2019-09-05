import json_parser as jp
import excel_reader as excel
import event_creater as calendar
import downloader
EXCEL_FILE = 'file.xlsx'

def main():
    if(downloader.download()):
        for x in (excel.get_all_lessons(EXCEL_FILE)):
            xEvent = x.__dict__()
            event_name = xEvent.get('name')
            calendar.send_event(event_name, xEvent.get(
                'startTime'), xEvent.get('endTime'))
            if (event_name is not None):
                print("event created " + xEvent.get('name'))
        print('success')
    else:
        print('error')


if __name__ == '__main__':
    main()
