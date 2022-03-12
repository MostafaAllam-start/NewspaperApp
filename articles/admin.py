from django.contrib import admin
from .models import Article, Comment
# Register your models here.
admin.site.register(Comment)

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]