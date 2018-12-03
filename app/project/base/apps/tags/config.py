from django.apps import AppConfig


class TagsAppConfig(AppConfig):

    def ready(self):
        from . import signals  # noqa
