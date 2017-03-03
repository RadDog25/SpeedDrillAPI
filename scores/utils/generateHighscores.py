from operator import itemgetter
from .. import models


def get():

    highscores = []
    # make an array of score objects
    for object in models.Log.objects.filter(competing=True):
        highscores.append({
            'name': object.name,
            'score': object.score,
            'time': object.time,
            'id': object.id, #this id will be used to determine which score matches the user
        })

    # this algorithm sorts with priority on highest score and next on lowest
    # time
    highscores = sorted(highscores, key=itemgetter('time'))
    highscores = sorted(highscores, key=itemgetter('score'), reverse=True)

    return highscores