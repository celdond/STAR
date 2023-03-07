from kivy.app import App
from kivy.uix.widget import Widget

class Dashboard(Widget):
    pass

class StarApp(App):
    def build(self):
        return Dashboard()
    
if __name__ == '__main__':
    StarApp().run()