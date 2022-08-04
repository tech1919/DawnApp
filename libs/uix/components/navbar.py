from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.floatlayout import MDFloatLayout


def press(object , id):
    image_source = 'assets/images/'
    button_ids = ['home_btn', 'daily_btn', 'diagnose_btn', 'profile_btn']
    image_names = ['home.png', 'daily.png', 'diagnose.png', 'profile.png']
    navbar = object.parent.parent
    pressed_button = object.children

    for button , image in zip(button_ids , image_names):
        navbar.ids[button].children[1].icon = image_source + image
    pressed_button[1].icon = f'{image_source}{id}_p.png'

class Navbar(MDFloatLayout):
    pass


class HomeButton(BoxLayout):
    def change_navbar(self , id):
        press(self , id)
class DailyButton(BoxLayout):
    def change_navbar(self,id):
        press(self,id)

class DiagnoseButton(BoxLayout):
    def change_navbar(self , id):
        press(self , id)
class ProfileButton(BoxLayout):
    def change_navbar(self,id):
        press(self,id)


