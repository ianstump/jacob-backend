from django.apps import AppConfig


class TagsAppConfig(AppConfig):
    name = 'project.base.apps.tags'
    verbose_name = _(u"tags")
    label = "tags"

    def ready(self):
        from . import signals  # noqa
