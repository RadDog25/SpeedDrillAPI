from operator import itemgetter
from django.http import JsonResponse
from .models import Log, Key
import json

from .utils import generateHighscores


def getHighscores(request):
    # scan the database for a key of the subitted value
    # if such a key exists, return the highscores, otherwise send an error
    API_KEY = request.GET.get('key')
    if Key.objects.filter(key=API_KEY):
        return JsonResponse({'highscores': generateHighscores.get()})

    return JsonResponse({'message': 'must provide a valid key'})


def postScore(request):
    data = (API_KEY, name, score, time, logStr) = (
        request.GET.get('key'),
        request.GET.get('name'),
        request.GET.get('score'),
        request.GET.get('time'),
        request.GET.get('log'),
    )
    if Key.objects.filter(key=API_KEY) and None not in data: #check that API is valid and all data is present
        # log = json.loads(logStr) #convert from string to dict if needed later
        #put game log into database
        Log.objects.create(
            name = name,
            score = score,
            time = time,
            competing = True,
            log = logStr,
        )
        return JsonResponse({'highscores': generateHighscores.get()}) ##return updated highscore

    return JsonResponse({'message': 'must post a valid key'})
