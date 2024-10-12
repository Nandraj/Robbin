from django.contrib import admin

from .models import OrgType, Year, Period, Task, Status

admin.site.site_header = "Robbin"
admin.site.site_title = "Robbin"
admin.site.index_title = "Welcome to the Robbin"

admin.site.register(OrgType)
admin.site.register(Year)
admin.site.register(Period)
admin.site.register(Task)
admin.site.register(Status)
