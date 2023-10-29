import time
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import OperationalError as DjangoOperationalError
from psycopg import OperationalError as PsycopgOperationalError
from django.db import connections


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        db_conn = connections['default']
        while not db_up:
            try:
                db_conn.cursor()
                db_up = True
            except (DjangoOperationalError, PsycopgOperationalError):
                self.stdout.write('database unavaiable waiting...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database abvaiable'))