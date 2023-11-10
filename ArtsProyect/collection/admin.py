from django.contrib import admin
from .models import Collection
from collection.models import Artist, Genre, Style, Period, Artwork

admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Style)
admin.site.register(Period)
admin.site.register(Artwork)
admin.site.register(Collection)


# Register your models here.
