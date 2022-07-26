from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout

from libs.uix.components.navbar import Navbar


class HomeScreen(Screen):

    def on_enter(self, *args):
        layout = HomeLayout()
        self.add_widget(layout)

        navbar = Navbar()

        navbar_buttons = navbar.children[0].children

        profile_button = navbar_buttons[0]
        diagnose_button = navbar_buttons[1]
        daily_button = navbar_buttons[2]
        home_button = navbar_buttons[3]
        home_button.change_navbar('home')

        layout.add_widget(navbar)





class HomeLayout(MDFloatLayout):
    pass