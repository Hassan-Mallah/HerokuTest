from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Greeting)
admin.site.register(SearchResult)
admin.site.register(SearchAreas)
admin.site.register(TelegramUser)