from kaki.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
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
        navbar = layout.children[1]
        navbar_buttons = navbar.children[0].children
        profile_button = navbar_buttons[0]
        profile_button.change_navbar('profile')


        # add user image
        layout.ids['user_image_pos'].add_widget(UserImage(source='assets/images/user.png'))

        # add user name label
        layout.ids['user_name_label'].text = f'{user.first_name} {user.last_name}'

        self.switch_main_profile_fields(2)

    def switch_main_profile_fields(self , switch_to , *args):
        switch_to -= 1
        main1 = MainProfileBoxLayout1()
        main2 = MainProfileBoxLayout2()
        main3 = MainProfileBoxLayout3()
        option = [main1 , main2 , main3]


        layout = self.children[0]
        # this widget is located always first
        old_main = layout.children[0]
        layout.remove_widget(old_main)
        new_main = option[switch_to]
        layout.add_widget(new_main)


        if switch_to == 0:
            # button1 = self.get_mdicon_button(new_main.children[2].children[0].children[1])
            button2 = self.get_mdicon_button(new_main.children[1].children[0].children[0])
            button2.bind(on_press=lambda a: self.switch_main_profile_fields(2))
            button3 = self.get_mdicon_button(new_main.children[0].children[0].children[0])
            button3.bind(on_press=lambda a: self.switch_main_profile_fields(3))

            # if area one is open
            self.update_user_fields(new_main.children[2])

        elif switch_to == 1:
            button1 = self.get_mdicon_button(new_main.children[2].children[0].children[0])
            button1.bind(on_press=lambda a: self.switch_main_profile_fields(1))
            # button2 = self.get_mdicon_button(new_main.children[1].children[0].children[0])
            button3 = self.get_mdicon_button(new_main.children[0].children[0].children[0])
            button3.bind(on_press=lambda a: self.switch_main_profile_fields(3))

            # create the scrollview in area two
            self.create_sv_diagnose(new_main.children[1])

        elif switch_to == 2:
            button1 = self.get_mdicon_button(new_main.children[2].children[0].children[0])
            button1.bind(on_press=lambda a: self.switch_main_profile_fields(1))
            button2 = self.get_mdicon_button(new_main.children[1].children[0].children[0])
            button2.bind(on_press=lambda a: self.switch_main_profile_fields(2))
            # button3 = self.get_mdicon_button(new_main.children[0].children[0].children[0])

    def get_mdicon_button(self , area):
        check = '_ButtonBehavior__state_event'

        list = area.children
        for item in list:
            keys = dir(item)
            if keys[0] == check:
                return item

        return False

    def clean_layout(self):
        if len(self.children) > 0:
            self.remove_widget(self.children[0])

    def update_user_fields(self,my_account_area):
        """
            This function updates the fields in the profile page
            at the My Account area

            the my_account_area is the MyAccountField_OPEN widget
        """

        user = App.get_running_app().user
        key_order = ['weight' ,'height' , 'date_of_birth' , 'last_name' , 'first_name' ]
        title = ['Weight' , 'Height' , 'Date Birth' , 'Last Name', 'First Name']
        user_info = user.user_info(get_object=True)
        box_area_of_fields = my_account_area.children[0].children[0]
        for i in range(len(key_order)):
            box_area_of_fields.children[i].children[0].text = user_info[f'{key_order[i]}']

    def create_sv_diagnose(self,diagnose_me_area):
        user = App.get_running_app().user
        questions = App.get_running_app().questions

        sv_box = diagnose_me_area.children[0].children[0]
        sv = ScrollView()
        ml = MDList()
        sv.add_widget(ml)
        for q , a in zip(questions , user.answers):
            ml.add_widget(
                TwoLineListItem(
                    text=q,
                    secondary_text= a
                )
            )

        sv_box.add_widget(sv)


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

class MainProfileBoxLayout1(BoxLayout):
    pass

class MainProfileBoxLayout2(BoxLayout):
    pass

class MainProfileBoxLayout3(BoxLayout):
    pass