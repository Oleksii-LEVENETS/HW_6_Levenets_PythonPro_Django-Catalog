from django.contrib import admin

from .models import Logger, Person


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email', 'get_attr', )
    # fields = ('last_name', 'first_name', 'email')
    # fieldsets = [
    #     ("Surname", {"fields": ["last_name"], }),
    #     ("Name", {"fields": ["first_name"], }),
    #     ("Email", {"fields": ["email"], }),
    # ]

    fieldsets = [
        ("Surname", {"fields": ["last_name"], }),
        ("Name", {"fields": ["first_name"], }),
        ('Email', {'fields': ['email', ], 'classes': ['wide', ]}),  # collapse wide
    ]

    list_display_links = ('last_name', 'first_name', 'email', 'get_attr', )
    list_per_page = 10
    # autocomplete_fields =
    # raw_id_fields =
    save_as = True

    # date_hierarchy =
    def get_attr(self, obj):
        return 11


@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    list_display = ['id', 'timestamp', 'path', 'method', 'request_data', 'run_time', ]
    # fields = ('last_name', 'first_name', 'email')
    # fieldsets = [
    #     ("Surname", {"fields": ["last_name"], }),
    #     ("Name", {"fields": ["first_name"], }),
    #     ("Email", {"fields": ["email"], }),
    # ]

    # fieldsets = [
    #     ("Surname", {"fields": ["last_name"], }),
    #     ("Name", {"fields": ["first_name"], }),
    #     ('Email', {'fields': ['email', ], 'classes': ['wide', ]}),  # collapse wide
    # ]
    #
    # list_display_links = ('last_name', 'first_name', 'email', 'get_attr',)
    # list_per_page = 10
    # # autocomplete_fields =
    # # raw_id_fields =
    # save_as = True
