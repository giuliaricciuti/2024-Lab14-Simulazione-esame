from database.DAO import DAO
from model.model import Model

m = Model()
m.creaGrafo()
print(m.getNum())
print(m.getMinMax())
print(m.getNumSoglia(3))