import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._loc = None

    def handle_graph(self, e):
        self._view.txt_result.controls.clear()
        self._model.creaGrafo()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato!\n"
                                                      f"Nodi: {self._model.getNum()[0]}\n"
                                                      f"Archi: {self._model.getNum()[1]}"))
        self.fillDD()
        self._view.update_page()

    def fillDD(self):
        self._view._ddLocalizzazione.options.clear()
        for l in self._model.getAllLoc():
            self._view._ddLocalizzazione.options.append(
                ft.dropdown.Option(text = l, data = l, on_click= self.readLoc)
            )

    def readLoc(self, e):
        if e.control.data is None:
            self._loc = None
        else:
            self._loc = e.control.data

    def handle_statistiche(self, e):
        if self._loc is None:
            self._view.txt_result.controls.append(ft.Text(f"Seleziona una localizzazione"))
            self._view.update_page()
            return
        res = self._model.handleStatistiche(self._loc)
        self._view.txt_result.controls.append(ft.Text(f"Adiacenti a {self._loc}"))
        for r in res:
            self._view.txt_result.controls.append(ft.Text(f"{r[0]}:  {r[1]}"))
        self._view.update_page()



    def handle_search(self, e):
        pass