from csv import list_dialects
from encodings import search_function
from django.contrib import admin
from jmespath import search
from main.models import Post,  Comment
# Register your models here.


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "content",
                    "created_at", "view_count", "writer")
    # list_editable =('content' , )
    list_filter = ("created_at", )
    search_fields = ('id', 'writer__username')
    search_help_text = "게시판 번호, 작성자 검색이 가능합니다."


admin.site.register(Comment)
