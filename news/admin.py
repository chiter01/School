from django.contrib import admin
from news.models import News
from django.utils.safestring import mark_safe


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'name', 
        'date',
        'is_published',
        'get_image', 
    )
    list_display_links = ('id', 'name')
    list_editable = ('is_published',)
    search_fields = (
        'name', 
        'description', 
    )
    list_filter = ('is_published', 'date',)

    readonly_fields = (
        'date',
        'get_full_image',
    )


    @admin.display(description='Изображение')
    def get_image(self, instance: News):
        if instance.image:
            return mark_safe(f'<img src="{instance.image.url}" width="100px">')
        return '-'
    
    @admin.display(description='Изображение')
    def get_full_image(self, instance: News):
        if instance.image:
            return mark_safe(f'<img src="{instance.image.url}" width="50%">')
        return '-'


