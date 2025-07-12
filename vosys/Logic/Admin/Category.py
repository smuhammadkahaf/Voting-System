from unicodedata import category

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
            self.db.insert_single(table_name,data)
            return 1#

    def update_category(self, data, condition):
        print(data)
        query = "SELECT * FROM categories WHERE category_name = '" + data["category_name"] + "';"
        result = self.db.query(query)
        if result["count_row"] >= 1:
            return False  # categroy already existng

        else:
            self.db.update("categories", data, condition)
        return True

    def get_categories_list(self):
        query = "SELECT category_name FROM categories"
        result = self.db.query(query)
        rows = result["all_rows"]
        categories = []
        for row in rows:
            categories.append(Common.unlocker(row['category_name']))
        return categories

    def get_all_categories(self):
        query = "SELECT * FROM categories ORDER BY id DESC"
        result = self.db.query(query)
        return result["all_rows"]

    def get_category(self,id_):
        query = "SELECT category_name FROM categories WHERE id = " + str(id_) + ";"
        result = self.db.query(query)
        return result["first_row"][0]

    def get_categories_id(self,names):
            query = "SELECT id FROM categories WHERE "
            if not names:
                return []
            query += "category_name = '" + Common.locker(names[0]) + "'"

            for i in range(1, len(names)):
                locked_name = Common.locker(names[i])
                query += " OR category_name = '" + locked_name + "'"

            result = self.db.query(query)
            result = result["all_rows"]
            category_id = []

            for row in result:
                category_id.append(row["id"])
            return category_id


    def get_number_of_categories(self):
        query = "select count(*) as categories from categories;"
        results = self.db.query(query)
        results = results["first_row"][0]["categories"]

        return results
