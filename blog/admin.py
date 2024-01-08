from django.contrib import admin
from .models import Article, Person
from django.contrib import messages


# @admin.action(description='به نمایش در آوردن مقالات انتخاب شده')
# def make_article_published(self, request, queryset):
#     updated = queryset.update(is_show=True)
#     self.message_user(request, f'{updated} تا مقاله به نمایش در آورده شدند', messages.SUCCESS)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_date', 'is_show')
    search_fields = ['title', 'text']
    list_editable = ['is_show']
    list_filter = ['is_show', 'author']
    empty_value_display = 'No data'
    actions = ['make_article_published']
    prepopulated_fields = {'text': ['title']}
    date_hierarchy = 'created_date'
    ordering = ['title']
    fieldsets = [
        (
            'Article Info',
            {
                'fields': ('title', 'text', 'is_show', 'image')
            }
        ),
        (
            'Author Info',
            {
                'fields': ('author',),
                'classes': ['collapse']
            }
        )
    ]
    raw_id_fields = ['author']

    @admin.action(description='به نمایش در آوردن مقالات انتخاب شده')
    def make_article_published(self, request, queryset):
        updated = queryset.update(is_show=True)
        self.message_user(request, f'{updated} تا مقاله به نمایش در آورده شدند', messages.SUCCESS)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age']

