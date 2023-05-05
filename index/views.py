from django.shortcuts import render, redirect
from django.core.cache import cache
from .models import (FirstSection, BaseInfo,
                        SecondSection, ThirdSection)
from .forms import AddContactForm

def index(request):
    """
    Функция передачи данных в шаблон index
    Во избежания лишней нагрузки используется кэш (время хранения 1 сек. в качестве демонстрации)
    """ 

    base_info = cache.get('base_info')
    first_section = cache.get('first_section')
    second_section = cache.get('second_section')
    third_section = cache.get('third_section')

    contact_form = AddContactForm()

    if request.method == 'POST':
        form = AddContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index-page')
    else:
        form = AddContactForm()

    if not base_info:
        base_info = BaseInfo.objects.first()
        cache.set('base_info', base_info, timeout=1)

    if not first_section:
        first_section = FirstSection.objects.first()
        cache.set('first_section', first_section, timeout=1)

    if not second_section:
        second_section = SecondSection.objects.first()
        cache.set('second_section', second_section, timeout=1)

    if not third_section:
        third_section= ThirdSection.objects.first()
        cache.set('third_section', third_section, timeout=1)

    context = {
        'first_section':first_section,
        'base_info':base_info,
        'second_section':second_section,
        'third_section':third_section,
        'form':contact_form,
    }

    return render(request, 'index/index.html', context=context)

