from django.contrib import admin
from polls.models import Questions, choice

# Register your models here.
admin.site.register((Questions, choice))