from django.contrib import admin
from .models import *  #accessing the models file so that we register those models to the admin's darshboard.
# Register your models here.
admin.site.register(Stockx)
admin.site.register(Sales)
admin.site.register(Deffered_payments)