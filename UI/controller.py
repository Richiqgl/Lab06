import flet as ft
from model.model import Model

class Controller:
    def __init__(self, view, model:Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def read_retailer(self, e):
        retailer = e.control.data

    def popola_anno(self):
        anni=self._model.restituisci_anni()
        for anno in anni:
            self._view.txt_anno.options.append(ft.dropdown.Option(key=anno['YEAR (gds.`Date`)'], text=anno['YEAR (gds.`Date`)']))
        self._view.update_page()

    def popola_retailer(self):
        retailers=self._model.restituisci_retailer()
        for retailer in retailers:
            self._view.txt_retailer.options.append(ft.dropdown.Option(key=retailer.Retailer_code, text=retailer.Retailer_name,data=retailer,on_click=self.read_retailer))
        self._view.update_page()

    def popola_brand(self):
        brands=self._model.restituisci_brand()
        for brand in brands:
            self._view.txt_brand.options.append(
                ft.dropdown.Option(key=brand["Product_brand"], text=brand["Product_brand"]))
        self._view.update_page()

    def selezione(self):
        brand = self._view.txt_brand.value
        if brand == "None":
            brand = None
        anno = self._view.txt_anno.value
        if anno == "None":
            anno = None
        codice_retailer = self._view.txt_retailer.value
        if codice_retailer == "None":
            codice_retailer = None
        return (brand,anno,codice_retailer)

    def top_vendita(self,e):
        (brand,anno,codice_retailer)=self.selezione()
        valori=self._model.calcolo_top_vendite(brand,anno,codice_retailer)[0:5]
        if valori==[]:
            self._view.txt_result.controls.append(ft.Text("Nessun risultato trovato",color="red"))
            self._view.update_page()
            return
        for elemento in valori:
            self._view.txt_result.controls.append(ft.Text(elemento.__str__()))
        self._view.update_page()


    def analizza_vendita(self,e):
        self._view.txt_result.controls.clear()
        (brand, anno, codice_retailer) = self.selezione()
        valori=self._model.calcolo_top_vendite(brand, anno, codice_retailer)
        (somma,conteggio,retailers,products)=self._model.statistiche_vendite(valori)
        self._view.txt_result.controls.append(ft.Text("Statistiche vendite:"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari:{somma}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vendite {conteggio}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero retailers coinvolti: {retailers}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {products}"))
        self._view.update_page()


