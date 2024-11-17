#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line

def create_default_admin():
    from django.contrib.auth.models import User
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print('Superusuário padrão criado.')
    else:
        print('Superusuário padrão já existe.')

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ufcsite.settings')
    try:
        # Inicializa o Django antes de criar o superusuário
        import django
        django.setup()
        create_default_admin()
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

if __name__ == '__main__':
    main()