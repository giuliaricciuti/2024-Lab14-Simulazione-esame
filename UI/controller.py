import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._selectedGene= None

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(
            f"Grafo creato!\n#Vertici: {self._model.getNum()[0]}\n"
            f"#Archi: {self._model.getNum()[1]}\n"
        ))
        self.fillDD()
        self._view.update_page()

    def handle_countedges(self, e):
        self._view.txt_result2.controls.clear()
        if self._selectedGene is None:
            self._view.txt_result2.controls.append(ft.Text(
                "Seleziona un gene", color='red'))
            self._view.update_page()
            return
        res = self._model.getAdiacenti(self._selectedGene)
        self._view.txt_result2.controls.append(ft.Text(
            f"Geni adiacenti a {self._selectedGene.GeneID}"))
        for g in res:
            self._view.txt_result2.controls.append(ft.Text(
                f"{g[0]}: {g[1]}"))
        self._view.update_page()

    def handle_search(self, e):
        pass

    def fillDD(self):
        for g in self._model.getGenes():
            self._view.ddGeni.options.append(ft.dropdown.Option(
                text = g.GeneID, data = g, on_click=self.readDD
            ))

    def readDD(self, e):
        if e.control.data is None:
            self._selectedGene = None
        else:
            self._selectedGene = e.control.data
        print(self._selectedGene)