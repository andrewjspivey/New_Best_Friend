from django.contrib import admin

# Register your models here.

from .models import Dog
from .models import Provider

# Register your models here
admin.site.register(Dog)
admin.site.register(Provider)