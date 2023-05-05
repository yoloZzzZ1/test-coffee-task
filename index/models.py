from django.db import models
from django_resized import ResizedImageField
from django.core.validators import RegexValidator

upload_path_first_section = 'index_page/first_section/'
upload_path_second_section = 'index_page/second_section/'
upload_path_third_section = 'index_page/third_section/'


class BaseInfo(models.Model):

    """ Общая информация для пользователей
    """

    phone_regex = RegexValidator(
        regex=r'^\+7\(\d{4}\) \d{2}-\d{2}-\d{2}$',
        message="Номер телефона должен иметь формат: '+7(XXXX) XX-XX-XX'")

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name='Номер телефона',
        help_text='Необходимо ввести номер телефона',
        blank=True
    )

    email = models.EmailField(
        verbose_name='Электронная почта',
        help_text='Необходимо ввести электронную почту',
        blank=True,
        null=True,
    )
    
    instagram_link = models.URLField(
        max_length=256,
        verbose_name='Ссылка на Instagram',
        help_text='Необходимо ввести ссылку на Instagram',
        blank=True,
        null=True
    )

    vk_link = models.URLField(
        max_length=256,
        verbose_name='Ссылка на VK',
        help_text='Необходимо ввести ссылку на VK',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name='Общая информация'
        verbose_name_plural='Общая информация'


class Contact(models.Model):

    name = models.CharField(
        max_length=256,
        verbose_name='Имя',
        help_text='Имя отправителя',
    )

    phone_number = models.CharField(
        max_length=18,
        verbose_name='Телефон',
        help_text='Номер телефона отправителя',
    )

    email = models.EmailField(
        max_length=64,
        verbose_name='E-mail',
        help_text='E-mail отправителя',
        blank=True,
        null=True
    )

    message = models.TextField(
        max_length=2048,
        verbose_name='Сообщение',
        help_text='Содержание сообщения',
        blank=True,
        null=True
    )


    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'


class FirstSection(models.Model):
    
    """ Информация из первой секции главной страницы
    """

    # не CharField для корректной работы linebreaksbr в шаблонах
    header = models.TextField(
        max_length=128,
        verbose_name='Заголовок',
        help_text='Необходимо ввести заголовок',
        blank=True,
        null=True,
    )

    # не CharField для корректной работы linebreaksbr в шаблонах
    secondary_header = models.TextField(
        max_length=128,
        verbose_name='Второстепенный заголовок',
        help_text='Необходимо ввести второстепенный заголовок',
        blank=True,
        null=True,
    )

    description = models.TextField(
        max_length=1000,
        verbose_name='Описание',
        help_text='Необходимо ввести описание',
        blank=True,
        null=True,
    )

    first_slide = ResizedImageField(
        crop=['middle', 'center'],
        size=[1920, 875],
        force_format='WEBP',
        upload_to=f'{upload_path_first_section}/first_slide',
        verbose_name='Первый слайд',
        help_text='Необходимо загрузить первый слайд',
    )

    second_slide = ResizedImageField(
        crop=['middle', 'center'],
        size=[1920, 875],
        force_format='WEBP',
        upload_to=f'{upload_path_first_section}/second_slide',
        verbose_name='Второй слайд',
        help_text='Необходимо загрузить второй слайд',
    )
    
    third_slide = ResizedImageField(
        crop=['middle', 'center'],
        size=[1920, 875],
        force_format='WEBP',
        upload_to=f'{upload_path_first_section}/third_slide',
        verbose_name='Третий слайд',
        help_text='Необходимо загрузить третий слайд',
    )

    fourth_slide = ResizedImageField(
        crop=['middle', 'center'],
        size=[1920, 875],
        force_format='WEBP',
        upload_to=f'{upload_path_first_section}/fourth_slide',
        verbose_name='Четвёртый слайд',
        help_text='Необходимо загрузить четвёртый слайд',
    )

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name='Первая секция'
        verbose_name_plural='Первая секция'


class SecondSection(models.Model):
    
    """ Информация из второй секции главной страницы
    """

    # не CharField для корректной работы linebreaksbr в шаблонах
    header = models.TextField(
        max_length=128,
        verbose_name='Заголовок',
        help_text='Необходимо ввести заголовок',
        blank=True,
        null=True,
    )

    # не CharField для корректной работы linebreaksbr в шаблонах
    secondary_header = models.TextField(
        max_length=128,
        verbose_name='Второстепенный заголовок',
        help_text='Необходимо ввести второстепенный заголовок',
        blank=True,
        null=True,
    )

    first_object_image = ResizedImageField(
        crop=['middle', 'center'],
        size=[512, 512],
        force_format='WEBP',
        upload_to=f'{upload_path_second_section}/first_object',
        verbose_name='Изображение для первого обьекта',
        help_text='Необходимо загрузить изображение для первого обьекта',
    )

    second_object_image = ResizedImageField(
        crop=['middle', 'center'],
        size=[512, 512],
        force_format='WEBP',
        upload_to=f'{upload_path_second_section}/second_object',
        verbose_name='Изображение для второго обьекта',
        help_text='Необходимо загрузить изображение для второго обьекта',
    )

    third_object_image = ResizedImageField(
        crop=['middle', 'center'],
        size=[512, 512],
        force_format='WEBP',
        upload_to=f'{upload_path_second_section}/third_object',
        verbose_name='Изображение для тртьего обьекта',
        help_text='Необходимо загрузить изображение для третьего обьекта',
    )

    first_object_header = models.TextField(
        max_length=128,
        verbose_name='Заголовок для первого обьекта',
        help_text='Необходимо ввести заголовок',
        blank=True,
        null=True,
    )

    second_object_header = models.TextField(
        max_length=128,
        verbose_name='Заголовок для второго обьекта',
        help_text='Необходимо ввести заголовок',
        blank=True,
        null=True,
    )

    third_object_header = models.TextField(
        max_length=128,
        verbose_name='Заголовок для третьего обьекта',
        help_text='Необходимо ввести заголовок',
        blank=True,
        null=True,
    )

    first_object_desc = models.TextField(
        max_length=1000,
        verbose_name='Описание для первого обьекта',
        help_text='Необходимо ввести описание',
        blank=True,
        null=True,
    )

    second_object_desc = models.TextField(
        max_length=1000,
        verbose_name='Описание для второго обьекта',
        help_text='Необходимо ввести описание',
        blank=True,
        null=True,
    )

    third_object_desc = models.TextField(
        max_length=1000,
        verbose_name='Описание для третьего обьекта',
        help_text='Необходимо ввести описание',
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name='Вторая секция'
        verbose_name_plural='Вторая секция'


class ThirdSection(models.Model):

    """ Информация из третьей секции главной страницы
    """
    
    # не CharField для корректной работы linebreaksbr в шаблонах
    header = models.TextField(
        max_length=128,
        verbose_name='Заголовок',
        help_text='Необходимо ввести заголовок',
        blank=True,
        null=True,
    )

    # не CharField для корректной работы linebreaksbr в шаблонах
    secondary_header = models.TextField(
        max_length=128,
        verbose_name='Второстепенный заголовок',
        help_text='Необходимо ввести второстепенный заголовок',
        blank=True,
        null=True,
    )

    first_slide = ResizedImageField(
        crop=['middle', 'center'],
        size=[1920, 875],
        force_format='WEBP',
        upload_to=f'{upload_path_third_section}/first_slide',
        verbose_name='Первый слайд',
        help_text='Необходимо загрузить первый слайд',
    )

    second_slide = ResizedImageField(
        crop=['middle', 'center'],
        size=[1920, 875],
        force_format='WEBP',
        upload_to=f'{upload_path_third_section}/second_slide',
        verbose_name='Второй слайд',
        help_text='Необходимо загрузить второй слайд',
    )
    
    third_slide = ResizedImageField(
        crop=['middle', 'center'],
        size=[1920, 875],
        force_format='WEBP',
        upload_to=f'{upload_path_third_section}/third_slide',
        verbose_name='Третий слайд',
        help_text='Необходимо загрузить третий слайд',
    )

    fourth_slide = ResizedImageField(
        crop=['middle', 'center'],
        size=[1920, 875],
        force_format='WEBP',
        upload_to=f'{upload_path_third_section}/fourth_slide',
        verbose_name='Четвёртый слайд',
        help_text='Необходимо загрузить четвёртый слайд',
    )

    first_point = models.TextField(
        max_length=328,
        blank=True,
        null=True,
        verbose_name='Первый пункт',
        help_text='Необходимо ввести первый пункт'
    )

    second_point = models.TextField(
        max_length=328,
        blank=True,
        null=True,
        verbose_name='Второй пункт',
        help_text='Необходимо ввести второй пункт'
    )

    third_point = models.TextField(
        max_length=328,
        blank=True,
        null=True,
        verbose_name='Третий пункт',
        help_text='Необходимо ввести третий пункт'
    )

    def __str__(self):
        return str(self.pk)
    
    class Meta:
        verbose_name='Третья секция'
        verbose_name_plural='Третья секция'
