from django.contrib import admin
from myblog.models import Topmenu,Banner,Aritical
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class Aritical_summer(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields =('centent',)


admin.site.register(Topmenu)
admin.site.register(Banner)
admin.site.register(Aritical, Aritical_summer)