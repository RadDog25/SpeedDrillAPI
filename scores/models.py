from django.db import models

class Log(models.Model):
    name = models.CharField(max_length=20)
    score = models.PositiveIntegerField()
    time = models.FloatField()
    competing = models.BooleanField() #weather or not this was a competing quiz
    #log is a string of the 20 entry array containing an array of every questions results
    log = models.CharField(max_length=3000)

    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id={}_name={}_date={}".format(self.id, self.name, self.time_stamp)

'''

python manage.py makemigrations
python manage.py migrate

'''

##this is the key to be passed with the request
class Key(models.Model):
    key = models.CharField(max_length=100)

    time_stamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "id={}_key={}_date={}".format(self.id, self.key, self.time_stamp)

