from django.contrib import admin

from issuetracker.models import Type, Task, Status

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','summary', 'status', 'type','created_at','updated_at']
    list_filter = ['status','type', 'created_at']
    search_fields = ['summary']
    fields = ['summary','description' ,'status', 'type','created_at','updated_at']
    readonly_fields = ['created_at','updated_at']

class StatusAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class TypeAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Type, TypeAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)