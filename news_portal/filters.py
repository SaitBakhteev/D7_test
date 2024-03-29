from django_filters import FilterSet, CharFilter, NumberFilter
from .models import Post


class PostFilter(FilterSet):
    search_title = CharFilter(lookup_expr='iregex', label='Название', field_name='title' )

    # class Meta:
    #     model = Post
    #     fields = {'title': ['icontains'],
    #               'author__user__username': ['icontains'],
    #               'raiting': ['lt'],
    #               'create_time': ['gte'],
    #               'content': ['icontains'],
    #     }
