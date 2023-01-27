"""
2. Написать кастомную менеджент комманду которая удалит пользователей
(https://docs.djangoproject.com/en/4.1/ref/models/querysets/#delete) с указанными id.
Команда принимает id пользователей через пробел.
Запрещено удалять суперпользователя
(https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.is_superuser) - при
наличии хотя бы одного суперпользователя в списке id - команда не должна выполнятся.
(Ожидаю выполнение этой части без использования циклов, но не буду запрещать другие способы)
python manage.py delete_users 1 2 3 4 5
https://docs.djangoproject.com/en/4.1/howto/custom-management-commands/
https://docs.djangoproject.com/en/4.1/ref/models/querysets/#bulk-create
https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_user
https://docs.djangoproject.com/en/4.1/topics/auth/passwords/#django.contrib.auth.hashers.make_password
https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User.set_password
https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html

"""

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Deleting Users, except Superusers'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, nargs="+",
                            help="Enter the user_id's to delete users. The command accepts user ids "
                                 "separated by a space.")

    def handle(self, *args, **options):
        list_delete = options['user_id']
        super_users = User.objects.filter(id__in=list_delete, is_superuser=True)
        if super_users.exists():
            raise CommandError('Can not delete admin user!')

        User.objects.filter(id__in=list_delete).delete()
        self.stdout.write(self.style.SUCCESS("Users successfully deleted."))
