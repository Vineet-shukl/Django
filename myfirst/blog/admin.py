from django.contrib import admin
from blog.models import Users, Posts,Post


admin.site.register(Users)  # Assuming you have a model to register

# Register your models here.
admin.site.register(Posts)
admin.site.register(Post)