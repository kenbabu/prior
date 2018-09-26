import os
from neo4j import GraphDatabase

password = os.getenv('NEO4J_PASSWORD')

class Application(object):
    def __init__(self, uri, user='neo4j', password=password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    def close(self):
        self.driver.close()
def print_interaction_partners(tx, protid):
    qs = """
    MATCH(a:Protein)-[r:INTERACTS_WITH]->(b:Protein)
    WHERE  a.uniprotid = {protid} AND r.interaction_score > 0.6
    RETURN a.uniprotid,b.uniprotid,r.interaction_score
    ORDER BY r.interaction_score DESC
    LIMIT 100
    """
    for rec in tx.run(qs, protid=protid):
        print("{prot1}\t{prot2}\t{score}".format(prot1=rec['a.uniprotid'],
                                            prot2=rec['b.uniprotid'],
                                            score=rec['r.interaction_score']))
def main():
    conn = Application('bolt://localhost:7687')
    if conn:
        print("Connected...")
        sess = conn.driver.session()
        sess.read_transaction(print_interaction_partners, 'Q96A58')
    else:
        print("Connection problem!")

if __name__ == '__main__':
            main()
