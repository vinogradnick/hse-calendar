import requests
from htmldom import htmldom
import downloader
import requests
import os
FILE_NAME = 'file.xlsx'

def download():
    # delete file
    path = os.getcwd() + "/" + FILE_NAME
    if os.path.isfile(path):
        os.remove(path)

    url = "http://students.perm.hse.ru/"
    dom = htmldom.HtmlDom(url+"timetable/")
    dom = dom.createDom()
    elem = dom.find("a[data-hse-file=XLS]").first()
    urlData = url+elem.attr("href")
    return DownloadFile(urlData)


def DownloadFile(url):
    file = requests.get(url)
    with open(FILE_NAME, 'wb') as binary:
        binary.write(file.content)
    if file.status_code == 200:
        return True
    return False
