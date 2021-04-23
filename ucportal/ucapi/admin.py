from django.contrib import admin
from ucportal.ucapi.models import Model, UESession, Object, Repository, UEFrameScenario

# Register your models here.
admin.site.register(Model)
admin.site.register(UESession)
admin.site.register(Object)
admin.site.register(Repository)
admin.site.register(UEFrameScenario)