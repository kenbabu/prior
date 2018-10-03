from fetch_api.models import Protein
from fetch_api.models  import GO
from prior.constants import  GOIDS

MODEL_ENTITIES = {
'Protein': Protein,
'GO': GO,
}

def filter_nodes(node_type, search_text):
    node_set = node_type.nodes
    # node_set = node_set.filter(uniprotid__exact=search_text)
    node_set.filter(uniprotid__icontains=search_text)


    # if node_type == 'Protein':
    #     node_set.filter(uniprotid_icontains=search_text)
    # node_set.filter(uniprotid_icontains=search_text)
    return node_set

def count_nodes(count_info):
    # print('Modified function')
    count = {}
    node_type   = count_info['node_type']
    # print('node_type: {}'.format(node_type))
    search_word = count_info['text']
    # go                      = count_info['go']
    # hpo                     = count_info['hpo']
    node_set = filter_nodes(MODEL_ENTITIES[node_type], search_word)
    count['count'] = len(node_set)
    return count


def fetch_nodes(fetch_info):
    node_type       = fetch_info['node_type']
    search_word     = fetch_info['search_text']
    # protein         = fetch_info['protein']
    limit           = fetch_info['limit']
    start           = ((fetch_info['page'] - 1) * limit)
    end             = start + limit
    # hpo    = fetch_info['hpo']
    # go     = fetch_info['go']
    node_set        = filter_nodes(MODEL_ENTITIES[node_type], search_word)
    fetched_nodes   = node_set[start:end]

    return [node.serialize for node in fetched_nodes]


def fetch_node_details(node_info):
    node_type       = node_info['node_type']
    node_id         = node_info['node_id']
    node            = MODEL_ENTITIES[node_type].nodes.get(uniprotid=node_id)
    node_details    = node.serialize

    # Make sure to return an empty array if not connections
    node_details['node_connections'] = []
    if (hasattr(node, 'serialize_connections')):
        print("Node has relationships")
        node_details['node_connections'] = node.serialize_connections
    return node_details


def fetch_proteins():
    return PROTEINS


def fetch_hpos():
    return HPO


def fetch_goids():
    return GOIDS
