#!/Users/Ken/anaconda3/envs/prioenv37/bin/python

from py2neo.ogm import GraphObject, Property, Relationship

class Protein(GraphObject):
	__primarykey__ = "uniprotid"
	uniprotid = Property()
