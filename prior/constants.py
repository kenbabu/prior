from neomodel import db

proteins = db.cypher_query(
    '''
    MATCH (n: Protein)
    RETURN DISTINCT n.uniprotid AS proteins
    LIMIT 100
    '''
)[0]

goids = db.cypher_query(
    '''
    MATCH (n:GO)
    RETURN DISTINCT n.goid AS goids
    LIMIT 100
    '''
)[0]


GOIDS = sorted([goid[0] for goid in goids])
PROTEINS = sorted([prot[0] for prot in proteins])
# JURISDICTIONS = sorted([jurisdiction[0] for jurisdiction in jurisdictions if isinstance(jurisdiction[0], str)])
# DATASOURCE = sorted([data_source[0] for data_source in data_sources if isinstance(data_source[0], str)])
