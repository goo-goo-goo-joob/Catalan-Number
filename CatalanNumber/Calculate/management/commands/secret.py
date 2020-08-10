from os import urandom

from django.core.management.base import BaseCommand

alphabet = r"0123456789qwertyuiopasdfghjklzxcvbnm[];',./{}:>?<!@#$%^&*()_+=-"


def get_int():
    n = 0
    for _ in range(4):
        n = (n << 2) + ord(urandom(1))
    return n


class Command(BaseCommand):
    help = 'Init secret file'
    requires_migrations_checks = False
    requires_system_checks = False
    def handle(self, *args, **options):
        with open("secret.txt", "w") as f:
            for i in range(100):
                f.write(alphabet[get_int() % len(alphabet)])
        self.stdout.write('Created successfully')
