from kaki.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.utils.fitimage import FitImage

from libs.uix.components.navbar import Navbar


class ProfileScreen(Screen):

    def on_enter(self, *args):
        self.clean_layout()
        layout = ProfileLayout()
        self.add_widget(layout)


        # get the user from the app
        user = App.get_running_app().user

        # change the navbar
        navbar = Navbar()
        navbar_buttons = navbar.children[0].children
        profile_button = navbar_buttons[0]
        diagnose_button = navbar_buttons[1]
        daily_button = navbar_buttons[2]
        home_button = navbar_buttons[3]
        profile_button.change_navbar('profile')
        layout.add_widget(navbar)

        # add user image
        user_circle = UserImageCircle()
        images_path = 'assets/images/'
        user_circle.add_widget(UserImage(source= f'{images_path}user.png'))
        layout.add_widget(user_circle)

        name = f'{user.first_name} {user.last_name}'
        layout.add_widget(UserNameLabel(text=name))


        my_account_area = layout.children[3].children[2]
        self.update_user_fields(my_account_area,user)





    def clean_layout(self):
        if len(self.children) > 0:
            self.remove_widget(self.children[0])

    def update_user_fields(self,my_account_area,user):
        """
            This function updates the fields in the profile page
            at the My Account area
        """
        key_order = ['weight' ,'height' , 'date_of_birth' , 'last_name' , 'first_name' ]
        title = ['Weight' , 'Height' , 'Date Birth' , 'Last Name', 'First Name']
        user_info = user.user_info(get_object=True)
        box_area_of_fields = my_account_area.children[0].children[0]
        for i in range(len(key_order)):
            box_area_of_fields.children[i].children[0].text = user_info[f'{key_order[i]}']




class ProfileLayout(MDFloatLayout):
    pass

class UserImageCircle(MDCard):
    pass

class UserImage(FitImage):
    pass

class UserNameLabel(Label):
    pass

class MyAccountField_OPEN(BoxLayout):
    pass

class SecurityField_OPEN(BoxLayout):
    pass

class SecurityField_CLOSED(BoxLayout):
    pass

class DiagnoseMe_CLOSED(BoxLayout):
    pass

class DiagnoseMe_OPEN(BoxLayout):
    pass

class MyAccountField_CLOSED(BoxLayout):
    pass