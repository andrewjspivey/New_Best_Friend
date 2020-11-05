from django.contrib import admin

# Register your models here.

from .models import Dog
from .models import Provider
from .models import User
from .models import RegUser

# Register your models here
admin.site.register(Dog)
admin.site.register(Provider)
admin.site.register(User)
admin.site.register(RegUser)