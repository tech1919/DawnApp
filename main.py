import os.path
import time
from datetime import date

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, FadeTransition, NoTransition, SlideTransition
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.list import MDList, TwoLineListItem

from db_connection import add_patient , verify_patient , update_patient
from user import User

path_to_images = 'assets/images/'
path_to_kv = 'kv/'
path_to_classes = 'libs/uix/baseclass'

def delay(seconds):
    start = time.time()
    stop = time.time()
    while stop - start < seconds:
        stop = time.time()

class DemoProject(ScreenManager):
    pass

class DawnApp(MDApp):
################################# LOGIN\SIGUP PAGE ######################################
    def hello(self, say_something):
        print(say_something)
    def google_login(self):
        print("Google login")
    def facebook_login(self):
        print("Facebook login")
    def forgot_password(self):
        print("forgot password")
    def login(self, *args):
        screen_manager.current = "login"
    def render_login_signup_page(self, screen_name):
        screen = self.getScreen(screen_name)
        screen.ids[f'username_{screen_name}'].text = ''
        screen.ids[f'password_{screen_name}'].text = ''
        if screen_name == 'signup':
            screen.ids[f'email_{screen_name}'].text = ''
        screen_manager.current = screen_name
    def on_text_login(self):
        pass
################################# PROFILE PAGE ##########################################
    def profile_changes(self, check):
        print(f'{check} changes made')
    def create_scrollview(self):
        # This function create a scroll view for the profile_diagnoseMe page
        # It uses the self.answers dictionary and displays the questions and the answers
        # of the user in the profile_diagnoseMe page

        screen = screen_manager.get_screen('profile_diagnoseMe')

        if self.first_scroll_view:
            self.first_scroll_view = False
        elif self.first_scroll_view == False:
            # update answers
            list = screen.ids['diagnose_me'].children[0].children[0].children
            # the list of children is fliped
            i = len(list) - 1
            while i >= 0:
                list[i].secondary_text = self.answers[len(list) - i - 1]
                i -= 1
            return

        sv = ScrollView()
        ml = MDList()
        sv.add_widget(ml)

        i = 0
        for q, a in zip(self.questions, self.answers):
            item = TwoLineListItem(
                text=q,
                secondary_text=a,
                font_style='Caption',
            )
            i += 1
            ml.add_widget(item)

        user.create_diagnose(self.questions, self.answers)

        screen.ids['diagnose_me'].add_widget(sv)
    def render_profile_page(self):
        screen_name = 'profile'
        day = screen_manager.get_screen('question_details').ids.day_field.text
        month = screen_manager.get_screen('question_details').ids.month_field.text
        year = screen_manager.get_screen('question_details').ids.year_field.text

        if (day or month or year) == "":
            user.date_of_birth = ""
        else:
            dob_field = f'{day}/{month}/{year}'
            user.date_of_birth = dob_field

        self.change_text('first-last_name', f'{user.first_name} {user.last_name}', screen_name)
        self.change_text('first_name', f'{user.first_name}', screen_name)
        self.change_text('last_name', f'{user.last_name}', screen_name)
        self.change_text('weight', f'{user.weight} kg', screen_name)
        self.change_text('height', f'{user.height} cm', screen_name)
        self.change_text('date_of_birth', f'{user.date_of_birth}', screen_name)
        screen_manager.current = screen_name
    def date_validation(self, text):

        day = screen_manager.get_screen('question_details').ids.day_field.text
        month = screen_manager.get_screen('question_details').ids.month_field.text
        year = screen_manager.get_screen('question_details').ids.year_field.text

        if not day == "":
            if int(day) < 1 or int(day) > 31:
                screen_manager.get_screen('question_details').ids.day_field.text = ""
        if not month == "":
            if int(month) < 1 or int(month) > 12:
                screen_manager.get_screen('question_details').ids.month_field.text = ""
        if not year == "":
            if date.today().year < int(year):
                screen_manager.get_screen('question_details').ids.year_field.text = ""
################################# DIAGNOSE FUNCTIONS ####################################
    def diagnose(self, *args):
        self.root.transition = FadeTransition()
        screen = self.getScreen('diagnose')
        screen.ids['date_diagnose'].text = (date.today().strftime("%A, %d %B, %Y"))
        screen_manager.current = "diagnose"
        self.root.transition = NoTransition()
