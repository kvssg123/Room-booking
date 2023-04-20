from django.contrib import admin
from book.models import Room

# Register your models here.
#admin.site.register(Room)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','type','available_count','rent_per_day')
    list_filter=['type','id']
    ordering = ['available_count']
    actions=['fun']
    @admin.action(description='Increase rommcount by 1')
    def fun(self,request,queryset):
        queryset.update(available_count=10)
admin.site.register(Room,UserAdmin)

