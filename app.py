import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout



kivy.require('1.9.0')


class MyRoot(BoxLayout):
    def loading_text(self):
        self.ids.my_label.text = "Loading..."


class MyApp(App):
    def build(self):
        return MyRoot()


if __name__ == '__main__':
    MyApp().run()