################################# QUESTION PAGE #########################################
    def on(self, check):
        # This function controls the buttons in the question page
        screen_name = 'question'
        screen = screen_manager.get_screen(screen_name)
        try:
            if check == 'yes':
                answer = 'Yes'
                # change for the user
                user.diagnose[self.cur_question_idx][2] = answer
                self.answers[self.cur_question_idx] = 'Yes'
                screen.ids[f'no_btn'].md_bg_color = get_color_from_hex("#FFFFFF")
                screen.ids[f'no_btn_label'].color = get_color_from_hex("#000000")
            elif check == 'no':
                answer = 'No'
                # change for the user
                user.diagnose[self.cur_question_idx][2] = answer
                self.answers[self.cur_question_idx] = 'No'
                screen.ids[f'yes_btn'].md_bg_color = get_color_from_hex("#FFFFFF")
                screen.ids[f'yes_btn_label'].color = get_color_from_hex("#000000")
            elif check == 'reset':
                screen.ids[f'yes_btn'].md_bg_color = get_color_from_hex("#FFFFFF")
                screen.ids[f'yes_btn_label'].color = get_color_from_hex("#000000")
                screen.ids[f'no_btn'].md_bg_color = get_color_from_hex("#FFFFFF")
                screen.ids[f'no_btn_label'].color = get_color_from_hex("#000000")

            screen.ids[f'{check}_btn'].md_bg_color = get_color_from_hex("#012241")
            screen.ids[f'{check}_btn_label'].color = get_color_from_hex("#FFFFFF")
        except:
            pass
    def render_question(self, operation):
        # if the app go to a question page from a login or signup page
        # the question current number need to reset for starting over
        # if self.last_screen == 'login' or self.last_screen == 'signup':
        # self.cur_question_idx = 0

        screen_name = 'question'
        self.cur_question_idx += 0
        # this operations comes from the user's buttons in the question page
        if operation == 'next_question':
            self.cur_question_idx += 1

        elif operation == 'prev_question' and self.cur_question_idx > 0:
            self.cur_question_idx -= 1


        # if the user finished all of the questions
        if self.cur_question_idx >= self.number_of_questions:
            screen_name = 'question_details'
            screen_manager.current = screen_name
            return screen_name

        q_num = self.cur_question_idx
        self.cur_question_idx = q_num
        self.cur_question = self.questions[q_num]
        # change the text in the page
        self.change_text(f'question_text', self.cur_question, screen_name)
        self.change_text(f'question_number', f'QUESTION {self.cur_question_idx + 1} OF {self.number_of_questions}',
                         screen_name)

        # check if there is an image for the current question
        file_exists = os.path.exists(f'{path_to_images}Q{self.cur_question_idx + 1}.png')
        if file_exists:
            self.change_photo(f'question_img', f'{path_to_images}Q{self.cur_question_idx + 1}.png', screen_name)
        else:
            self.change_photo(f'question_img', f'{path_to_images}Q1.png', screen_name)

        # set the button
        self.on('reset')
        self.on(user.diagnose[self.cur_question_idx][2].lower())

        return screen_name
    def first_question(self, first=False):
        # This function sets up the questions list and the answers dictionary
        self.questions = [
            'Can you now (or could you ever) place your hand flat on the floor without bending your knees?',
            'Can you now (or could you ever) bend your thumb to touch your forearm?',
            'As a child, did you amuse your friends by contorting your body into storage shapes or could you do the splits?',
            'As a child ot teenager, did your shoulder or kneecap dislocate on more than one occasion?',
            'Do you consider yourself "double jointed"?',
            'Unusually soft or velvety skin',
            'Mild skin hyperextensibility',
            'Unexplained striae distensae or rubae at the back, groins, thighs, breasts and/or abdomen in adolescents, men or pre-pubertal women without a history of significant gain or loss of body fat orweight',
            'Bilateral piezogenic papules of the heel',
            'Recurrent or multiple abdominal hernia(s)',
            'Atrophic scarring involving at least nwo sites and without the formation of truly papyraceous and/or hemosideric scars as seen in classical EDS ',
            'Pelvic floor, rectal, and/or uterine prolapse in children, men or nulliparous women without a history of morbid obesity or other known '
            + 'predisposing medical condition',
            'Dental crowding and high or narrow palate',
            'Arachnodactyly, as defined in one or more of the following:' +
            '(1) positive wrist sign (Walker sign) on both sides, (2) positive thumb sign (Steinberg sign) on both sides',
            'Arm span-to-height ratio =1.05',
            'Mitral valve prolapse (MVP) mild or greater based on strict echocardiographic criteria',
            'Aortic root dilatation with Z-score >+2',
            'Musculoskeletal pain in two or more limbs, recurring daily for at least 3 months',
            'Chronic, widespread pain for 3 months or more',
            'Recurrent joint dislocations or frank joint instability, in the absence of trauma'
        ]

        if first:
            self.answers = []
            # first question
            self.cur_question_idx = 0
            self.number_of_questions = len(self.questions)
            for i in range(0, self.number_of_questions):
                self.answers.append('-')

        user.create_diagnose(self.questions, self.answers)

        self.cur_question = self.questions[self.cur_question_idx]
