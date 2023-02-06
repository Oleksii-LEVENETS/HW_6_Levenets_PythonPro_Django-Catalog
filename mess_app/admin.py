from django.contrib import admin
from django.db.models import Avg
from django.utils.html import format_html

from .models import Logger, Person


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email',)

    fieldsets = [
        ("Surname", {"fields": ["last_name"], }),
        ("Name", {"fields": ["first_name"], }),
        ('Email', {'fields': ['email', ], 'classes': ['wide', ]}),
    ]

    list_display_links = ('last_name', 'first_name', 'email',)
    list_per_page = 10
    save_as = True


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'path', 'method', 'request_data', 'run_time', "average_run_time"]

    def average_run_time(self, obj):
        result = Logger.objects.filter(method=obj.method).aggregate(Avg("run_time"))
        return format_html("<b><i>{}</i></b>", round(result["run_time__avg"], 7))

    average_run_time.short_description = "Average Method Run-Time"
    list_filter = ('timestamp', 'method', )
    search_fields = ('id', 'timestamp', 'path', 'method', 'request_data', 'run_time',)
    # fields = ('path', ('method', 'request_data', ), 'run_time',)
    fieldsets = (
        (None, {
            'fields': ('path',)
        }),
        ('Method & Request Data', {
            'fields': (('method', 'request_data',),)
        }),
        ('Advanced options', {
            'fields': ('run_time',),
            'classes': ('collapse', 'wide',),
        }),
    )

    date_hierarchy = 'timestamp'
    actions_on_top = False
    actions_on_bottom = True
    actions_selection_counter = True  # By default
    empty_value_display = '-empty-'
    save_as = True
    list_per_page = 10
    list_display_links = ('id', 'timestamp', 'path', 'method', 'request_data', 'run_time', "average_run_time",)
