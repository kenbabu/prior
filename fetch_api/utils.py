from .models import Protein

MODEL_ENTITIES = {
'Protein': Protein,
}

def filter_nodes(node_type, search_text, protein):
    if node_type.__name__ == 'Protein':
        node_set.filter(uniprotid_icontains=search_text)
    return node_set

def count_nodes(count_info):
    count = {}
    node_type               = count_info['node_type']
    search_word             = count_info['name']
    country                 = count_info['country']
    jurisdiction            = count_info['jurisdiction']
    data_source             = count_info['sourceID']
    node_set                = filter_nodes(MODEL_ENTITIES[node_type], search_word, country, jurisdiction, data_source)
    count['count']          = len(node_set)

    return count


def fetch_nodes(fetch_info):
    node_type       = fetch_info['node_type']
    search_word     = fetch_info['name']
    country         = fetch_info['country']
    limit           = fetch_info['limit']
    start           = ((fetch_info['page'] - 1) * limit)
    end             = start + limit
    jurisdiction    = fetch_info['jurisdiction']
    data_source     = fetch_info['sourceID']
    node_set        = filter_nodes(MODEL_ENTITIES[node_type], search_word, country, jurisdiction, data_source)
    fetched_nodes   = node_set[start:end]

    return [node.serialize for node in fetched_nodes]


def fetch_node_details(node_info):
    node_type       = node_info['node_type']
    node_id         = node_info['node_id']
    node            = MODEL_ENTITIES[node_type].nodes.get(node_id=node_id)
    node_details    = node.serialize

    # Make sure to return an empty array if not connections

def fetch_countries():
    return PROTEINS


def fetch_jurisdictions():
    return HPO


def fetch_data_source():
    return GO