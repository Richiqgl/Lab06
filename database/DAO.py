from database.DB_connect import DBConnect
from model.retail import Retailer
from model.products import Product
from model.sales import Sales
class DAO:
    @staticmethod
    def get_anni():
        try:
            cnx=DBConnect.get_connection()
            cursor=cnx.cursor(dictionary=True)
            query="""SELECT DISTINCT YEAR (gds.`Date`)
                    FROM go_daily_sales gds """
            cursor.execute(query)
            result=cursor.fetchall()
            cursor.close()
            cnx.close()
            return result
        except Exception:
            return None

    @staticmethod
    def get_retailer():
        try:
            cnx = DBConnect.get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                FROM go_retailers gr """
            cursor.execute(query)
            result=[]
            for row in cursor:
                result.append(Retailer(row["Retailer_code"],
                                       row ["Retailer_name"],
                                       row["Type"],
                                       row ["Country"]))
            cursor.close()
            cnx.close()
            return result
        except Exception:
            return None

    @staticmethod
    def get_products():
        try:
            cnx = DBConnect.get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                        FROM go_products gp """
            cursor.execute(query)
            result = []
            for row in cursor:

                result.append(Product(row["Product_number"],
                                        row["Product_line"],
                                          row["Product_type"],
                                           row["Product"],
                                           row["Product_brand"],
                                          row["Product_color"],
                                          row["Unit_cost"],
                                          row["Unit_price"]))
            cursor.close()
            cnx.close()
            return result
        except Exception:
            return None
    @staticmethod
    def ricerca_brand():
        try:
            cnx = DBConnect.get_connection()
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT DISTINCT gp.Product_brand 
                    FROM go_products gp """
            cursor.execute(query)
            result =cursor.fetchall()
            cursor.close()
            cnx.close()
            return result
        except Exception:
            return None
    @staticmethod
    def get_topvendite(anno,brand,codice_retail):
        try:
            cnx = DBConnect.get_connection()
            if cnx is None:
                print("Errore connessione")
                return
            else:
                cursor = cnx.cursor(dictionary=True)
                query = """ SELECT gds.Date , gds.Unit_sale_price * gds.Quantity as Ricavo, gds.Retailer_code, gds.Product_number
                                    FROM go_daily_sales gds, go_products gp  
                                    WHERE gp.Product_number = gds.Product_number 
                                    AND YEAR (gds.Date) = COALESCE (%s, YEAR(gds.Date)) 
                                    AND gp.Product_brand = COALESCE (%s, gp.Product_brand) 
                                    AND gds.Retailer_code = COALESCE (%s, gds.Retailer_code)
                                    ORDER BY (gds.Unit_sale_price*gds.Quantity) DESC"""
                cursor.execute(query, (anno, brand, codice_retail))
                res = []
                rows = cursor.fetchall()
                for row in rows:
                    res.append(Sales(row["Date"],
                                     row["Ricavo"],
                                     row["Retailer_code"],
                                     row["Product_number"]))
                cursor.close()
                cnx.close()

                return res
        except Exception as err:
            print(err)
            return None


if __name__=="__main__":
        print(DAO.get_topvendite("2017","Star",1216))