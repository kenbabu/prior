from abc import ABCMeta
from neomodel import db

class NodeUtils:
    __metaclass__ = ABCMeta
    def serialize_relationships(self, nodes):
        serialized_nodes = []
        for node in nodes:
            serialized_node = node.serialize
            # get relationship types
            results, columns = self.cypher('''
                START start_node=node({self}), end_node=node({end_node})
                MATCH (start_node)-[rel]-(end_node)
                RETURN type(rel) as node_relationship
                ''',
                {'end_node': node.id}
            )
            serialized_node['node_relationship'] = results[0][0]
            serialized_nodes.append(serialized_node)
        return serialize_nodes 