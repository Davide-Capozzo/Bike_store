from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._products = []
        self._idMapP = {}

    def buildGraph(self, cat):
        #salviamo tutti gli oggetti in una lista
        self._products = DAO.getProductsByCategory(cat)
        for p in self._products:
            self._idMapP[p.product_id] = p

        #siamo pronti ad aggiungere i nodi
        self._graph.add_nodes_from(self._products)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getDateRange(self):
        return DAO.getDateRange()

    def getCategories(self):
        return DAO.getCategorie()