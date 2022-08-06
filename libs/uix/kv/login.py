from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

from dawn_animations import scroll_up_animation
from db_connection import verify_patient
from libs.uix.components.loader import DawnLoader


class LoginScreen(MDScreen):
    def on_enter(self, *args):
        self.pos = [0.5 , 0.5]

        layout = self.children[0]

        # check loader
        # loader = DawnLoader()
        # layout.add_widget(loader)

        login_button = layout.children[2].children[0]
        login_button.bind(on_press = self.verify)


    def clear_login_screen(self):
        input_box = self.children[0].children[3]
        password_input = input_box.children[1].children[0].children[0]
        username_input = input_box.children[3].children[0].children[0]

        password_input.text = ''
        username_input.text = ''

    def verify(self, *args):


        # get the user from the app
        user = App.get_running_app().user

        # get input box
        input_box = self.children[0].children[3]
        password_input = input_box.children[1].children[0].children[0]
        username_input = input_box.children[3].children[0].children[0]

        loader = DawnLoader()
        self.children[0].add_widget(loader)


        user.password = password_input.text
        user.username = username_input.text

        # printing user information
        # user.user_info()

        record = verify_patient({
            'username': user.username,
            'password': user.password
        })

        # print(record)


        if record:

            user.update_local_by(record)
            # pulling user information from db
            # user_value = [record.get(value) for value in keys]
            first_name_field = user.first_name
            email_field = user.email
            height_text_field = user.height
            weight_text_field = user.weight
            dob_field = user.date_of_birth
            q = user.questions

            user.weight = weight_text_field
            user.height = height_text_field

            # username equals firstname till a field update. once fixed remove comment from next line
            user.first_name = user.username
            # user.first_name = first_name_field
            user.email = email_field
            user.date_of_birth = dob_field

            self.children[0].remove_widget(loader)
            App.get_running_app().go_to('home')


        else:
            # root = Tk()
            # root.wm_title("DAWN")
            # frm = ttk.Frame(root, padding=100)
            # frm.grid()
            # ttk.Label(frm, text="Please insert correct details").grid(column=0, row=0)
            # ttk.Button(frm, text="Exit", command=root.destroy).grid(column=1, row=0)
            # root.mainloop()

            self.children[0].remove_widget(loader)
            self.clear_login_screen()
            App.get_running_app().go_to('login')

    def clean_layout(self):
        if len(self.children) > 0:
            self.remove_widget(self.children[0])

    def scroll_layout(self , destination, *args):

        if self.pos == [0.5 , 0.5]:
            scroll_up_animation(self, destination)
            self.pos = [0.5 , 0.8]
        else:
            scroll_up_animation(self,0.5)
            self.pos = [0.5, 0.5]
    
class LoginLayout(MDFloatLayout):
    pass

class LoginSocial(MDFloatLayout):
    pass

class LoginButton(MDCard):
    pass

class BottomLineButton(Button):
    pass

