from operator import itemgetter
from .. import models


def sort(scores):  # takes in a list
    # this algorithm sorts with priority on highest score and next on lowest
    # time
    scores = sorted(scores, key=itemgetter('time'))
    scores = sorted(scores, key=itemgetter('score'), reverse=True)

    return scores


def makeObject(model):
    return {
        'name': model.name,
        'score': model.score,
        'time': model.time,
        'id': model.id,  # this id will be used to determine which score matches the user
    }
