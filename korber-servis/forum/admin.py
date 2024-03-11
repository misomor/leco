# Register your models here.
from django.contrib import admin
from .models import Category, Document, Post, Comment


class DocumentInline(admin.TabularInline):
    model = Document
    fk_name = 'pdfFile'
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', '_documents')
    inlines = [DocumentInline]

    def _documents(self,obj):
        return obj.documents.all()
    

admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    list_display = ('category','content', 'author','closed_comments')

admin.site.register(Post, PostAdmin)