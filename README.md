# HW_6-7-8-9-10_Levenets_PythonPro_Django-Catalog
========================================
ДЗ 10. Django Forms
Створено: 24.01.2023 21:33
Заняття 11. MVC, func-based views, forms

1. Выполнять в текущем проекте (можете создать еще одно приложение)
Добавить вью по пути /triangle.
На этой вью необходимо использовать форму, которая будет принимать значения двух катетов треугольника
(положительные, больше нуля, для простоты используйте int значения если хотите). 
После отправки формы, если значения были валидными - на этой же странице вывести значение гипотенузы.

Это должна быть одна view.
Можете использовать 1 или 2 темплейта при необходимости для рендера формы и результата.
Если один темплейт - значение гипотенузы по умолчанию None - проверяйте его в темплейте, и на основании того
None или "значение" рендерите форму или значение гипотенузы.
template.html
if gip
  <p> гипотенуза равна gip
form.as_p
в этом случае вы не будете использовать redirect
Использовать только формы. Модели не нужно.
TLDR:
- 1 form
- 1 url
- 1 view (get and get+submit)
- 1 or 2 template
- redirect - optional

========================================
ДЗ 9. OneToOneField, ForeignKey, ManyToManyField
Створено: 20.01.2023 21:45
Заняття 10. Django management commands, django-extensions

1. Реализовать в приложении (catalog созданной в одном из предшествующих заданий) модели использующие 
поля OneToOneField, ForeignKey, ManyToManyField.
2. Использовать graph_models из django-extensions, чтобы отобразить структуру моделей ТОЛЬКО этого приложения. 
Результат - изображение сопоставимое с представленным в ридми файле репозитория
https://github.com/Pyromanser/django_example_project/

Учтите, что для работы этой команды необходимо доустановить зависимости в систему.
Если у вас не получается - можете составить условную диаграмму связей между таблицами самостоятельно.

Пример:
Город
Клиент (MTM на товар, FK на город)
Товар
Поставщик (OTO на город)

3. Написать по запросу из инстанса одной модели в другую по каждой из связей (всего 3 запроса).
...
city = City.objects.get(id=1)
city."<model>_set".filter(date__year=2022).order_by("-date")
<SQL>
retailer = Retailer.objects.get(id=1)
retailer.city
<SQL>
...
Для создания запроса используйте shell_plus --print-sql что бы ваш SQL отобразился в консоли.

Ожидаю:
-- Ссылка на репозиторий
-- Прикрепленный скрин с диаграммой связей между таблицами (и/или наличие его в репозитории)
-- Запрос и его SQL версия (текст или скрин в комментарии и/или в репозитории)
![catalog_models.png](https://github.com/Oleksii-LEVENETS/HW_6_Levenets_PythonPro_Django-Catalog/blob/main/graph_models/catalog_models.png?raw=true)
========================================
ДЗ 8. queryset methods, management commands
Створено: 20.01.2023 21:44
Заняття 10. Django management commands, django-extensions

В текущем репозитории (дз 7):
1. Написать кастомную менеджмент команду, которая будет генерировать случайных пользователей
(https://docs.djangoproject.com/en/4.1/ref/models/querysets/#create) c username, email и password.
Команда принимает один обязательный аргумент - количество вновь сгенерированных пользователей. 
Значения меньше 1 и больше 10 - должны вызывать ошибку.
(Ожидаю использования bulk_create, но не буду запрещать другие способы)
python manage.py create_users 3
2. Написать кастомную менеджмент команду, которая удалит пользователей 
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
3. Создать файл фикстур используя менеджмент команду dumpdata 
(https://docs.djangoproject.com/en/4.1/ref/django-admin/#dumpdata)
https://docs.djangoproject.com/en/4.1/ref/django-admin/#what-s-a-fixture
https://coderwall.com/p/mvsoyg/django-dumpdata-and-loaddata (секция Restore fresh database)

=======================================
ДЗ 7. Flake8, Travis CI
Створено: 13.01.2023 21:42
Заняття 8. Flake8, Travis CI, django queryset
1. В текущий репозиторий (ДЗ-6), добавить flake8 с дополнительными модулями
   (flake8-django, flake8-import-order, flake8-builtins, flake8-print).
2. Настроить файл конфигураций для него и проверить свой код на предмет ошибок, исправить их.
3. Зарегистрироваться на travis ci и добавить интеграцию в github.
4. Добавить файл настроек для этого-же и настроить его так, что бы новый коммит проверялся
   flake8 средствами travis ci.

========================================
ДЗ 6. Django
Створено: 06.01.2023 22:32
Заняття 6. Django
1. В новом репозитории.
2. Инициализоровать новый django проект с последней версией django.
3. Зайти в папку репозитория "django-admin startproject <project_name> . "
   (точка в конце -- путь куда положить файлы проекта, в данном случае -- текущая папка).
4. В .gitignore добавить (удостовериться в наличии) файл базы данных, папку виртуального окружения
   (если она в папке проекта) и папку настроек среды разработки.
5. Создать requirements.txt (или Pipfile + Pipfile.lock в зависимости от используемого).
6. Создать django приложение catalog (python manage.py startapp <app_name>) и добавить его в INSTALLED_APPS
7. Убедиться что SECRET_KEY будет взят из переменных окружения и НЕ будет храниться в репозитории
   (os.environ.get("SECRET_KEY", "<def value>")).
8. README.md - описать проект.
Жду ссылки на репозиторий.
