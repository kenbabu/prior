from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship
)
from .nodeutils import NodeUtils

class GO(StructuredNode):
    goid = StringProperty()
    prot = RelationshipFrom('.proteins.Protein', 'HAS_ANNOTATION')

    @property
    def serialize(self):
        return {
            'node_properties': {
                'goid': self.goid,
                'id': self.id,
                                },
                }
