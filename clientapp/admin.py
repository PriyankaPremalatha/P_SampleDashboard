from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.TicketRegister)
admin.site.register(models.TicketCreation)
admin.site.register(models.OrgInsertion)