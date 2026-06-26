import datetime

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDCategories(self):
        categories = self._model.getCategories()
        categoriesDDOptions = list(map(lambda x:ft.dropdown.Option(data= x, key= x.category_name,
                                                                   on_click = self._chioceCategory), categories))
        self._view._ddcategory.options = categoriesDDOptions
        self._view.update_page()

    def _chioceCategory(self, e):
        self._categoryValue = e.control.data

    def handleCreaGrafo(self, e):
        pass

    def handleBestProdotti(self, e):
        pass

    def handleCercaCammino(self, e):
        pass



    def setDates(self):
        first, last = self._model.getDateRange()

        self._view._dp1.first_date = datetime.date(first.year, first.month, first.day)
        self._view._dp1.last_date = datetime.date(last.year, last.month, last.day)
        self._view._dp1.current_date = datetime.date(first.year, first.month, first.day)

        self._view._dp2.first_date = datetime.date(first.year, first.month, first.day)
        self._view._dp2.last_date = datetime.date(last.year, last.month, last.day)
        self._view._dp2.current_date = datetime.date(last.year, last.month, last.day)
