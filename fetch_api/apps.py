from django.apps import AppConfig


class FetchApiConfig(AppConfig):
    name = 'fetch_api'
    def ready(self):
        from prior import constants
