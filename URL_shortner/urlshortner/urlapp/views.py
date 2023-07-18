from django.shortcuts import render, redirect

from .backend import processor
from django.db import connections
from .backend import url_shortner_main


def input_page(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        if user_input:
            connection = connections['default']
            long_to_short_url = url_shortner_main.convert_long_to_short_url(connection, user_input)
            return render(request, 'input_page.html', {'result': long_to_short_url})
    else:
        return render(request, 'input_page.html')


def redirect_to_original(request, short_code):
    connection = connections['default']
    short_to_long_url = url_shortner_main.convert_short_to_long_url(connection, short_code)
    if short_to_long_url:
        return redirect(short_to_long_url)
    else:
        return redirect('input_page.html')
