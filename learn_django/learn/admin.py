from django.contrib import admin
from learn.models import Myapp
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
  list_display=("icon", "title","des")

admin.site.register(Myapp,ServiceAdmin)