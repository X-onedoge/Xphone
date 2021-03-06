from django.contrib import admin
from blog.models import *
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js'
        )


admin.site.register(News)
admin.site.register(Comment)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Video)
admin.site.register(Category)
admin.site.register(ProPic)
admin.site.register(Picture_details)
admin.site.register(Picture2)

