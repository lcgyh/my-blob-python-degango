from django.contrib import admin
from .models import Articel
# Register your models here.
class ArticelAdmin(admin.ModelAdmin):
    list_display=("title","content","pub_time")
    list_filter=("pub_time",)

admin.site.register(Articel,ArticelAdmin)