from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(Topic)

admin.site.register(WebPage)

admin.site.register(AccessRecord)


'''limeserver is used for seeig the data of the database(sqlite3)'''