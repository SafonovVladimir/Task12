from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

admin.site.site_title = 'Управление Djangogram'
admin.site.site_header = 'Управление Djangogram'


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'e_mail', 'birthday', 'gender', 'bio', 'get_photo')
    list_display_links = ('id', 'user', 'full_name')
    search_fields = ('user', 'full_name')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '---'

    get_photo.short_description = 'Миниатюра'


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at', 'updated_at', 'num_of_likes')
    list_display_links = ('id', 'author')
    search_fields = ('user',)
    save_on_top = True


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'image', 'get_photo')
    list_display_links = ('id', 'post')
    search_fields = ('post',)
    save_on_top = True
    fields = ('post', 'image', 'get_photo')
    readonly_fields = ('get_photo',)

    def get_photo(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return '---'

    get_photo.short_description = 'Миниатюра'


class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post')
    list_display_links = ('id', 'user')
    search_fields = ('title',)
    save_on_top = True


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Tag)
admin.site.register(Like, LikeAdmin)
