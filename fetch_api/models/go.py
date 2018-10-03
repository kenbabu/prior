from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship
)

class GO(StructuredNode):
    goid =  StringProperty()

    @property
    def serialize(self):
        return {
            'node_properties': {
                'goid': self.uniprotid,
                'id': self.id,
                                },
                }
