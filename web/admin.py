from website.web.views import signup
from django.contrib import admin
from .models import Signup, Language, Projects
# Register your models here.



admin.site.register(Projects)
admin.site.register(Signup)
admin.site.register(Language)