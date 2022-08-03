from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout




class LoginScreen(Screen):
    def on_enter(self, *args):
        self.clean_layout()
        layout = LoginLayout()
        self.add_widget(layout)

        # get buttons
        bottom_line_button = self.children[0].children[0]
        login_social_area = self.children[0].children[1]
        login_button = self.children[0].children[2].children[0]
        login_button.bind(on_press = self.verify)






    def verify(self, *args):

        # get the user from the app
        user = App.get_running_app().user

        # get input box
        input_box = self.children[0].children[3]
        self.password_input = input_box.children[1].children[0].children[0]
        self.username_input = input_box.children[3].children[0].children[0]

        user.password = self.password_input.text
        user.username = self.username_input.text

        user.user_info()

    def clean_layout(self):
        if len(self.children) > 0:
            self.remove_widget(self.children[0])


class LoginLayout(MDFloatLayout):
    pass

class LoginSocial(MDFloatLayout):
    pass

class LoginButton(MDCard):
    pass


class BottomLineButton(Button):
    pass

