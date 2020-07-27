from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']  # 제목 부분에 링크 걸리게 함.
    search_fields = ['title']  # 검색에 제목 치면 해당 게시글 나오도록.