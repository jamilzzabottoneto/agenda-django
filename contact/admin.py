from django.contrib import admin
from contact import models

# Register your models here.
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email',
    ordering = 'id',
    #list_filter = 'created_date, 
    search_fields = 'id', 
    list_per_page = 10
    list_max_show_all = 50
    list_editable = 'phone', 'email', 
    list_display_links = 'first_name', 'last_name', 