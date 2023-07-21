from django.contrib import admin
from .models import Blog, Group, Topic

# Register your models here.
admin.site.register(Blog)
admin.site.register(Group)
admin.site.register(Topic)