################################# HOME PAGE #############################################
    def render_home_page(self):
        screen_manager.current = 'home'
################################# GENERAL FUNCTIONS #####################################
    def getScreen(self, screen_name):
        return screen_manager.get_screen(screen_name)
    def change_text(self, id, text, screen_name):
        # This function can change the text for a label in a given screen
        screen = screen_manager.get_screen(screen_name)
        screen.ids[id].text = text
    def change_photo(self, id, new_path, screen_name):
        # This function can change an image that has a id
        # in a given screen

        screen = screen_manager.get_screen(screen_name)
        screen.ids[id].source = new_path
    def change_navbar(self, screen_name):
        # This function controls the bottom navigation bar
        # for a given screen_name, the funtion will switch the
        # source of the photo for the navbar to the right one for this screen

        images_ids = ['home', 'daily', 'diagnose', 'profile']
        flag = False
        for id in images_ids:
            if id == screen_name or screen_name == "presplash_diagnose":
                flag = True
                break

        if not flag:
            return

        screen = screen_manager.get_screen(screen_name)
        for id in images_ids:
            screen.ids[f'{id}_btn'].source = f'{path_to_images}{id}.png'

        screen.ids[f'{screen_name}_btn'].source = f'{path_to_images}{screen_name}_p.png'
    def go_to(self, screen_name):
        # saves the last screen before changing
        self.root.transition = NoTransition()
        try:
            if screen_name == 'back':
                self.root.transition = SlideTransition(direction="right")
                screen_name = 'profile'
        except:
            pass
        finally:
            if not self.last_screen == screen_name:
                self.last_screen = screen_manager.current

        # screen = self.getScreen(screen_name)

        try:

            if screen_name == 'question_details':
                self.root.transition = NoTransition()
                screen_manager.current = screen_name
            elif screen_name == 'home':
                screen = self.getScreen(screen_name)
                screen.ids['hello-first_name'].text = f'Hello {user.username}'
                screen_manager.current = screen_name
            elif screen_name == 'question_details_datepick':
                self.root.transition = NoTransition()
                screen_manager.current = screen_name
            elif screen_name == 'diagnose' or screen_name == 'presplash_diagnose':
                screen_manager.current = 'presplash_diagnose'
                Clock.schedule_once(self.diagnose, 2)
            elif screen_name == 'profile':
                self.render_profile_page()
            elif screen_name == 'profile_diagnoseMe':
                screen = screen_manager.get_screen(screen_name)
                screen_manager.current = screen_name
                self.create_scrollview()
                screen.ids['profile_btn'].source = f'{path_to_images}profile_p.png'
            elif screen_name == 'profile_security':
                screen = screen_manager.get_screen(screen_name)
                screen_manager.current = screen_name
                screen.ids['profile_btn'].source = f'{path_to_images}profile_p.png'
            elif screen_name == 'next_question' or screen_name == 'prev_question' or screen_name == 'question':
                if self.last_screen == 'login':
                    self.root.transition = SlideTransition(direction='up')
                if self.last_screen == 'question_details' and screen_name == 'prev_question':
                    self.root.transition = SlideTransition(direction='right')
                elif self.last_screen == 'home':
                    self.cur_question_idx = 0
                elif screen_name == 'prev_question' and self.cur_question_idx == 0:
                    screen_manager.current = 'profile'
                    return
                else:
                    self.root.transition = SlideTransition(direction='left')

                screen_name = self.render_question(screen_name)
                screen_manager.current = screen_name

                i = 0
                for q in self.questions:
                    #        print(self.answers[i], f'number: {i + 1}')
                    i += 1

            elif screen_name == 'home':
                self.render_home_page()
            elif screen_name == 'login' or screen_name == 'signup':
                self.render_login_signup_page(screen_name)
            else:
                self.root.transition = NoTransition()
                screen_manager.current = screen_name
        except:
            # in case on an error, the app go to profile page
            print(f'error in {screen_name}')
            screen_manager.current = 'profile'

        self.change_navbar(screen_name)
