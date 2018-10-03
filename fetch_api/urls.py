from django.conf.urls import url
from .views import (
    GetNodesCount,
    GetNodesData,
    GetNodeData,
)

app_name = 'fetch_api'
urlpatterns = [
    url(r'^count[/]?$', GetNodesCount.as_view(), name='get_nodes_count'),
    url(r'^nodes[/]?$', GetNodesData.as_view(), name='get_nodes_count'),
    url(r'^node[/]?$', GetNodeData.as_view(), name='get_node_data'),
]
