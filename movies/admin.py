from django.contrib import admin

# Register your models here.
from .models import Movie
from .models import Cast
from .models import Director
from .models import Genre

admin.site.register(Movie)
admin.site.register(Cast)
admin.site.register(Director)
admin.site.register(Genre)