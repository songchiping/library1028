from django.contrib import admin
from mysite.models import Post
# from mysite.models import NewTable

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug', 'body' ,'picture', 'release_date','choose')
    
admin.site.register(Post,PostAdmin)

# admin.site.register(Product)