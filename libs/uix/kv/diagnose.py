from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivymd.uix.floatlayout import MDFloatLayout

from libs.uix.components.navbar import Navbar

from datetime import date

class DiagnoseScreen(Screen):

    def on_enter(self, *args):
        self.clean_layout()
        layout = DiagnoseLayout()
        self.add_widget(layout)
        navbar = Navbar()
        navbar_buttons = navbar.children[0].children

        profile_button = navbar_buttons[0]
        diagnose_button = navbar_buttons[1]
        daily_button = navbar_buttons[2]
        home_button = navbar_buttons[3]

        diagnose_button.change_navbar('diagnose')
        layout.add_widget(navbar)

        # updating the date at the coreect position
        date_label = DateLabel()
        date_format = date.today().strftime("%A, %d %B, %Y")
        date_pos , _ = date_label.children
        date_pos.text = date_format
        layout.add_widget(date_label)

    def clean_layout(self):
        if len(self.children) > 0:
            self.remove_widget(self.children[0])

class DiagnoseLayout(MDFloatLayout):
    pass

class DateLabel(BoxLayout):
    # how to format the date string
    # https: // stackoverflow.com / questions / 311627 / how - to - print - a - date - in -a - regular - format
    pass

# Diagnostics

class Adenomyosis(BoxLayout):
    pass