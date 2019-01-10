from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from collections import OrderedDict
from pymongo import MongoClient

class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #     stb = {
    #     'TH0':{0:'St0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH1':{0:'Stm0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH2':{0:'Stmp0',1:'Sampled1.0',2:'Sampled2.0',3:'Sampled4.0'},
    #     'TH3':{0:'Stmpl0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH4':{0:'Stmple0',1:'Sample1',2:'Sample2',3:'Sample4'},
    # }
    client = MongoClient()
    db = client.silverpos
    users = db.users
    _users = OrderedDict()
    first_names = []
    last_names = []
    user_names = []
    passwords = []
    designations = []
    for user in users.find():
        first_names.append(user['first_name'])
        last_names.append(user['last_name'])
        user_names.append(user['user_name'])
        passwords.append(user['password'])
        designations.append(user['designation'])
    print(designations)



class AdminApp(App):
    def build(self):

        return AdminWindow()

if __name__=='__main__':
    AdminApp().run()