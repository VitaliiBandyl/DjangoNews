from django.contrib import admin

from .models import Tag, Category, Post, Comment


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'poster']
    readonly_fields = ['poster']

