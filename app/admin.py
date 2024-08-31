from django.contrib import admin
from .models import (
    Contact,
    OrgType,
    Client,
    Year,
    Period,
    Task,
    Status,
    Employee,
    Assignment,
)


admin.site.site_header = "Robbin"
admin.site.site_title = "Robbin"
admin.site.index_title = "Welcome to the Robbin"


admin.site.register(Contact)
admin.site.register(OrgType)
admin.site.register(Client)
admin.site.register(Year)
admin.site.register(Period)
admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Employee)
admin.site.register(Assignment)
