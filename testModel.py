from database.DAO import DAO
from model.model import Model

m = Model()
m.creaGrafo()
print(m.getNum())
loc = "ER"
print(m.handleStatistiche(loc))