"""
В текущем репозитории (дз 7):
1. Написать кастомную менеджмент команду которая будет генерировать случайных пользователей
(https://docs.djangoproject.com/en/4.1/ref/models/querysets/#create) c username, email и password.
Команда принимает один обязательный аргумент - количество вновь сгенерированных пользователей.
Значения меньше 1 и больше 10 - должны вызывать ошибку.
(Ожидаю использования bulk_create, но не буду запрещать другие способы)
python manage.py create_users 3.

"""

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.template.defaultfilters import pluralize

from faker import Faker


class Command(BaseCommand):
    help = 'Creating fake Users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('count_of_users', type=int, choices=range(1, 11),
                            help="Enter an integer from 1 to 10 incl. -- the count of fake users.")

    def handle(self, *args, **options):
        fake = Faker()
        objs = [
            User(
                username=fake.name(),
                email=fake.email(),
                password=fake.password()
            )
            for user in range(1, options['count_of_users'] + 1)
        ]
        User.objects.bulk_create(objs)

        self.stdout.write(self.style.SUCCESS(f"Successfully created {options['count_of_users']} "
                                             f"user{pluralize(options['count_of_users'])}!"))
