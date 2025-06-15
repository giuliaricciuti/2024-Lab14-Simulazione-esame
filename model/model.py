import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._local = []

    def creaGrafo(self):
        self._graph.clear()
        self._local = DAO.getAllLoc()
        self._graph.add_nodes_from(self._local)
        for e in DAO.getArchi():
            self._graph.add_edge(e.L1, e.L2, weight = e.Peso)


    def getAllLoc(self):
        return DAO.getAllLoc()

    def handleStatistiche(self, loc):
        result = []
        for n in self._graph.neighbors(loc):
            peso = self._graph[loc][n]["weight"]
            result.append((n, peso))
        return result

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()