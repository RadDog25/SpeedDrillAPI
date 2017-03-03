from operator import itemgetter
from django.http import JsonResponse
from .models import Log, Key
import json

from .utils import helpers

def postName(request):
    data = (API_KEY, playerId, name) = (
        request.GET.get("key"),
        request.GET.get("playerId"),
        request.GET.get("name")
        )
    #if we get all our data then make name change
    if Key.objects.filter(key=API_KEY) and None not in data:
        playerModel = Log.objects.filter(id=playerId)[0]
        #cant have 'You'
        if playerModel and name != "You":
            playerModel.name = name
            return JsonResponse({'message': 'success!'})

    return JsonResponse({'message': 'failure! could not match playerId!'})

def postScore(request):
    data = (API_KEY, name, score, time, logStr) = (
        request.GET.get('key'),
        request.GET.get('name', 'You'),
        request.GET.get('score'),
        request.GET.get('time'),
        request.GET.get('log'),
    )
    # check that API is valid and all data is present
    if Key.objects.filter(key=API_KEY) and None not in data:
        # log = json.loads(logStr) #convert from string to dict if needed later
        # put game log into database
        Log.objects.create(
            name=name,
            score=score,
            time=time,
            competing=True,
            log=logStr,
        )

        # next get players model
        playerModel = Log.objects.filter(competing=True).order_by('-id')[0]
        # then conver to an object
        playerObject = helpers.makeObject(playerModel)
        # then grab playerId
        playerId = playerObject['id']

        scoreObjects = []
        for model in Log.objects.filter(competing=True).exclude(name='You'):
            scoreObjects.append(helpers.makeObject(model))


        # now combine add the player object to the score objects and sort
        scoreObjects.append(playerObject)
        # finally sort our list
        scoreObjects = helpers.sort(scoreObjects)

        return JsonResponse({
            'playerId': playerId,
            'scores': scoreObjects,
        })

    return JsonResponse({'message': 'must post a valid key'})
