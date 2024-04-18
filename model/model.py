from database.DAO import DAO
from model.sales import Sales
class Model:

    def restituisci_anni(self):
        return DAO.get_anni()
    def restituisci_retailer(self):
        return DAO.get_retailer()
    def restituisci_prodotti(self):
        return DAO.get_products()
    def restituisci_brand(self):
        return DAO.ricerca_brand()
    def calcolo_top_vendite(self,brand, anno,codice_retail):
       return DAO.get_topvendite(anno,brand,codice_retail)
    def statistiche_vendite(self,lista):
        somma=sum([elemento.Ricavo  for elemento in lista])
        conteggio=len(lista)
        retailers=len(set([elemento.retailer_code for elemento in lista]))
        products = len(set([elemento.product_number for elemento in lista]))
        return somma,conteggio,retailers,products



