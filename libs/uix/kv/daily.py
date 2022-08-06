from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.app import App

from libs.uix.components.navbar import Navbar


class DailyScreen(Screen):


    def on_enter(self, *args):

        layout = self.children[0]

        navbar , list_layout , _ , _ = layout.children

        profile_button , diagnose_button , daily_button , home_button = navbar.children[0].children
        daily_button.change_navbar('daily')


        self.update_progress_list(list_layout)


    def update_progress_list(self , list_layout):
        if len(list_layout.children) > 0:
            # later need to update this part to update the progress
            # cards to the current values from the user info
            return
        disc_list = [
            "Skin Moisturizing",
            "Body Tempreture",
            "Cardiovascular Efficiency",
            "Blood Pressure",
            "Blood Glucose",
            "Muscle Pressure",

        ]
        values = [
            70,
            21,
            38,
            95,
            82,
            100,
        ]
        for d , val in zip(disc_list , values):
            card = ProgressCard()
            arrow_btn = card.children[0].children[0]
            progress_layout = card.children[0].children[1]
            precent_label = card.children[0].children[2]
            precent_label.text = f'{val}%'
            progress_bar = progress_layout.children[0]
            progress_disc = progress_layout.children[1]
            progress_bar.value = val
            progress_disc.text = d
            list_layout.add_widget(card)

class DailyLayout(MDFloatLayout):
    pass

class ProgressCard(MDCard):
    pass

class ListLayout(BoxLayout):
    pass

class DailyScrollView(ScrollView):
    pass

