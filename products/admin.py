from django.contrib import admin
from .models import Product


# class CommentInline(admin.TabularInline):
#     model = Comment
#     fields = ['body', 'product', 'user', 'recommend', 'publish', 'stars', ]
#     extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'price',
                    # 'size',
                    # 'category',
                    # 'available',
                    # 'stock',
                    # 'release',
                    # 'datetime_created',
                    # 'datetime_modified',
                    )
    # inlines = [
    #     CommentInline,
    # ]


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['body', 'user', 'recommend', 'publish', 'stars', ]
