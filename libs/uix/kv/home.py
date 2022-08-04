from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.utils.fitimage import FitImage

from libs.uix.components.navbar import Navbar


class HomeScreen(Screen):

    def on_enter(self, *args):
        self.clean_layout()
        layout = HomeLayout()
        self.add_widget(layout)

        # get the user from the app
        user = App.get_running_app().user

        # Navbar
        navbar = Navbar()
        navbar_buttons = navbar.children[0].children
        profile_button = navbar_buttons[0]
        diagnose_button = navbar_buttons[1]
        daily_button = navbar_buttons[2]
        home_button = navbar_buttons[3]
        home_button.change_navbar('home')
        layout.add_widget(navbar)


        # user image and user name
        top_box = TopBox()
        image_circle = top_box.children[1]
        images_path = 'assets/images/'
        image_circle.add_widget(UserImage(source=f'{images_path}user.png'))

        _ , name_label = top_box.children[0].children
        name_label.text = f'Hello {user.first_name}'
        layout.add_widget(top_box)



    def clean_layout(self):
        if len(self.children) > 0:
            self.remove_widget(self.children[0])
class HomeLayout(MDFloatLayout):
    pass

class UserImage(FitImage):
    pass

class TopBox(MDBoxLayout):
    pass

class BigButtonBox(BoxLayout):
    pass

class MyAppointment(BoxLayout):
    pass