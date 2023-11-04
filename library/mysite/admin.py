from django.contrib import admin
from mysite.models import Post,Product
# from mysite.models import NewTable
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug', 'release_date')
    
admin.site.register(Post,PostAdmin)
admin.site.register(Product)
# admin.site.register(Product)