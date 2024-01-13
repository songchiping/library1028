from .models import Post
import django_filters

class Search(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = '__all__'