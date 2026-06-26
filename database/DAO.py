from database.DB_connect import DBConnect
from model.category import Category
from model.product import Product


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getCategorie():

        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * from categories c"

        cursor.execute(query)

        for row in cursor:
            results.append(Category(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def getDateRange():

        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct (order_date) from orders o order by order_date"

        cursor.execute(query)

        for row in cursor:
            results.append(row["order_date"])

        first = results[0]
        last = results[-1]

        cursor.close()
        conn.close()
        return first, last

    @staticmethod
    def getProductsByCategory(c):

        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from products p where p.category_id = %s """

        cursor.execute(query, (c.category_id,))

        for row in cursor:
            results.append(Product(**row))

        cursor.close()
        conn.close()
        return results