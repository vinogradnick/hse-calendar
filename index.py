from htmldom import htmldom
import downloader,requests
url="http://students.perm.hse.ru/"

dom = htmldom.HtmlDom( url+"timetable/" )
dom=dom.createDom()

elem=dom.find("a[data-hse-file=XLS]").first()
print(elem.html())

urlData=url+elem.attr("href")

downloader.DownloadFile(urlData)