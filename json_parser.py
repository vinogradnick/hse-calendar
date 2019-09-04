import json


def toJson(structure):

    response = json.dumps(toDictionary(structure),  indent=4)
    return response


def toDictionary(dataList):
    dataSet = []
    print(dataList)
    for data in dataList:
        if(data is not None):
            spl = data.split('\n\n')
            times = spl[1].split('-')
            dataSet.append(
                dict(numberLesson=spl[0], startTime=times[0], endTime=times[1]))
    return dataSet
