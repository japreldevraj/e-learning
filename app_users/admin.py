from django.contrib import admin
from app_users.models import UserProfileInfo,Event
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Event)
