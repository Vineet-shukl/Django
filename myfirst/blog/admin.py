from django.contrib import admin
from blog.models import Users, Posts


admin.site.register(Users)  # Assuming you have a model to register

# Register your models here.
admin.site.register(Posts)