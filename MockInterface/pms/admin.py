from django.contrib import admin

# Register your models here.
from pms import models
admin.site.register(models.MockOption)
admin.site.register(models.ApiDetail)

