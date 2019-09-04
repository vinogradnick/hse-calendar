import json
import models.schedule as scModel


def toJson(structure):

    response = json.dumps(toDictionary(structure),  indent=4)
    return response


def toDictionary(dataList):
    dataSet = []
    for data in dataList:
        try:
            model = scModel.Schedule.toSchedule(data)
            dataSet.append(model.toDict())
        except TypeError:
            print('err')
    return dataSet
