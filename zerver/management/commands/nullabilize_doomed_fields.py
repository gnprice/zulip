
from typing import Any, Callable, Dict, List, Set, Text

from django.db import connection

from zerver.lib.management import ZulipBaseCommand

def nullabilize(cursor: Any, table_name: str, column_name: str) -> None:
    cursor.execute('''
        ALTER TABLE %s
        ALTER %s DROP NOT NULL
    ''' % (table_name, column_name))

def nullabilize_all():
    with connection.cursor() as cursor:
        nullabilize(cursor, 'zerver_userprofile', 'autoscroll_forever')
        nullabilize(cursor, 'zerver_userprofile', 'emoji_alt_code')
        nullabilize(cursor, 'zerver_userprofile', 'quota')

class Command(ZulipBaseCommand):
    help = """Create concurrent indexes for large tables."""

    def handle(self, *args: Any, **options: str) -> None:
        nullabilize_all()
