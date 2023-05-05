from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from django.utils.html import mark_safe
from django.urls import reverse
from django.utils.html import format_html
from .models import (FirstSection, BaseInfo,
                    SecondSection, ThirdSection,
                    Contact, )


@admin.register(BaseInfo)
class BaseInfoAdmin(admin.ModelAdmin):

    def get_edit_link(self, obj):
        url = reverse('admin:index_baseinfo_change', args=[obj.pk])
        return format_html('<a href="{}">Перейти к редактированию</a>', url)

    def has_add_permission(self, request) -> bool:
        return False
    
    def has_delete_permission(self, request, obj = None) -> bool:
        return False

    get_edit_link.short_description = ''

    list_display = (
        'phone_number',
        'email',
        'instagram_link',
        'vk_link',
        'get_edit_link',
    )

    list_display_links = (
        'get_edit_link',
    )

    fieldsets = (
        ('Контактные данные', {
            'fields': (
                'phone_number',
                'email',
           )
        }),
        
        ('Социальные сети', {
            'fields': (
                'instagram_link',
                'vk_link',
            )
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    def get_edit_link(self, obj):
        url = reverse('admin:index_contact_change', args=[obj.pk])
        return format_html('<a href="{}">Смотреть</a>', url)

    def has_add_permission(self, request) -> bool:
        return False

    def has_change_permission(self, request, obj = ...) -> bool:
        return False

    get_edit_link.short_description = ''

    list_display = (
        'name',
        'phone_number',
        'email',
        'message',
        'get_edit_link',
    )

    list_display_links = (
        'get_edit_link',
    )


@admin.register(FirstSection)
class FirstSectionAdmin(admin.ModelAdmin):

    def get_edit_link(self, obj):
        url = reverse('admin:index_firstsection_change', args=[obj.pk])
        return format_html('<a href="{}">Перейти к редактированию</a>', url)

    def first_slide_screenshot(self, obj):
        if obj.first_slide is None or obj.first_slide == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "400","180",obj.first_slide.url))
        
    def second_slide_screenshot(self, obj):
        if obj.second_slide is None or obj.second_slide == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "400","180",obj.second_slide.url))        

    def third_slide_screenshot(self, obj):
        if obj.third_slide is None or obj.third_slide == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "400","180",obj.third_slide.url))      

    def fourth_slide_screenshot(self, obj):
        if obj.fourth_slide is None or obj.fourth_slide == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "400","180",obj.fourth_slide.url))  

    def has_add_permission(self, request) -> bool:
        return False
    
    def has_delete_permission(self, request, obj = None) -> bool:
        return False

    first_slide_screenshot.short_description = 'Скриншот первого слайда'
    second_slide_screenshot.short_description = 'Скриншот второго слайда'
    third_slide_screenshot.short_description = 'Скриншот третьего слайда'
    fourth_slide_screenshot.short_description = 'Скриншот четвёртого слайда'

    get_edit_link.short_description = ''

    list_display = (
        'header',
        'secondary_header',
        'get_edit_link',
    )

    list_display_links = (
        'get_edit_link',
    )

    readonly_fields = (
        'first_slide_screenshot',
        'second_slide_screenshot',
        'third_slide_screenshot',
        'fourth_slide_screenshot',
    )

    fieldsets = (
        ('Заголовки', {
            'fields': (
                'header',
                'secondary_header',
           )
        }),
        
        ('Слайды', {
            'fields': (
                'first_slide',
                'second_slide',
                'third_slide',
                'fourth_slide',
                'first_slide_screenshot',
                'second_slide_screenshot',
                'third_slide_screenshot',
                'fourth_slide_screenshot',

            )
        }),

        ('Описание', {
            'fields': (
                'description',
            )
        }),
    )


