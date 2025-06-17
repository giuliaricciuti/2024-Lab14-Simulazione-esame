from database.DAO import DAO
from model.gene import Gene
from model.model import Model

m = Model()
m.creaGrafo()
print(m.getNum())
g = Gene("G234194", 4)
print(m.getAdiacenti(g))