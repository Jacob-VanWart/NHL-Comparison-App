from kivy.app import App

from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.label import Label



from NHL_Site_Parsing import NHL_Comparison_Offline

class MainWidget(FloatLayout):
    def __init__(self,**kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self.title = 'NHL_APP'
        Window.size=(1200,600)
        self.size=Window.size
        with self.canvas.before:
            Color(0.2,0.2,1,0.2)
            self.rect= Rectangle(size=self.size, pos=self.pos)

        self.image = Image(source='/Users/Jake/Documents/Programming/NHL_Comparison_Offline/hockey_PNG101.png',size_hint=(1,1),pos=(150,0))
        self.add_widget(self.image)
        self.textBox1()

    def textBox1(self):
        self.text1 = TextInput(size_hint=(0.45,0.1),pos=(25,450))
        self.add_widget(self.text1)
        self.text2 = TextInput(size_hint=(0.45,0.1),pos=(620,450))
        self.add_widget(self.text2)
        self.button1()

    def button1(self):
        gobutton = Button(text="Compare",size_hint=(0.5,0.1),pos=(250,50))
        gobutton.bind(on_press=self.buttonClicked)
        self.add_widget(gobutton)


    def buttonClicked(self, instance):
        self.stat1, self.stat2 = NHL_Comparison_Offline(self.text1.text, self.text2.text)
        self.createTable()

    def createTable(self):
        grid = GridLayout(cols=15,size_hint_y=0.25,pos=(20,200))
        header=["NAME", "GP", "GOALS", "ASSISTS", "POINTS", "+/-", "PIM", "SOG",
                         "Shooting %", "GWG", "TOI", "PPG", "PPA", "SHG", "SHA"]
        row1=[self.stat1.name, self.stat1.GP, self.stat1.goals, self.stat1.assists, self.stat1.points,
                         self.stat1.plusminus, self.stat1.pim, self.stat1.sog, self.stat1.shootpct, self.stat1.gwg, self.stat1.avgtoi, self.stat1.ppg, self.stat1.ppa,
                         self.stat1.shgoal, self.stat1.shassist]
        row2=[self.stat2.name, self.stat2.GP, self.stat2.goals, self.stat2.assists, self.stat2.points,
                         self.stat2.plusminus, self.stat2.pim, self.stat2.sog, self.stat2.shootpct, self.stat2.gwg, self.stat2.avgtoi, self.stat2.ppg, self.stat2.ppa,
                         self.stat2.shgoal, self.stat2.shassist]
        with self.canvas:
            Color(0.2,0.2,1,1)
            self.rect= Rectangle(size=(1180,150), pos=(12,190))
        for i in range(0,15):
            if i==0:
                head = Label(text=header[i], bold=True,size_hint_x=None, width=100)
                head.bind(size=head.setter("text_size"))
                grid.add_widget(head)
            else:
                head=Label(text=header[i],bold=True,size_hint=(0.01,1))
                head.bind(size=head.setter("text_size"))
                grid.add_widget(head)

        for n in range(0, 15):
            r1 = Label(text=row1[n], bold=True, size_hint=(0.01, 1))
            r1.bind(size=r1.setter("text_size"))
            grid.add_widget(r1)

        for j in range(0, 15):
            r2 = Label(text=row2[j], bold=True, size_hint=(0.01, 1))
            r2.bind(size=r2.setter("text_size"))
            grid.add_widget(r2)

        self.add_widget(grid)


class NHLApp(App):

     def build(self):

        return MainWidget()



if __name__ == '__main__':
     NHLApp().run()