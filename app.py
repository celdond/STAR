from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder

Builder.load_file('source_new/ui/dashboard.kv')

class Dashboard(TabbedPanel):

    def __init__(self, **kwargs):
        super(Dashboard, self).__init__(**kwargs)

class StarApp(App):
    def build(self):
        return Dashboard()
    
if __name__ == '__main__':
    StarApp().run()