from django.conf.urls import url
from .views import (
    GetNodesCount,
)

app_name = 'fetch_api'
urlpatterns = [
    url(r'^count[/]?$', GetNodesCount.as_view(), name='get_nodes_count'),
]
