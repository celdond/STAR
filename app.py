from kivy.app import App
from kivy.uix.widget import Widget

class dashboard(Widget):
    pass

class star_app(App):
    def build(self):
        return dashboard()
    
if __name__ == '__main__':
    star_app().run()