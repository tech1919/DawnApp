from kivy.app import App
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

from dawn_animations import scroll_up_animation
from db_connection import update_patient
from libs.uix.components.navbar import Navbar


class ProfileScreen(Screen):

    def on_enter(self, *args):

        # get the user from the app
        user = App.get_running_app().user

        # for scroll method
        self.pos = [0.5, 0.5]


        layout = self.children[0]

        # change the navbar
        navbar = layout.children[1]
        navbar_buttons = navbar.children[0].children
        profile_button = navbar_buttons[0]
        profile_button.change_navbar('profile')

        # add user image
        user_image = layout.ids['user_image']
        user_image.source = App.get_running_app().images_source + '/user.png'

        # add user name label
        layout.ids['user_name_label'].text = f'{user.first_name} {user.last_name}'

        # using thread
        self.switch_main_profile_fields(1)

    def switch_main_profile_fields(self , switch_to , *args):
        switch_to -= 1
        main1 = MainProfileBoxLayout1()
        main2 = MainProfileBoxLayout2()
        main3 = MainProfileBoxLayout3()
        main4 = MainProfileBoxLayout4()
        option = [main1 , main2 , main3 , main4]


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
        elif switch_to == 3:
            # button1 = self.get_mdicon_button(new_main.children[2].children[0].children[1])
            button2 = self.get_mdicon_button(new_main.children[1].children[0].children[0])
            button2.bind(on_press=lambda a: self.switch_main_profile_fields(2))
            button3 = self.get_mdicon_button(new_main.children[0].children[0].children[0])
            button3.bind(on_press=lambda a: self.switch_main_profile_fields(3))

    def get_mdicon_button(self , area):
        check = '_ButtonBehavior__state_event'

        list = area.children
        for item in list:
            keys = dir(item)
            if keys[0] == check:
                return item

        return False

    def scroll_layout(self , destination, *args):

        if self.pos == [0.5 , 0.5]:
            scroll_up_animation(self, destination)
            self.pos = [0.5 , 0.8]
        else:
            scroll_up_animation(self,0.5)
            self.pos = [0.5, 0.5]

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


    def edit_profile(self):
        layout = self.children[0]


        edit_button = layout.children[-1].children[0]
        if edit_button.icon == App.get_running_app().images_source + 'edit.png':
            # change the button's image to plus sign
            edit_button.icon =  App.get_running_app().images_source + 'plus_btn.png'

            # use a function built to switch correctly
            # the main open field at the profile screen
            # field 4 is correlate with MainProfileBoxLayout4 class
            self.switch_main_profile_fields(4)


        else:
            # change back the icon from plus to the edit icon
            edit_button.icon = App.get_running_app().images_source + 'edit.png'

            main_field = layout.children[0]
            main_field.get_update_info()

            # update the user at the data base
            user = App.get_running_app().user
            query = {'username' : user.username}
            update_fields = user.user_info(get_object=True)
            update_patient(query ,update_fields)

            # switch back to main field 1
            self.switch_main_profile_fields(1)


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

class MyAccountField_EDIT_OPEN(BoxLayout):
    pass

class MyAccountField_CLOSED(BoxLayout):
    pass

class MainProfileBoxLayout1(BoxLayout):
    pass

class MainProfileBoxLayout2(BoxLayout):
    pass

class MainProfileBoxLayout3(BoxLayout):
    pass

class MainProfileBoxLayout4(BoxLayout):
    def get_update_info(self):
        edit_field = self.children[2].children[0].children[0]
        weight , height , date_of_birth , last_name , first_name = edit_field.children
        weight = self.get_text(weight)
        height = self.get_text(height)
        date_of_birth = self.get_text(date_of_birth , date=True)
        last_name = self.get_text(last_name).capitalize()
        first_name = self.get_text(first_name).capitalize()

        user = App.get_running_app().user
        user.first_name = first_name
        user.last_name = last_name
        user.weight = weight
        user.height = height
        user.date_of_birth = date_of_birth

    def get_text(self , field , date = False):
        if date:
            year,_,month,_,day = field.children[0].children
            date_of_birth = f'{day.text}/{month.text}/{year.text}'
            return date_of_birth
        else:
            return field.children[0].text

