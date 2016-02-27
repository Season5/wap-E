from django.contrib import admin

from .models import Top_spots
from .models import Popular
from .models import Content

# Register your models here.
admin.site.register(Top_spots)
admin.site.register(Popular)
admin.site.register(Content)
