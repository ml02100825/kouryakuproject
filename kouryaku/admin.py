from django.contrib import admin

from .models import Character, Map, Lineups
from .models import Comments
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links= ('id', 'title')
class MapAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links= ('id', 'title')
class LineupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links= ('id', 'title')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links= ('id', 'user')
admin.site.register(Character, CharacterAdmin)
admin.site.register(Map, MapAdmin)
admin.site.register(Lineups, LineupsAdmin)

admin.site.register(Comments, CommentsAdmin)