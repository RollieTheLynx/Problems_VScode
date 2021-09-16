#!/usr/bin/env python

# Django's command-line utility for administrative tasks.
# https://www.youtube.com/watch?v=F5mRW0jo-U4

# создается через django-admin startproject project_name
# запускается через python manage.py runserver
# создаем приложение python manage.py startapp core
# добавляем созданное приложение core в settings.py > INSTALLED_APPS
# пишем функцию в views.py приложения 
# импортируем эту функцию в urls.py и прописываем путь: path('index/', index),
# создаем админа python manage.py createsuperuser - http://127.0.0.1:8000/admin/
# создаем дб python manage.py migrate
# когда добавляем новую модель python manage.py makemigrations, python manage.py migrate
# потом в admin.py: from .models import Product, admin.site.register(Product)
# bultin template tags and filters

# // cd C:\Users\Rollie\Documents\Python_Scripts\Problems_VScode\mikesplayground_django
# python manage.py runserver


import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mikesplayground_django.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
