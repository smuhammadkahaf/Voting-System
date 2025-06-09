from Includes.BaseClass import BaseClass
from Includes.Common import Common

class Category(BaseClass):

    def __init__(self):
        super().__init__()
        self.ensure_db()

    def create_category(self,categoryName):
        name  = Common.locker(categoryName)
        query = "SELECT * FROM categories WHERE category_name = '" + name + "';"
        result = self.db.query(query)
        if result["count_row"] >=1:
            return 0 #categroy already existng
        else:
            table_name  = "categories"
            data = {
                "category_name": name
            }
            self.db.insert(table_name,data)
            return 1#

    def update_category(self, data, condition):
        self.db.update("categories", data, condition)

    def get_all_categories(self):
        query = "SELECT * FROM categories ORDER BY id DESC"
        result = self.db.query(query)
        return result["all_rows"]

    def get_category(self,id_):
        query = "SELECT category_name FROM categories WHERE id = " + str(id_) + ";"
        result = self.db.query(query)
        return result["first_row"][0]