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

        layout = self.children[0]


        # get the user from the app
        user = App.get_running_app().user

        navbar , my_appointment , _ , _ , _ ,top_box , _ , _ = layout.children

        # update navbar
        profile_button , diagnose_button , daily_button , home_button = navbar.children[0].children
        home_button.change_navbar('home')

        # user image and user name
        user_image = top_box.children[1].children[0]
        user_name = top_box.children[0].children[1]
        # later need to be change the source of the image to the get from the user information
        user_image.source = App.get_running_app().images_source + 'user.png'
        user_name.text = f'Hello {user.first_name}'

class HomeLayout(MDFloatLayout):
    pass

class TopBox(MDBoxLayout):
    pass

class BigButtonBox(BoxLayout):
    pass

class MyAppointment(BoxLayout):
    pass

class HomeUserImage(FitImage):
    pass