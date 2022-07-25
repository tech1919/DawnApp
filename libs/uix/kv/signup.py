from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout


class SignupScreen(Screen):
    pass

class SignupLayout(MDFloatLayout):
    pass


class SignupButton(BoxLayout):
    def signup(self):
        print('signup')