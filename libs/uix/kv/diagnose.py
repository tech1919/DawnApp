from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.app import App
from libs.uix.components.navbar import Navbar

from datetime import date

class DiagnoseScreen(Screen):

    def on_enter(self, *args):

        layout = self.children[0]

        navbar , diagnostic_info , date_label , _ , _ = layout.children

        # update the navbar
        profile_button, diagnose_button, daily_button, home_button = navbar.children[0].children
        diagnose_button.change_navbar('diagnose')


        # updating the date at the coreect position
        date_format = date.today().strftime("%A, %d %B, %Y")
        date_pos , _ = date_label.children
        date_pos.text = date_format

class DiagnoseLayout(MDFloatLayout):
    pass

class DateLabel(BoxLayout):
    # how to format the date string
    # https: // stackoverflow.com / questions / 311627 / how - to - print - a - date - in -a - regular - format
    pass

# Diagnostics

class Adenomyosis(BoxLayout):
    pass