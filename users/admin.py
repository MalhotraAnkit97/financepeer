from django.contrib import admin
from .models import user
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    fields = ['UserID','id','title','body']


admin.site.register(user,UserAdmin)
