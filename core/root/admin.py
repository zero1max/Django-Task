from django.contrib import admin
from .models import Jobs

# Register your models here.
class JobAwwdmin(admin.ModelAdmin):
    list_display = ['title', 'time', 'company', 'country']

admin.site.register(Jobs, JobAdmin)