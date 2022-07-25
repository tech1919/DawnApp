from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import MDFloatLayout

from db_connection import verify_patient



class LoginScreen(Screen):
    pass

class LoginLayout(MDFloatLayout):
    pass

class LoginSocial(MDFloatLayout):

    def hello(self , say):
        print(say)

class LoginButton(MDCard):

    def check(self , say):
        print(say)

    def verify(self , user ,screen_manager):
        user.username = screen_manager.get_screen('login').ids.username_login.text
        user.password = screen_manager.get_screen('login').ids.password_login.text
        # record = DataBase().patient_db().find_one({"Username": user.username, "Password": user.password})
        record = verify_patient({
            'username': user.username,
            'password': user.password
        })

        # print(record)

        if record:
            keys = ['first_name', 'email', 'height', 'weight', 'date_of_birth', 'questions']

            # pulling user information from db
            user_value = [record.get(value) for value in keys]
            first_name_field = user_value[0]
            email_field = user_value[1]
            height_text_field = user_value[2]
            weight_text_field = user_value[3]
            dob_field = user_value[4]
            q = user_value[5]

            if q:
                for answer in q:
                    if answer == 'No':
                        DawnApp.on(self, 'no')
                        DawnApp.render_question(self, 'next_question')
                    if answer == 'Yes':
                        DawnApp.on(self, 'yes')
                        DawnApp.render_question(self, 'next_question')
                    else:
                        pass

            try:
                # if the user didn't yet enter a valid date of birth leave the field empty
                if dob_field == "":
                    user.date_of_birth = ""
                # else the date of birth is a string DD/MM/YYYY and will be pulled from db to fields
                else:
                    dob = dob_field.split("/")
                    dob_day = dob[0]
                    dob_month = dob[1]
                    dob_year = dob[2]

                    # inserting the values of Date of birth from db to details screen
                    screen_manager.get_screen('question_details').ids.day_field.text = dob_day
                    screen_manager.get_screen('question_details').ids.month_field.text = dob_month
                    screen_manager.get_screen('question_details').ids.year_field.text = dob_year
            except:
                pass

            try:
                # inserting the values of height and weight from db to details screen
                screen_manager.get_screen('question_details').ids.height_input.text = height_text_field
                screen_manager.get_screen('question_details').ids.weight_input.text = weight_text_field
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

            DawnApp.go_to(self, 'home')
        else:
            # root = Tk()
            # root.wm_title("DAWN")
            # frm = ttk.Frame(root, padding=100)
            # frm.grid()
            # ttk.Label(frm, text="Please insert correct details").grid(column=0, row=0)
            # ttk.Button(frm, text="Exit", command=root.destroy).grid(column=1, row=0)
            # root.mainloop()
            DawnApp.go_to(self, 'login')

class BottomLineButton(BoxLayout):
    pass

