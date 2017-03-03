from operator import itemgetter
from .. import models


def sort(scores):  # takes in a list
    # this algorithm sorts with priority on highest score and next on lowest
    # time
    scores = sorted(scores, key=itemgetter('time'))
    scores = sorted(scores, key=itemgetter('score'), reverse=True)

    return scores

'''
def makeObjectList(model):
    print("hello from makeObjectList!")
    print("type", type(model))
    print("length", len(model))
    # this converts a model object to a list of objects to be used
    if type(model) is not list:
        print("not a list!")
        model = [ model ]
    objectList = []
    for object in model:
        objectList.append({
            'name': object.name,
            'score': object.score,
            'time': object.time,
            'id': object.id,  # this id will be used to determine which score matches the user
        })
    print("hello, objectList", objectList)

    return objectList
'''


def makeObject(model):
    return {
        'name': model.name,
        'score': model.score,
        'time': model.time,
        'id': model.id,  # this id will be used to determine which score matches the user
    }


'''
def getScores():

    highscores = []
    # make an array of score objects
    for object in models.Log.objects.filter(competing=True):
        highscores.append({
            'name': object.name,
            'score': object.score,
            'time': object.time,
            'id': object.id,  # this id will be used to determine which score matches the user
        })

    # this algorithm sorts with priority on highest score and next on lowest
    # time
    highscores = sorted(highscores, key=itemgetter('time'))
    highscores = sorted(highscores, key=itemgetter('score'), reverse=True)

    return highscores
'''
