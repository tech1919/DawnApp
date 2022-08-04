from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.screen import MDScreen

from db_connection import verify_patient


class LoginScreen(MDScreen):
    def on_enter(self, *args):
        pass
        # self.clean_layout()
        # layout = LoginLayout()
        # self.add_widget(layout)
        # print(layout)





        # login_button = self.children[0].children[2].children[0]
        # print('check')
        # login_button.bind(on_press = self.verify)

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

        user.password = password_input.text
        user.username = username_input.text

        # printing user information
        user.user_info()

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

            # if q:
            #     for answer in q:
            #         if answer == 'No':
            #             DawnApp.on(self, 'no')
            #             DawnApp.render_question(self, 'next_question')
            #         if answer == 'Yes':
            #             DawnApp.on(self, 'yes')
            #             DawnApp.render_question(self, 'next_question')
            #         else:
            #             pass

            # try:
            #     # if the user didn't yet enter a valid date of birth leave the field empty
            #     if dob_field == "":
            #         user.date_of_birth = ""
            #     # else the date of birth is a string DD/MM/YYYY and will be pulled from db to fields
            #     else:
            #         dob = dob_field.split("/")
            #         dob_day = dob[0]
            #         dob_month = dob[1]
            #         dob_year = dob[2]
            #
            #         # inserting the values of Date of birth from db to details screen
            #         screen_manager.get_screen('question_details').ids.day_field.text = dob_day
            #         screen_manager.get_screen('question_details').ids.month_field.text = dob_month
            #         screen_manager.get_screen('question_details').ids.year_field.text = dob_year
            # except:
            #     pass

            try:
                pass
                # # inserting the values of height and weight from db to details screen
                # screen_manager.get_screen('question_details').ids.height_input.text = height_text_field
                # screen_manager.get_screen('question_details').ids.weight_input.text = weight_text_field
            except:
                pass
            finally:
                # assigning the values for the user pulled previously from db
                user.weight = weight_text_field
                user.height = height_text_field


            # username equals firstname till a field update. once fixed remove comment from next line
            user.first_name = user.username
            # user.first_name = first_name_field
            user.email = email_field
            user.date_of_birth = dob_field

            App.get_running_app().go_to('home')


        else:
            # root = Tk()
            # root.wm_title("DAWN")
            # frm = ttk.Frame(root, padding=100)
            # frm.grid()
            # ttk.Label(frm, text="Please insert correct details").grid(column=0, row=0)
            # ttk.Button(frm, text="Exit", command=root.destroy).grid(column=1, row=0)
            # root.mainloop()
            self.clear_login_screen()
            App.get_running_app().go_to('login')

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

