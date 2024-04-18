from dataclasses import dataclass
from datetime import time
@dataclass
class Sales:
    Date:time
    Ricavo:float
    retailer_code:int
    product_number:int

    def __eq__(self, other):
        return self.Date==other.data and self.retailer_code==other.retailer.Retailer_code and self.product_number==other.product_number
    def __hash__(self):
        return hash((self.Date,self.product_number,self.retailer_code))

    def __str__(self):
        return f"Data:{self.Date}; Ricavo:{self.Ricavo}; retailer-code:{self.retailer_code}; product_number:{self.product_number}"


