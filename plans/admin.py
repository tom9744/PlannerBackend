from django.contrib import admin

from .models import Tag, Plan, BucketList


class BucketListAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = [
        'id',
        'title',
        'is_complete',
    ]

# Register your models here.
admin.site.register(Tag)
admin.site.register(Plan)
admin.site.register(BucketList, BucketListAdmin)