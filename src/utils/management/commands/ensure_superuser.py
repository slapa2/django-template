import os
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

class Command(BaseCommand):

    def handle(self, *args, **options):

        if os.environ.get('DJANGO_SUPERUSER_CREATE') != 'true':
            self.stdout.write('creating superuser is off')
            return
        
        self.stdout.write('superuser creating...')
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if User.objects.filter(username='admin').exists():
            self.stdout.write('superuser already created')
            return

        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write('superuser created')