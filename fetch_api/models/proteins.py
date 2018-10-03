
from .nodeutils import NodeUtils
from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship
)

class Protein(StructuredNode, NodeUtils):
    uniprotid = StringProperty()
    # drugs = RelationshipFrom('.drug.Drug', 'TARGETS')
    go = RelationshipTo('.go.GO', 'HAS_ANNOTATION')

    @property
    def serialize(self):
        return {
            'node_properties': {
                'uniprotid': self.uniprotid,
                'id': self.id,
                                },
                }
    @property
    def serialize_connections(self):
        # Define all the relationships that a node has  with the other
        # nodes in the database.
        return [
            {
                'nodes_type':'GO',
                'nodes_related': self.serialize_relationships(self.go.all()),
            },
        ]
