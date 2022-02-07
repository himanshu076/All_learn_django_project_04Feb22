'''Check Django version using_code'''
# import django
# print(django.get_version())

# ************************************************************
'''CHANGE THE VALUE OF TIME_ZONE IN SETTINGS.PY TO A VALID TIME ZONE'''
# import pytz
# timezones = pytz.all_timezones
# print(timezones)
import datetime

from polls.models import Questions
print(datetime.datetime.now())


# Question - difference b/w & checvk type
# user = user.object.all()
# user = user.object.get(name="himanhu")
# user = user.object.all().filter(name="himanhu")

