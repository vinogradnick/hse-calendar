import requests
from htmldom import htmldom
import downloader
import requests


def download():
    url = "http://students.perm.hse.ru/"
    dom = htmldom.HtmlDom(url+"timetable/")
    dom = dom.createDom()
    elem = dom.find("a[data-hse-file=XLS]").first()
    urlData = url+elem.attr("href")
    return DownloadFile(urlData)


def DownloadFile(url):
    file = requests.get(url)
    with open('file.xlsx', 'wb') as binary:
        binary.write(file.content)
    if file.status_code == 200:
        return True
    return False
