import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._geni = DAO.getAllGenes()
        self._idMapGeni = {}
        for g in self._geni:
            self._idMapGeni[g.GeneID]=g

    def creaGrafo(self):
        self._graph.clear()
        self._graph.add_nodes_from(self._geni)
        self.addEdges()

    def addEdges(self):
        archi = DAO.getAllArchi()
        for a in archi:
            u = self._idMapGeni[a[0]]
            v = self._idMapGeni[a[1]]
            if u.Chromosome == v.Chromosome:
                peso = 2*abs(a[2])
            else:
                peso = abs(a[2])
            self._graph.add_edge(u, v, weight=peso)

    def getNum(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getGenes(self):
        return self._geni

    def getAdiacenti(self, gene):
        result = []
        for g in self._graph.neighbors(gene):
            peso = self._graph[gene][g]["weight"]
            result.append((g.GeneID, peso))
        result.sort(key = lambda x: x[1], reverse=True)
        return result