################################# DATABASE FUNCTIONS ####################################

    # function verifies if user exist and assigning data from db to user
    # if not exist pops up a message
    def verify(self):
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
    # sign up a user to db
    def sign_up(self):
        user.username = screen_manager.get_screen('signup').ids.username_signup.text
        user.password = screen_manager.get_screen('signup').ids.password_signup.text
        # data = DataBase()
        add_patient(sign_user=user)
        DawnApp.go_to(self, 'login')
    def question(self):
        i = 0
        for q in self.questions:
            print(self.answers[i], f'number: {i + 1}')
            i += 1
    # updates the details from the diagnostic question and the parameters of height and weight
    # the function is called after pressing the "next" button on question details screen
    def update_patient(self):
        # output = answers to all question yes/no
        output = [x[2] for x in user.diagnose]

        # stores the values of user Height and Weight
        user.weight = screen_manager.get_screen('question_details').ids.weight_input.text
        user.height = screen_manager.get_screen('question_details').ids.height_input.text

        # stores the values of user date of birth
        day = screen_manager.get_screen('question_details').ids.day_field.text
        month = screen_manager.get_screen('question_details').ids.month_field.text
        year = screen_manager.get_screen('question_details').ids.year_field.text
        dob_string = f'{str(day)}/{str(month)}/{str(year)}'
        user.date_of_birth = dob_string

        diagnose = self.update_diagnose()
        # date
        # updates the DB: finds according username and set the values for
        # height,weight,date of birth, diagnose and questions
        update_patient({'username': user.username}, {'height': user.height, 'weight': user.weight, "date_of_birth": user.date_of_birth,
                     "diagnose": diagnose, 'questions': output})

    # checks if diagnose fits the criteria
    # first critera at least 2/5, second critera 5/12, third critera 1/3
    def update_diagnose(self):
        list_for_diagnostic = [x[2] for x in user.diagnose]
        diagnose = ""
        first_counter = 0
        for criteria_one in range(5):
            if list_for_diagnostic[criteria_one] == 'Yes':
                first_counter += 1
        if first_counter >= 2:
            second_counter = 0
            for criteria_two in range(5, 17):
                if list_for_diagnostic[criteria_two] == 'Yes':
                    second_counter += 1
            if second_counter >= 5:
                third_counter = 0
                for criteria_three in range(17, 20):
                    if list_for_diagnostic[criteria_three] == 'Yes':
                        third_counter += 1
                if third_counter >= 1:
                    diagnose = "ADS"

        return diagnose
################################# BUILD FUNCTIONS #######################################
    def build(self):

        # set the first question in line
        global screen_manager
        global user

        user = User('', '', '', '', '', '', '')

        Window.clearcolor = get_color_from_hex("#F5E5D6")
        self.first_scroll_view = True
        self.icon = f'{path_to_images}app_logo.png'
        self.first_question(first=True)
        self.last_screen = 'login'

        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'login.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'profile.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'signup.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'daily.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'home.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'profile_diagnoseMe.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'profile_security.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'diagnose.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'presplash_diagnose.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'question.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'question_details.kv'))
        screen_manager.add_widget(Builder.load_file(path_to_kv + 'question_details_datepick.kv'))

        return screen_manager
    def on_start(self):
        # This function waits for 3 seconds in the presplash screen
        # until switching to the login screen

        Clock.schedule_once(self.login, 3)
    def keypad_listener(self, pos_hint, state):
        # This Function shifts the screen to the point where the
        # focused text field is above the middle of the screen for using the phone's keypad
        screen_name = screen_manager.current
        if state == True:
            ypos = pos_hint['center_y']
            # delay one second
            delay(0.3)
            # get the screen
            self.scrollPage(ypos, screen_name)
        else:
            self.scrollPage(0.7, screen_name)
    def scrollPage(self, to_h, screen_name):
        screen = self.getScreen(screen_name)
        offset = 0.7 - to_h
        screen.children[0].pos_hint = {"center_x": 0.5, "center_y": 0.5 + offset}

if __name__ == '__main__':
    DawnApp().run()
