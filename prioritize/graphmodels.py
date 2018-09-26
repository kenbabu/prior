#!/Users/Ken/anaconda3/envs/prioenv37/bin/python
import os

# activate_this_file = "/Users/Ken/anaconda3/envs/prioenv37/bin/activate_this.py"
# exec(activate_this_file, dict(__file__=activate_this_file))

from py2neo import Graph
import os

neo_password = os.getenv("NEO4J_PASSWORD")
g = Graph(host="localhost", password=os.getenv("NEO4J_PASSWORD"))

qs = """ 
		MATCH(a:Protein)-[r:INTERACTS_WITH]->(b:Protein) 
		WHERE r.interaction_score > 0.6
		RETURN a.uniprotid,b.uniprotid,r.interaction_score LIMIT 100

	"""

hprots = g.run(qs)
print("Password: {}".format(neo_password))

for i in hprots:
	print(i[0], i[1], i[2])