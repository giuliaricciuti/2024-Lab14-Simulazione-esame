import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Numero di vertici: {self._model.getNum()[0]} "
                    f"Numero di archi: {self._model.getNum()[1]}")
        )
        self._view.txt_result.controls.append(
            ft.Text(f"Informazioni sui pesi degli archi -valore minimo: "
                    f"{self._model.getMinMax()[0]} e valore massimo: "
                    f"{self._model.getMinMax()[1]}")
        )
        self._view.update_page()

    def handle_countedges(self, e):
        self._view.txt_result2.controls.clear()
        soglia = self._view.txt_name.value
        if soglia =="" or soglia is None:
            self._view.txt_result2.controls.append(ft.Text("Inserisci un valore della soglia", color='red'))
            self._view.update_page()
            return
        try:
            int(soglia)
        except ValueError:
            self._view.txt_result2.controls.append(ft.Text("Inserisci un valore intero della soglia", color='red'))
            self._view.update_page()
            return
        maggiore, minore = self._model.getNumSoglia(int(soglia))
        self._view.txt_result2.controls.append(
            ft.Text(f"Numero archi con peso maggiore della soglia: {maggiore}\n"
                    f"Numero archi con peso minore della soglia: {minore}"))
        self._view.update_page()



    def handle_search(self, e):
        pass