from operator import itemgetter
from django.http import JsonResponse
from .models import Log, Key

from .utils import generateHighscores


def getHighscores(request):
    #scan the database for a key of the subitted value
    #if such a key exists, return the highscores, otherwise send an error
    API_KEY = request.GET.get('key')
    if Key.objects.filter(key=API_KEY):
        return JsonResponse({'highscores': generateHighscores.get()})

    return JsonResponse({'message': 'must provide a valid key' })


def postScore(request):
    (API_KEY, log) = ( request.POST.get('key'), request.POST.get('log') )
    if Key.objects.filter(key=API_KEY):
        return JsonResponse({'message': log }) 


    return JsonResponse({'message': 'must post a valid key' })
