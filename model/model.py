import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._cromosomi = DAO.getAllChromosomes()

    def creaGrafo(self):
        self._graph.clear()
        self._graph.add_nodes_from(self._cromosomi)
        self._archi = DAO.getArchiPesati()
        for a in self._archi:
            self._graph.add_edge(a.c1, a.c2, weight = a.peso)

    def getMinMax(self):
        massimo = max(self._archi, key=lambda a: a.peso)
        minimo = min(self._archi, key=lambda a: a.peso)
        return minimo.peso, massimo.peso

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getNumSoglia(self, soglia):
        maggiori = 0
        minori = 0
        for a in self._archi:
            if a.peso>soglia:
                maggiori += 1
            elif a.peso<soglia:
                minori += 1
        return maggiori, minori
