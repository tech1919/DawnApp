from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout


from libs.uix.components.navbar import Navbar


class DailyScreen(Screen):


    def on_enter(self, *args):
        self.clean_layout()
        layout = DailyLayout()
        self.add_widget(layout)

        list_layout = ListLayout()
        layout.add_widget(list_layout)
        navbar = Navbar()

        navbar_buttons = navbar.children[0].children

        profile_button = navbar_buttons[0]
        diagnose_button = navbar_buttons[1]
        daily_button = navbar_buttons[2]
        home_button = navbar_buttons[3]

        daily_button.change_navbar('daily')

        layout.add_widget(navbar)
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

    def clean_layout(self):
        if len(self.children) > 0:
            self.remove_widget(self.children[0])

class DailyLayout(MDFloatLayout):
    pass

class ProgressCard(MDCard):
    pass

class ListLayout(BoxLayout):
    pass

class DailyScrollView(ScrollView):
    pass