@admin.register(SecondSection)
class SecondSectionAdmin(admin.ModelAdmin):

    def get_edit_link(self, obj):
        url = reverse('admin:index_secondsection_change', args=[obj.pk])
        return format_html('<a href="{}">Перейти к редактированию</a>', url)

    def first_object_screenshot(self, obj):
        if obj.first_object_image is None or obj.first_object_image == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "350","250",obj.first_object_image.url))

    def second_object_screenshot(self, obj):
        if obj.second_object_image is None or obj.second_object_image == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "350","250",obj.second_object_image.url))

    def third_object_screenshot(self, obj):
        if obj.third_object_image is None or obj.third_object_image == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "350","250",obj.third_object_image.url))

    def has_add_permission(self, request) -> bool:
        return False
    
    def has_delete_permission(self, request, obj = None) -> bool:
        return False

    first_object_screenshot.short_description = 'Скриншот изображения для первого обьекта'
    second_object_screenshot.short_description = 'Скриншот изображения для второго обьекта'
    third_object_screenshot.short_description = 'Скриншот изображения для третьего обьекта'

    get_edit_link.short_description = ''

    readonly_fields = (
        'first_object_screenshot',
        'second_object_screenshot',
        'third_object_screenshot',
    )

    list_display = (
        'header',
        'secondary_header',
        'get_edit_link',
    )

    list_display_links = (
        'get_edit_link',
    )

    fieldsets = (
        ('Заголовки', {
            'fields': (
                'header',
                'secondary_header',
           )
        }),
        
        ('Первый обьект', {
            'fields': (
                'first_object_header',
                'first_object_image',
                'first_object_desc',
                'first_object_screenshot',
            )
        }),

        ('Второй обьект', {
            'fields': (
                'second_object_header',
                'second_object_image',
                'second_object_desc',
                'second_object_screenshot',
            )
        }),

        ('Третий обьект', {
            'fields': (
                'third_object_header',
                'third_object_image',
                'third_object_desc',
                'third_object_screenshot',
            )
        }),

    )


@admin.register(ThirdSection)
class ThirdSectionAdmin(admin.ModelAdmin):

    def get_edit_link(self, obj):
        url = reverse('admin:index_thirdsection_change', args=[obj.pk])
        return format_html('<a href="{}">Перейти к редактированию</a>', url)

    def first_slide_screenshot(self, obj):
        if obj.first_slide is None or obj.first_slide == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "400","180",obj.first_slide.url))
        
    def second_slide_screenshot(self, obj):
        if obj.second_slide is None or obj.second_slide == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "400","180",obj.second_slide.url))        

    def third_slide_screenshot(self, obj):
        if obj.third_slide is None or obj.third_slide == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "400","180",obj.third_slide.url))      

    def fourth_slide_screenshot(self, obj):
        if obj.fourth_slide is None or obj.fourth_slide == "":
            return mark_safe('<div class="text-danger">File not found</div>')
        else:
            return mark_safe('<img width=%s height=%s src=%s></iframe>' % (
                       "400","180",obj.fourth_slide.url))  

    def has_add_permission(self, request) -> bool:
        return False
    
    def has_delete_permission(self, request, obj = None) -> bool:
        return False

    first_slide_screenshot.short_description = 'Скриншот первого слайда'
    second_slide_screenshot.short_description = 'Скриншот второго слайда'
    third_slide_screenshot.short_description = 'Скриншот третьего слайда'
    fourth_slide_screenshot.short_description = 'Скриншот четвёртого слайда'

    get_edit_link.short_description = ''

    list_display = (
        'header',
        'secondary_header',
        'get_edit_link',
    )

    list_display_links = (
        'get_edit_link',
    )

    readonly_fields = (
        'first_slide_screenshot',
        'second_slide_screenshot',
        'third_slide_screenshot',
        'fourth_slide_screenshot',
    )

    fieldsets = (

        ('Заголовки', {
            'fields': (
                'header',
                'secondary_header',
           )
        }),
        
        ('Слайды', {
            'fields': (
                'first_slide',
                'second_slide',
                'third_slide',
                'fourth_slide',
                'first_slide_screenshot',
                'second_slide_screenshot',
                'third_slide_screenshot',
                'fourth_slide_screenshot',

            )
        }),

        ('Пункты', {
            'fields': (
                'first_point',
                'second_point',
                'third_point',
           )
        }),
    )
