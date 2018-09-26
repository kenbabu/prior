from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship
)

class Protein(StructuredNode):
    uniprotid =  StringProperty()
    
