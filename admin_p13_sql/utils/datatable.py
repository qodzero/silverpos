from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

from pymongo import MongoClient
from collections import OrderedDict

Builder.load_string('''
<DataTable>:
    id: main_win
    RecycleView:
        viewclass: 'CustLabel'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            cols: 5
            default_size: (None,250)
            default_size_hint: (1,None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5
<CustLabel@Label>:
    bcolor: (1,1,1,1)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos: self.pos
''')
class DataTable(BoxLayout):
    def __init__(self,table='', **kwargs):
        super().__init__(**kwargs)

        # products = self.get_products()
        products = table

         #     stb = {
    #     'TH0':{0:'St0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH1':{0:'Stm0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH2':{0:'Stmp0',1:'Sampled1.0',2:'Sampled2.0',3:'Sampled4.0'},
    #     'TH3':{0:'Stmpl0',1:'Sample1',2:'Sample2',3:'Sample4'},
    #     'TH4':{0:'Stmple0',1:'Sample1',2:'Sample2',3:'Sample4'},

        col_titles = [k for k in products.keys()]
        rows_len = len(products[col_titles[0]])
        self.columns = len(col_titles)
        # print(rows_len)
        table_data = []
        for t in col_titles:
            table_data.append({'text':str(t),'size_hint_y':None,'height':50,'bcolor':(.06,.45,.45,1)})

        for r in range(rows_len):
            for t in col_titles:
                table_data.append({'text':str(products[t][r]),'size_hint_y':None,'height':30,'bcolor':(.06,.25,.25,1)})
        self.ids.table_floor_layout.cols = self.columns
        self.ids.table_floor.data = table_data


    
# class DataTableApp(App):
#     def build(self):

#         return DataTable()

# if __name__=='__main__':
#     DataTableApp().run()