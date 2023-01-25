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
from django.core.management.base import BaseCommand
from django.template.defaultfilters import pluralize


class Command(BaseCommand):
    help = 'Deleting Users, except Superusers'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, nargs="+",
                            help="Enter the user_id's to delete users. The command accepts user ids "
                                 "separated by a space.")

    def handle(self, *args, **options):
        list_delete = options['user_id']
        list_superusers = User.objects.filter(is_superuser=True).values_list('id', flat=True)
        both = set(list_superusers) & set(list_delete)

        if len(both) > 0:
            self.stderr.write(f"Superuser{pluralize(both)} with id {list(both)} cannot be deleted!")
            exit()

        d = User.objects.filter(id__in=list_delete)
        d_id = list(User.objects.filter(id__in=list_delete).values_list('id', flat=True))

        if d.exists():
            d.delete()
            if not d.exists():
                self.stdout.write(self.style.SUCCESS(f"Successfully deleted user{pluralize(d_id)} "
                                                     f"with id: {d_id}"))
            else:
                self.stdout.write(self.style.ERROR('Oops.. something went wrong.'))
        else:
            self.stderr.write(f"User{pluralize(list_delete)} with id {list_delete} do not exist in DataBase.")
