from django.contrib import admin
from .models import category
# Register your models here.

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    search_fields=('title',)
    
admin.site.register(category, categoryAdmin)