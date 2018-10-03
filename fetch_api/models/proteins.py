from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship
)

class Protein(StructuredNode):
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
