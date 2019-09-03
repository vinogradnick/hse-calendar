import requests 


def DownloadFile(url):
    file=requests.get(url)
    with open('file.xlsx','wb') as binary:
       binary.write(file.content)
    if file.status_code==200:
        return True
    return False