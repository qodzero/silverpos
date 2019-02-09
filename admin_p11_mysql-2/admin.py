from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from pymongo import MongoClient
from utils.datatable import DataTable
import mysql.connector

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #     stb = {
    #     'TH0':{0:'St0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH1':{0:'Stm0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH2':{0:'Stmp0',1:'Sampled1.0',2:'Sampled2.0',3:'Sampled4.0'},
    #     'TH3':{0:'Stmpl0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH4':{0:'Stmple0',1:'Sample1',2:'Sample2',3:'Sample4'},
        # print(self.get_products())
    # }
        content = self.ids.scrn_content
        users = self.get_users()
        userstable = DataTable(table=users)
        content.add_widget(userstable)

        #Display Products
        product_scrn = self.ids.scrn_product_content
        products = self.get_products()
        prod_table = DataTable(table=products)
        product_scrn.add_widget(prod_table)

    def get_users(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='#hasH537',
            database='pos'
        )
        mycursor = mydb.cursor()
        _users = OrderedDict()
        _users['first_names'] = {}
        _users['last_names'] = {}
        _users['user_names'] = {}
        _users['passwords'] = {}
        _users['designations'] = {}
        first_names = []
        last_names = []
        user_names = []
        passwords = []
        designations = []

        sql = 'SELECT * FROM users'
        mycursor.execute(sql)
        users = mycursor.fetchall()
        for user in users:
            first_names.append(user[1])
            last_names.append(user[2])
            user_names.append(user[3])
            pwd = user[4]
            if len(pwd) > 10:
                pwd = pwd[:10] + '...'
            passwords.append(pwd)
            designations.append(user[5])
        # print(designations)
        users_length = len(first_names)
        idx = 0
        while idx < users_length:
            _users['first_names'][idx] = first_names[idx]
            _users['last_names'][idx] = last_names[idx]
            _users['user_names'][idx] = user_names[idx]
            _users['passwords'][idx] = passwords[idx]
            _users['designations'][idx] = designations[idx]

            idx += 1
        
        return _users
    # def get_users(self):
    #     client = MongoClient()
    #     db = client.silverpos
    #     users = db.users
    #     _users = OrderedDict()
    #     _users['first_names'] = {}
    #     _users['last_names'] = {}
    #     _users['user_names'] = {}
    #     _users['passwords'] = {}
    #     _users['designations'] = {}
    #     first_names = []
    #     last_names = []
    #     user_names = []
    #     passwords = []
    #     designations = []
    #     for user in users.find():
    #         first_names.append(user['first_name'])
    #         last_names.append(user['last_name'])
    #         user_names.append(user['user_name'])
    #         pwd = user['password']
    #         if len(pwd) > 10:
    #             pwd = pwd[:10] + '...'
    #         passwords.append(pwd)
    #         designations.append(user['designation'])
    #     # print(designations)
    #     users_length = len(first_names)
    #     idx = 0
    #     while idx < users_length:
    #         _users['first_names'][idx] = first_names[idx]
    #         _users['last_names'][idx] = last_names[idx]
    #         _users['user_names'][idx] = user_names[idx]
    #         _users['passwords'][idx] = passwords[idx]
    #         _users['designations'][idx] = designations[idx]

    #         idx += 1
        
    #     return _users
    def get_products(self):
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='#hasH537',
            database='pos'
        )
        mycursor = mydb.cursor()
        _stocks = OrderedDict()
        _stocks['product_code'] = {}
        _stocks['product_name'] = {}
        _stocks['product_weight'] = {}
        _stocks['in_stock'] = {}
        _stocks['sold'] = {}
        _stocks['order'] = {}
        _stocks['last_purchase'] = {}

        product_code = []
        product_name = []
        product_weight = []
        in_stock = []
        sold = []
        order = []
        last_purchase = []
        sql = 'SELECT * FROM stocks'
        mycursor.execute(sql)
        products = mycursor.fetchall()
        for product in products:
            product_code.append(product[1])
            name = product[2]
            if len(name) > 10:
                name = name[:10] + '...'
            product_name.append(name)
            product_weight.append(product[3])
            in_stock.append(product[5])
            sold.append(product[6])
            order.append(product[7])
            last_purchase.append(product[8])
        # print(designations)
        products_length = len(product_code)
        idx = 0
        while idx < products_length:
            _stocks['product_code'][idx] = product_code[idx]
            _stocks['product_name'][idx] = product_name[idx]
            _stocks['product_weight'][idx] = product_weight[idx]
            _stocks['in_stock'][idx] = in_stock[idx]
            _stocks['sold'][idx] = sold[idx]
            _stocks['order'][idx] = order[idx]
            _stocks['last_purchase'][idx] = last_purchase[idx]
           

            idx += 1
        
        return _stocks
    # def get_products(self):
    #     client = MongoClient()
    #     db = client.silverpos
    #     products = db.stocks
    #     _stocks = OrderedDict()
    #     _stocks['product_code'] = {}
    #     _stocks['product_name'] = {}
    #     _stocks['product_weight'] = {}
    #     _stocks['in_stock'] = {}
    #     _stocks['sold'] = {}
    #     _stocks['order'] = {}
    #     _stocks['last_purchase'] = {}

    #     product_code = []
    #     product_name = []
    #     product_weight = []
    #     in_stock = []
    #     sold = []
    #     order = []
    #     last_purchase = []

    #     for product in products.find():
    #         product_code.append(product['product_code'])
    #         name = product['product_name']
    #         if len(name) > 10:
    #             name = name[:10] + '...'
    #         product_name.append(name)
    #         product_weight.append(product['product_weight'])
    #         in_stock.append(product['in_stock'])
    #         sold.append(product['sold'])
    #         order.append(product['order'])
    #         last_purchase.append(product['last_purchase'])
    #     # print(designations)
    #     products_length = len(product_code)
    #     idx = 0
    #     while idx < products_length:
    #         _stocks['product_code'][idx] = product_code[idx]
    #         _stocks['product_name'][idx] = product_name[idx]
    #         _stocks['product_weight'][idx] = product_weight[idx]
    #         _stocks['in_stock'][idx] = in_stock[idx]
    #         _stocks['sold'][idx] = sold[idx]
    #         _stocks['order'][idx] = order[idx]
    #         _stocks['last_purchase'][idx] = last_purchase[idx]
           

    #         idx += 1
        
    #     return _stocks
        
    def change_screen(self, instance):
        if instance.text == 'Manage Products':
            self.ids.scrn_mngr.current = 'scrn_product_content'
        elif instance.text == 'Manage Users':
            self.ids.scrn_mngr.current = 'scrn_content'
        else:
            self.ids.scrn_mngr.current = 'scrn_analysis'


class AdminApp(App):
    def build(self):

        return AdminWindow()

if __name__=='__main__':
    AdminApp().run()