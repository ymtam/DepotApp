import kivy
from kivy.app import App
from kivy.uix.button import Button

class FunkyButton(Button):
    pass

class DepotApp(App):
    def build(self):
        return FunkyButton(
            pos=(100,100),
            size=(500,500),
            size_hint=(None,None)
        )

if __name__ == '__main__':
    DepotApp().run()
