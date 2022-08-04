from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout

from db_connection import add_patient


class SignupScreen(Screen):
    def on_enter(self, *args):
        self.clean_layout()
        layout = SignupLayout()
        self.add_widget(layout)


        # get buttons
        bottom_line_button = self.children[0].children[0]
        login_social_area = self.children[0].children[1]
        singup_button = self.children[0].children[2].children[0]
        singup_button.bind(on_press = self.signup)


    def sign_up(self):
        """
            sign up user to data base
        """


    def signup(self , *args):
        # get the user from the app
        user = App.get_running_app().user

        # get input box
        input_box = self.children[0].children[3]
        self.password_input = input_box.children[0].children[0].children[0]
        self.email_input = input_box.children[2].children[0].children[0]
        self.username_input = input_box.children[4].children[0].children[0]

        user.password = self.password_input.text
        user.email = self.email_input.text
        user.username = self.username_input.text

        add_patient(sign_user=user)
        App.get_running_app().go_to('login')

        # printing the user information
        # user.user_info()


    def clean_layout(self):
        if len(self.children) > 0:
            self.remove_widget(self.children[0])

class SignupLayout(MDFloatLayout):
    pass


class SignupButton(MDCard):
    pass