from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserSignup)
admin.site.register(Event)
admin.site.register(Category)
admin.site.register(Booking)
